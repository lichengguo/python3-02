import socket
import struct
import json

class FTPServer(object):
    def __init__(self):
        self.run()

    def get_socket(self):
        # 1  创建一个套接字对象(socket)  AF_INET: ipv4协议   SOCK_STREAM： TCP协议
        sock = socket.socket()
        # 2 绑定IP与端口
        sock.bind(("127.0.0.1", 8800))
        # 3 创建监听数
        sock.listen(5)
        return sock

    def run(self):
        self.sock=self.get_socket()
        print("server is waiting....")
        self.conn,self.addr=self.sock.accept()
        while 1:
            length_pack=self.conn.recv(4)
            length=struct.unpack("i",length_pack)[0]
            info_bites=self.conn.recv(length)
            info=json.loads(info_bites)
            print("info",info)
            cmd=info.get("action")
            if hasattr(self,cmd):
                getattr(self,cmd)(info)
            else:
                pass

    def put(self,info):
        '''
        上传文件
        :return:
        '''
        filename = info.get("filename")
        filesize = info.get("filesize")
        # 循环接受文件
        with open(filename,"wb") as f:
            recv_data_len=0
            while recv_data_len<int(filesize):
                line=self.conn.recv(1024)
                f.write(line)
                recv_data_len+=len(line)
        print("上传完毕")


    def download(self,info):
        '''
        下载文件
        :return:
        '''
        pass





FTPServer()