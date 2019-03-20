
import socket

# 1 创建套接字对象
sock=socket.socket()

# 2 连接服务器
sock.connect(("127.0.0.1",8899))

while 1:
    data = input(">>>")
    sock.send(data.encode())
    if data=="quit":
        break
    print("等待回复...")
    res = sock.recv(1024)
    print("服务器响应:", res.decode())

print("聊天结束！")