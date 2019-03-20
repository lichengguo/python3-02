#!/usr/bin/env python3
# author:Alnk(李成果)
import socket
from socket import AF_INET, SOCK_STREAM

# 1 创建套接字对象  family=AF_INET, type=SOCK_STREAM
# AF_INET:表示ipv4,  AF_INET6:表示ipv6
# SOCK_STREAM:表示tcp协议,  SOCK_DGRAM:表示udp协议
sock = socket.socket(family=AF_INET, type=SOCK_STREAM)  # 看源码，括号里参数也可以不写

# 2 绑定IP和端口
sock.bind(("127.0.0.1", 8899))

# 3 创建一个监听数
# 表示可以等待5个请求连接，如果算上已经连接的请求，那么第7个才会报错
# 排队5个，连接1个，所以第7个才会报错
sock.listen(5)

# 4 等待连接，一旦客户端请求过来，会返回两个值：客户端的套接字对象，客户端的地址
print('等待连接...')
conn, addr = sock.accept()  # 阻塞状态，不占CPU资源
print('conn', conn)
print('addr', addr)

# 5 接受客户端信息
data = conn.recv(1024)
print(data.decode())

# 6 给客户端返回一个welcome字符串
conn.send('welcom! 苑!'.encode())

# 7 关闭与客户端连接
conn.close()
# 关闭服务器的socket
sock.close()
