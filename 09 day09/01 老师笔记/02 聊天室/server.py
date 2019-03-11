
import socket
from socket import AF_INET,SOCK_STREAM

# 1  创建一个套接字对象(socket)  AF_INET: ipv4协议   SOCK_STREAM： TCP协议
sock=socket.socket(family=AF_INET, type=SOCK_STREAM)
# 2 绑定IP与端口
sock.bind(("127.0.0.1",8800))
# 3 创建监听数
sock.listen(5)

# 4 等待连接,一旦客户请求到来，返回两个值：客户端的套接字对象，客户端的地址
while 1:
    print("waiting a connect.....")
    conn, addr = sock.accept()
    while 1:
        try:
            data = conn.recv(1024)
        # 针对window
        except Exception as e:
            break
        # 针对linux
        if len(data) == 0:
            break
        print("客户：", data.decode())
        if data.decode() == "quit":
            conn.close()
            break
        res = input("响应 >>>")
        conn.send(res.encode())






