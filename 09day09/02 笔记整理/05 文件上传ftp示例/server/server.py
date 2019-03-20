#!/usr/bin/env python3
# author:Alnk(李成果)
import socket
import struct
import json


class FTPServer(object):
    def __init__(self):
        self.ip = '127.0.0.1'
        self.server_port = 8800
        self.run()

    def get_socket(self):
        sock = socket.socket()
        sock.bind((self.ip, self.server_port))
        sock.listen(5)
        return sock

    def run(self):
        self.sock = self.get_socket()
        print('server is waiting...')
        self.conn, self.addr = self.sock.accept()

        while 1:
            length_park = self.conn.recv(4)  # 获取4个字节，即信息字典的字节长度
            length = struct.unpack('i', length_park)[0]
            info_bites = self.conn.recv(length)  # 接收信息字典
            info = json.loads(info_bites)
            print('客户端传递的信息字典:', info)
            cmd = info.get('action')
            if hasattr(self, cmd):
                getattr(self, cmd)(info)
            else:
                print('客户端传递过来的信息字典有问题')

    def put(self, info):
        '''
        接收客户端的上传请求
        :return:
        '''
        filename = info.get('filename')
        filesize = info.get('filesize')
        # 循环接收客户端传递的文件
        with open(filename, 'wb') as f:
            recv_data_len = 0
            while 1:
                line = self.conn.recv(1024)
                f.write(line)
                recv_data_len += len(line)

    def download(self, info):
        '''
        处理用户下载请求
        :return:
        '''
        pass


if __name__ == '__main__':
    fs = FTPServer()
