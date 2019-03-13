#!/usr/bin/env python3
# author:Alnk(李成果)
import socket
from core.basic import Basic


class FTPClient(Basic):  # ftp客户端
    def __init__(self, ip, port, name, pwd):
        self.ip = ip
        self.port = port
        self.name = name
        self.pwd = pwd
        self.sock = self.connect()

    def connect(self):  # 连接服务器
        sock = socket.socket()
        sock.connect((self.ip, self.port))
        return sock

    def run(self):
        msg = ''' 
        ------ 欢迎使用ftp客户端 ------
        1 上传文件
        2 下载文件
        3 执行文件操作命令 
        4 帮助
        5 退出
        '''
        msg_dict = {'1': 'put', '2': 'download', '3': 'cmd', '5': 'logout', '4': 'manual'}
        flag = self.login()
        if flag == 'OK':
            while 1:
                print('\n %s' % msg)
                choose = input('输入编号>>>')
                if not msg_dict.get(choose):  # 规范用户输入动作
                    print('编号有误重新输入')
                    continue
                if hasattr(self, msg_dict[choose]):  # 反射
                    getattr(self, msg_dict[choose])()
                else:
                    print('类定义的方法有问题')
        else:
            print('客户端：账号或者密码错误')

    def login(self):  # 登录
        pwd_md5 = self.get_md5(self.pwd.encode())  # 密码md5
        info_dict = {'action': 'login', 'name': self.name, 'pwd': pwd_md5, }  # 发送给
        last_info = self.send_dict_info(info_dict)  # 获取打包好的数据
        self.sock.send(last_info)  # 发送给服务器
        flag = self.sock.recv(1024).decode()  # 接收服务器返回的标志位，1 登录成功，0 登录失败
        return flag

    def put(self):  # 上传文件
        user_cmd = input('请输入命令>>>')
        action, parameter = user_cmd.split(' ')
        if action == 'put':
            with open(parameter, 'rb') as f:  # 读取文件大小
                filesize = 0
                for line in f:
                    filesize += len(line)
                    file_md5 = self.get_md5(line)  # md5
            info_dict = {'action': action, 'parameter': parameter, 'filesize': filesize, 'md5': file_md5, 'name': self.name}  # 发送给服务端的信息
            last_info = self.send_dict_info(info_dict)  # 获取打包好的数据
            self.sock.send(last_info)  # 发送给服务端

            # 等服务器返回标志位，看之前是否已经有传过相同的文件
            recv_file_size = 0
            flag_file = self.sock.recv(1024).decode()
            if flag_file == 'NO':  # 之前没传过同名文件
                pass
            else:
                print('cccccccccccc',flag_file)
                recv_file_size = int(flag_file)
                print(recv_file_size)

            flag_quota = self.sock.recv(1024).decode()  # 接收服务器返回的磁盘空间是否足够的标志位
            if flag_quota == 'NO':  # 用户空间配额不足直接返回
                print('该用户磁盘配额不足啦')
                return False

            with open(parameter, 'rb') as f:  # 发送需要传送的文件给服务端
                # 调整文件指针位置
                f.seek(recv_file_size)
                already_size = 0
                for line in f:
                    self.sock.send(line)
                    already_size += len(line)
                    self.view_bar(filesize,already_size)  # 进度条
            flag = self.sock.recv(1024).decode()  # 接收服务器传输完成并且md5校验以后的标志位
            if flag == 'OK':
                print('\n文件[%s]传输完成了！' % info_dict['parameter'])
            else:
                print('文件传输过程中丢包了，请重新再传')
        else:
            print('输入命令类似 put /path/filename')

    def download(self):  # 下载文件
        print('下载文件')

    def cmd(self):  # 执行命令
        print('执行命令')

    def logout(self):  # 退出
        quit()

    def manual(self):  # 手册
        msg = ''' 
        ----------- 欢迎使用帮助手册 ----------------
        1 上传文件示例： put /path/filename
        2 下载文件示例： get /path/filename
        3 执行命令示例：
            查看目录： ls /pathname
            切换目录： cd /pathname
            删除文件： rm /pathname/filename
            新建文件： mkdir /pathname/name
            退出：     quit
        '''
        print(msg)
