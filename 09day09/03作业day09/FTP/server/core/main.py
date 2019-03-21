#!/usr/bin/env python3
#author:Alnk(李成果)
import socketserver
import struct
import json
import os
import hashlib
from conf.settings import IP, PORT, user_info_file, db_base

class FTPServer(socketserver.BaseRequestHandler):
    def handle(self):
        while 1:
            try:
                data_length = self.request.recv(4)
                info_length = struct.unpack('i', data_length)[0]  # 解包
                info = json.loads(self.request.recv(info_length))
            except Exception:
                break
            if hasattr(self, info['action']):
                getattr(self, info['action'])(info)

    def __recv_write_file(self, file_path, file_size, exist_size=0, mode='wb' ):  # 接收数据，写入文件
        with open(file_path, mode) as f:
            recv_data = 0
            while recv_data < file_size - exist_size:
                data = self.request.recv(1024)
                f.write(data)
                recv_data += len(data)

    def __get_md5_and_size(self,file_path):  # 获取md5和文件大小
        md5 = hashlib.md5()
        size = 0
        with open(file_path, 'rb') as f:
            for line in f:
                md5.update(line)
                size += len(line)
        return md5.hexdigest(),size

    def __get_info_dict(self,file_path):  # 获取用户信息
        with open(file_path, 'r') as f:  # 读取用户信息
            msg_dict = json.load(f)
        return msg_dict

    def __write_info_dict(self, file_path, info_dict):  # 修改磁盘配额数据，并且写入文件
        with open(file_path, 'w') as f:
            json.dump(info_dict, f)
            f.flush()

    def __file_send_to_client(self, file_path, pointer=0):  # 传输文件到服务器
        # pointer 指针，默认为0
        already_size = 0
        with open(file_path, 'rb') as f:
            f.seek(pointer)  # 调整指针位置
            for line in f:
                self.request.send(line)  # 循环发送数据到服务器
                already_size += len(line)

    def __info_send_to_client(self, msg):  # 发送给服务端的报头信息
        bites_msg = json.dumps(msg).encode()
        bites_len = len(bites_msg)
        msg_pack = struct.pack('i', bites_len)
        last_msg = msg_pack + bites_msg
        self.request.send(last_msg)

    def login(self, info):  # 登录
        msg_dict = self.__get_info_dict(user_info_file)
        if msg_dict.get(info['name']) and msg_dict[info['name']]['pwd'] == info['pwd']:  # 判断账号密码
            self.request.send(b'OK')  # 登录成功标志位
        else:
            self.request.send(b'NO')  # 登录失败标志位

    def put(self, info):  # 上传
        name = info['name']  # 用户名
        file_name = info['file_name']  # 文件名
        file_size = info['file_size']  # 文件大小
        file_md5 = info['file_md5']  # md5
        file_path = os.path.join(db_base, name, file_name)  # 文件路径
        msg_dict = self.__get_info_dict(user_info_file)  # 服务器用户信息表
        if file_size > msg_dict[info['name']]['quota']:  # 判断磁盘配额是否足够
            self.request.send(b'NO QUOTA')
            return False
        if os.path.isfile(file_path):  # 待上传的文件存在了，断点续传或者不需要传输
            exist_md5, exist_size = self.__get_md5_and_size(file_path)  # 获取已经存在的文件的大小和md5
            if file_md5 == exist_md5:  # 同一个文件，不在需要上传了
                self.request.send(b'NO')
            else:  # 断点续传
                self.request.send(str(exist_size).encode())  # 直接发送服务器文件的大小给服务端
                self.__recv_write_file(file_path, file_size, exist_size=exist_size, mode='ab')  # 接收数据，写入文件
                msg_dict[info['name']]['quota'] -= file_size   # 减少磁盘配额
                self.__write_info_dict(user_info_file, msg_dict)  # 写入用户信息文件
                recv_md5 = self.__get_md5_and_size(file_path)[0]  # 获取md5
                if file_md5 == recv_md5:  # 如果md5 相等，证明没有丢包，上传完成
                    self.request.send(b'OK')
                else:
                    self.request.send(b'NO')
        else:  # 待上传的文件不存在，全额传输
            self.request.send(b'NO EXIST')  # 发送给客户端的标志位
            self.__recv_write_file(file_path, file_size)  # 接收数据，写入文件
            msg_dict[info['name']]['quota'] -= file_size  # 减少磁盘配额
            self.__write_info_dict(user_info_file, msg_dict)  # 写入用户信息文件
            recv_md5 = self.__get_md5_and_size(file_path)[0]  # 获取md5
            if file_md5 == recv_md5:  # 如果md5 相等，证明没有丢包，上传完成
                self.request.send(b'OK')
            else:
                self.request.send(b'NO')

    def get(self, info):  # 下载
        user_name = info['name']  # 用户名称
        file_name = info['file_name']  # 需要传输给客户端的文件名称
        file_md5 = info['file_md5']  # md5
        pointer = info['pointer']  # 指针，服务端不做断点续传判断，直接seek 指针的位置就行了
        file_path = os.path.join(db_base, user_name, file_name)  # 客户端请求下载的文件的路径
        if os.path.isfile(file_path):  # 如果文件存在
            md5, file_size = self.__get_md5_and_size(file_path)  # 获取本地文件的md5 和大小
            if file_md5 == md5:  # 需要下载的文件已经在客户端完整的存在了
                info = {'file_size': file_size, 'file_md5': md5, 'stat': 'EXIST'}
                self.__info_send_to_client(info)  # 发送报头给客户端
            elif 0 < pointer < file_size:  # 断点续传
                file_size -= pointer
                info = {'file_size': file_size, 'file_md5': md5, 'stat': 'NO'}  # 断点续传
                self.__info_send_to_client(info)  # 发送报头给客户端
                self.__file_send_to_client(file_path, pointer=pointer)  # 发送文件给客户端
            else:  # 全额传输
                file_size -= pointer  # 传给客户端的文件大小要减去客户端已经存在的文件大小
                info = {'file_size': file_size, 'file_md5': md5, 'stat': 'OK'}
                self.__info_send_to_client(info)  # 发送报头给客户端
                self.__file_send_to_client(file_path, pointer=pointer)  # 发送文件给客户端
        else:
            info = {'file_size': None, 'file_md5': None, 'stat': 'NO EXIST'}
            self.__info_send_to_client(info)  # 发送报头给客户端
            print('需要下载的文件不存在')
            return False

    def ls(self, info):  # 显示
        pass

    def mk(self, info):  # 新建
        pass

    def rm(self, info):  # 删除
        pass

    def cd(self, info):  # 切换目录
        pass


def run():
    fs = socketserver.ThreadingTCPServer((IP, PORT), FTPServer)
    fs.serve_forever()
