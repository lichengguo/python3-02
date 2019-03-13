#!/usr/bin/env python3
#author:Alnk(李成果)
import socketserver
import json
import struct
import os
from conf.settings import IP, PORT, user_info_path, db_path
from core.basic import Basic


class FTPServer(socketserver.BaseRequestHandler, Basic):  # 服务端
    def handle(self):
        while 1:
            # 针对windows
            print('等待请求...')
            try:
                data = self.request.recv(4)
            except Exception as e:
                break
            # 针对linux
            if len(data) == 0:
                break
            info_length = struct.unpack('i', data)[0]  # 解包，获取客户端传过来的字典信息长度
            info_data_bites = self.request.recv(info_length)  # 接收客户端传过来的字典信息
            info_dict = json.loads(info_data_bites.decode())  # 转化成字典
            print('##########',info_dict)
            action = info_dict['action']
            if hasattr(self, action):
                getattr(self, action)(info_dict)
            else:
                print('客户端传参有误')

    def login(self,info_dict):  # 登录
        user_dict = self.read_info(user_info_path)  # 读取登录文件
        # 判断账号和密码
        if user_dict.get(info_dict['name']):
            if user_dict.get(info_dict['name'])['pwd'] == info_dict['pwd']:
                print('登陆成功')
                self.request.send(b'OK')
                return True
            else:
                print('密码错误')
                self.request.send(b'NO')
                return False
        else:
            print('账号密码错误')
            self.request.send(b'NO')
            return False

    def put(self,info_dict):  # 上传
        file_path = os.path.join(db_path, info_dict['name'], info_dict['parameter'])  # 用户家目录下的文件
        recv_size = 0  # 已经接收的文件的大小
        if os.path.isfile(file_path):  # 断点续传
            with open(file_path, 'rb') as f:
                for line in f:
                    recv_size += len(line)
            recv_size_str = str(recv_size)  # 转换成str格式
            self.request.send(recv_size_str.encode())  # 在哪里断开传输的发送给客户端
        else:
            self.request.send(b'NO')  # 告诉客户端，这个文件之前没传过

        user_dict = self.read_info(user_info_path)  # 读取登录文件
        filesize = info_dict['filesize']  # 传入文件总大小
        if filesize > user_dict[info_dict['name']]['quota']:   # 文件大小要小于磁盘配额才能传入，不然就返回NO
            self.request.send(b'NO')
            print('磁盘空间不够啦')
            return False
        else:
            user_dict[info_dict['name']]['quota'] -= filesize  # 上传文件以后磁盘配额要减少
            self.write_info(user_info_path, user_dict)  # 用户信息写入到文件
            self.request.send(b'OK')
        total_recv = 0  # 已经接收的大小

        with open(file_path, 'ab') as f:
            while total_recv < filesize - recv_size:  # 如果该文件上传过那么，需要减去之前上传的
                data = self.request.recv(1024)
                file_md5 = self.get_md5(data)
                f.write(data)
                total_recv += len(data)
        if file_md5 == info_dict['md5']:  # md5校验
            print('传输完成')
            self.request.send(b'OK')
        else:
            print('文件有丢包')
            self.request.send(b'NO')


def run():
    server = socketserver.ThreadingTCPServer((IP, PORT), FTPServer)
    server.serve_forever()
