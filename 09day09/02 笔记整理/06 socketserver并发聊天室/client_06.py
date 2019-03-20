#!/usr/bin/env python3
# author:Alnk(李成果)
import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 8899))

while 1:
    data = input('发给服务端的请求>>>')
    if len(data) == 0:
        continue
    if data == 'quit':
        break
    sock.send(data.encode())
    res = sock.recv(1024)
    print('服务器的回复:', res.decode())

print('聊天结束')
sock.close()
