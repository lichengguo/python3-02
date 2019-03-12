#!/usr/bin/env python3
# author:Alnk(李成果)
import socket

# 1 创建套接字对象
sock = socket.socket()

# 2 连接服务端
sock.connect(('127.0.0.1', 8899))

# 3 给服务端发送消息
sock.send(b'hello')

# 4 接受服务端的消息
data = sock.recv(1024)
print('data:', data)
print('data:', data.decode())

# 5 关闭链接
sock.close()
