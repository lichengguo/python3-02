#!/usr/bin/env python3
# author:Alnk(李成果)
import socket
import struct
import json
import hashlib
import os
import sys
from conf.settings import IP, PORT


class FTPClient():

    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
        self.sock = socket.socket()
        self.__connect_server()

    def __connect_server(self):  # 连接服务器
        self.sock.connect((IP, PORT))

    def __info_send_to_server(self, msg):  # 发送给服务端的报头信息
        bites_msg = json.dumps(msg).encode()
        bites_len = len(bites_msg)
        msg_pack = struct.pack('i', bites_len)
        last_msg = msg_pack + bites_msg
        self.sock.send(last_msg)

    def __file_send_to_server(self, file_path, file_size, pointer=0):  # 传输文件到服务器
        # pointer 指针，默认为0
        already_size = 0  # 已经传递给服务器大小
        with open(file_path, 'rb') as f:
            f.seek(pointer)  # 调整指针位置
            for line in f:
                self.sock.send(line)  # 循环发送数据到服务器
                already_size += len(line)
                self.__view_bar(already_size, file_size - pointer)  # 进度条

    def __size_and_md5(self, file):  # 统计文件字节数和md5
        md5 = hashlib.md5()
        size = 0
        with open(file, 'rb') as f:
            for line in f:
                size += len(line)
                md5.update(line)
            return size, md5.hexdigest()

    def get_md5(self, content):  # 密码md5
        md5 = hashlib.md5()
        md5.update(content.encode())
        return md5.hexdigest()

    def __view_bar(self, already_size, total_size):  # 进度条
        num = int((already_size / total_size) * 100)
        r = '\r%s%s%%' % ('>' * num, num)
        sys.stdout.write(r)
        sys.stdout.flush

    def run(self):
        ret = self.login()
        if ret:
            msg = '''
            -- 欢迎使用ftp客户端 --
                1 上传文件
                2 下载文件
                3 显示目录
                4 新建目录
                5 删除目录
                6 切换目录
                7 退出
            '''
            msg_dic = {
                '1': 'put',
                '2': 'get',
                '3': 'ls',
                '4': 'mk',
                '5': 'rm',
                '6': 'cd',
                '7': 'logout',
            }
            while 1:
                print(msg)
                choose = input('输入编号>>>')
                if msg_dic.get(choose):
                    if hasattr(self, msg_dic[choose]):
                        getattr(self, msg_dic[choose])()
                else:
                    print('编号输错了，请重新输入！')
        else:
            print('登录失败了！')

    def login(self):  # 登录
        pwd = self.get_md5(self.pwd)  # 密码进行md5加密
        msg = {'action': 'login', 'name': self.name, 'pwd': pwd}
        self.__info_send_to_server(msg)
        flag = self.sock.recv(1024).decode()
        if flag == 'OK':
            return True
        else:
            return False

    def put(self):  # 上传
        cmd = input('输入命令>>>')
        try:
            action, parameter = cmd.replace(' ', '').split('|')
        except Exception:
            print('提示: put | filename')
            return False
        if action == 'put' and os.path.isfile(parameter):  # 判断输入的命令是否合法
            file_size,file_md5 = self.__size_and_md5(parameter)  # 获取文件大小和md5
            file_name = os.path.basename(parameter)  # 获取命令参数中的文件名
            info = {'action': action, 'file_name': file_name, 'file_size': file_size, 'file_md5': file_md5, 'name': self.name}
            self.__info_send_to_server(info)  # 发送给服务端
            flag = self.sock.recv(1024).decode()  # 接收服务端返回的标志位
        else:
            print('命令错误,提示: put | filename')
            return
        # 看服务器返回的标志位
        if flag == 'NO EXIST':  # 待上传的文件在服务器上没有
            self.__file_send_to_server(parameter, file_size)
            end_flag = self.sock.recv(1024).decode()  # 接收服务端返回的标志位
            if end_flag == 'OK':
                print('\n文件上传完成,md5校验通过')
            else:
                print('\n文件上传有问题了')
        elif flag == 'NO':  # 已经上传过了，不需要在上传了
            print('文件在服务器中已经存在了,不需要在上传了')

        elif flag == 'NO QUOTA':
            print('磁盘配额不够,请联系管理员帮忙修改配额')

        else:  # 待上传文件在服务器存在，断点续传
            print('该文件之前已经传输过一部分了，启用断点续传')
            # pointer=int(flag)  直接接收服务器返回已存在的文件的大小
            self.__file_send_to_server(parameter, file_size, pointer=int(flag))
            end_flag = self.sock.recv(1024).decode()  # 接收服务端返回的标志位
            if end_flag == 'OK':
                print('\n断点续传完成,md5校验通过')
            else:
                print('断点续传完成有问题了')

    def get(self):  # 下载
        pass

    def ls(self):  # 显示
        pass

    def mk(self):  # 新建
        pass

    def rm(self):  # 删除
        pass

    def cd(self):  # 切换目录
        pass

    def logout(self):  # 退出
        quit()
