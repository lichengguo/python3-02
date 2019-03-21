#!/usr/bin/env python3
# author:Alnk(李成果)
import socket
import struct

sock = socket.socket()
sock.connect(('127.0.0.1', 8800))

while 1:
    cmd = input('请输入命令>>>')
    if len(cmd) == 0:
        break
    if cmd == 'quit':
        break
    sock.send(cmd.encode())
    temp_data_len = sock.recv(4)  # 接收服务器数据传过来的数据总长度大小
    data_len = struct.unpack('i', temp_data_len)[0]
    print('数据字节总长度:', data_len)
    # 循环接收所有的数据
    recv_data_length = 0  # 已经接收的字节长度
    recv_data = b''  # 已经接收的字节
    while recv_data_length < data_len:
        temp_data = sock.recv(1024)
        recv_data += temp_data  # 拼接字节
        recv_data_length += len(temp_data)  # 加字节长度
    print("服务器命令返回值:", recv_data.decode('gbk'))
