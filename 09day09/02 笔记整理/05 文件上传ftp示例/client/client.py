#!/usr/bin/env python3
# author:Alnk(李成果)
import socket
import json
import struct


class FTPClient(object):
    def __init__(self):
        self.ip = '127.0.0.1'
        self.server_port = 8800
        self.run()

    def get_socket(self):
        sock = socket.socket()
        return sock

    def run(self):
        self.sock = self.get_socket()
        self.sock.connect((self.ip, self.server_port))

        msg = '''
            1 : 上传
            2 : 下载
        '''
        action_dict = {'1': 'put', '2': 'download'}
        while 1:
            print(msg)
            choose = input('请输入命令>>>')
            if hasattr(self, action_dict[choose]):
                getattr(self, action_dict[choose])()
            else:
                print('输入有误，重新输入')

    def put(self):
        '''
        上传文件
        :return:
        '''
        print('欢迎上传文件')
        cmd = input('输入命令>>>')
        action, params = cmd.split(' ')

        if action == 'put':
            # 上传的基本信息
            filesize = 0  # 字节长度
            with open(params, 'rb') as f:
                for line in f:
                    filesize += len(line)
            # 基本信息字典
            info = {'action': action, 'filename': params, 'filesize': filesize}
            # 打包格式
            info_bites = json.dumps(info).encode()
            info_bites_length = len(info_bites)  # 基本信息字典 字节长度
            length_pack = struct.pack('i', info_bites_length)
            # 拼接信息字典字节长度+基本信息字典
            new_data = length_pack + info_bites
            self.sock.send(new_data)
            # 开始上传数据
            with open(params, 'rb') as f:
                for line in f:
                    self.sock.send(line)
            print('上传完成')
        else:
            print('命令错误！')

    def download(self):
        '''
        下载文件
        :return:
        '''
        pass


if __name__ == '__main__':
    fc = FTPClient()
