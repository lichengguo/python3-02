import socket
import json
import struct

class FTPClient(object):
    def __init__(self):
        self.ip="127.0.0.1"
        self.server_port=8800
        self.run()

    def get_socket(self):
        # 1  创建一个套接字对象(socket)  AF_INET: ipv4协议   SOCK_STREAM： TCP协议
        sock = socket.socket()
        return sock

    def run(self):
        self.sock = self.get_socket()
        self.sock.connect((self.ip,self.server_port))
        print('''
            1 : 登陆
            2 ：上传文件
            3 ：下载文件
            4 ： 远程控制 
        ''')
        while 1:
           choose = input("请输入命令>>>")
           action_dict = {"2": "put", "3": "download"}
           if hasattr(self, action_dict[choose]):
               getattr(self, action_dict[choose])()
           else:
               pass
    def put(self):
        '''
        上传文件
        :return:
        '''
        print("欢迎上传文件！")
        cmd=input(">>>")
        action,params=cmd.split(" ")
        if action=="put":
            # 上传的基本信息
            filesize=0
            with open(params, "rb") as f:
                for line in f:
                    filesize+=len(line)
            info={"action":"put","filename":params,"filesize":filesize}
            #打包格式： xxx xxx xxx xxx{"action":"put","filename":params,"filesize":filesize}
            info_bites=(json.dumps(info)).encode()
            length_pack=struct.pack("i",len(info_bites))
            new_info=length_pack+info_bites
            self.sock.send(new_info)
            # 上传数据
            with open(params,"rb") as f:
                for line in f:
                    self.sock.send(line)
            print("上传完毕")
        else:
            pass
    def download(self):
        '''
        下载文件
        :return:
        '''
        pass


FTPClient()