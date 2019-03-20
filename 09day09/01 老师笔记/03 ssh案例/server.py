
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
            cmd = conn.recv(1024)
        # 针对window
        except Exception as e:
            break
        # 针对linux
        if len(cmd) == 0:
            break
        print("客户端命令：", cmd.decode())
        if cmd.decode() == "quit":
            conn.close()
            break
        # 执行远程命令,得到结果返回
        import subprocess
        res=subprocess.Popen(cmd.decode(),shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
        data=res.stdout.read()
        print("data",data.decode("gbk"))
        print("length",len(data))
        # conn.send((str(len(data))).encode())
        # conn.recv(1024)
        # conn.send(data)
        # 解决粘包的最终方案：报头报文的设计思路

        #  获取长度的打包结果
        import  struct
        pack_length=struct.pack("i",len(data))
        final_data=pack_length+data
        conn.send(final_data)











