#!/usr/bin/env python3
#author:Alnk(李成果)
import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 8899))
sock.listen(5)

while 1:
    conn, _ = sock.accept()
    data = conn.recv(1024)
    print('客户端发送：',data)
    with open(r"02.2 jd.html", 'rb') as f:
        content = f.read()
    # print('服务端返回：',content)
    conn.send(b'HTTP/1.1 200 0K \r\n\r\n' + content)
    # conn.send(b'HTTP/1.1 201 0K\r\n\r\n <h1> welcome to </h1> ')
    # conn.send(b'<img src="http://img1.imgtn.bdimg.com/it/u=2735633715,2749454924&fm=26&gp=0.jpg" />')
    conn.close()
