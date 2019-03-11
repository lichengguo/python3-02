
import socket

# 1 创建套接字对象
sock=socket.socket()

# 2 连接服务器
sock.connect(("127.0.0.1",8800))
sock.send(b"hello")
data=sock.recv(1024)
print("data字节串",data)
print("data字符串",data.decode())

sock.close()