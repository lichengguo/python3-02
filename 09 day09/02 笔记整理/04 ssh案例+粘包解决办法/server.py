#!/usr/bin/env python3
# author:Alnk(李成果)
import socket
import struct
import subprocess

sock = socket.socket()
sock.bind(('127.0.0.1', 8800))
sock.listen(5)

while 1:
    print('等待...')
    conn, addr = sock.accept()
    while 1:
        try:
            cmd = conn.recv(1024)
        except Exception as e:
            break
        if len(cmd) == 0:
            break
        print('客户端的命令:', cmd.decode())
        if cmd.decode() == 'quit':
            conn.close()
            break
        # 执行客户端传过来的命令
        res = subprocess.Popen(cmd.decode(),
                         shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         )
        cmd_data = res.stdout.read()
        print("命令返回结果:", cmd_data.decode('gbk'))
        print('命令返回字节长度:', len(cmd_data))
        # 解决粘包问题:根据网络传输的报头报文思路
        pack_length = struct.pack('i', len(cmd_data))  # 打包
        final_data = pack_length + cmd_data  # 拼接命令返回的数据
        conn.send(final_data)
