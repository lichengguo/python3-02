#!/usr/bin/env python3
# author:Alnk(李成果)
import socket

# 1 创建套接字对象
sock = socket.socket()

# 2 连接服务端
sock.connect(('127.0.0.1', 8899))

while 1:
    data = input('>>>')
    if len(data) == 0:  # 防止客户端输入空值，卡死程序
        continue
    if data == 'quit':  # quit退出聊天
        break
    sock.send(data.encode())
    print('等待回复')
    res = sock.recv(1024)
    print('服务器响应：', res.decode())

print('聊天结束')
sock.close()