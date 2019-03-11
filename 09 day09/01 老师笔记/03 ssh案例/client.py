
import socket

# 1 创建套接字对象
sock=socket.socket()
# 2 连接服务器
sock.connect(("127.0.0.1",8800))

while 1:
    data = input("请输入命令>>>")
    sock.send(data.encode())
    if data=="quit":
        break
    print("等待回复...")
    # 第一次先接收数据总长度
    import struct
    data_len = struct.unpack("i",sock.recv(4))[0]
    # sock.send(b"ok")
    print("data_len",data_len)
    # 循环接收响应数据
    recv_data_length=0
    recv_data=b""
    while recv_data_length<data_len:
        temp_data=sock.recv(1024)
        recv_data+=temp_data
        recv_data_length+=len(temp_data)

    print("命令响应:",recv_data.decode("gbk"))


print("聊天结束！")