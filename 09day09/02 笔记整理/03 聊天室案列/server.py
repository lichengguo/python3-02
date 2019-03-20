#!/usr/bin/env python3
# author:Alnk(李成果)
import socket

sock = socket.socket()
sock.bind(("127.0.0.1", 8899))
sock.listen(5)

while 1:
    print('等待...')
    conn, addr = sock.accept()
    while 1:
        # 针对windows系统客户端直接关闭的情况处理
        try:
            data = conn.recv(1024)
        except Exception as e:
            break
        # 针对linux系统客户端直接关闭的情况处理
        if len(data) == 0:
            break
        print('客户消息：', data.decode())
        if data.decode() == 'quit':  # 客户端传入quit，结束会话
            conn.close()
            break
        res = input('响应客户端请求>>>')
        conn.send(res.encode())
