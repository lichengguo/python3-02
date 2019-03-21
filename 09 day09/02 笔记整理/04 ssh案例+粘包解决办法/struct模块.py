#!/usr/bin/env python3
# author:Alnk(李成果)
import struct  # 打包

# http://www.cnblogs.com/Eva-J/articles/8244551.html

# 打包
# print(struct.pack('i', 1000))  # int 类型，打包后的大小为4个字节
# print(struct.pack('i', 1))
# print(struct.pack('i', 112))
# print(struct.pack('i', 34))


# 解包
temp = struct.pack('i', 1000)
print('打包字节大小',len(temp))
print(struct.unpack('i', temp))  # 解包出来的数据是一个元组
print(struct.unpack('i', temp)[0])
