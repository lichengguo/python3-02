#!/usr/bin/env python3
#author:Alnk(李成果)
# 其他操作方法：
# readable() writable()  ***      文件句柄是否可读，可写
# seek 调整光标位置 按照字节   ***
# seek(0)  将光标移动到开始
# seek(0，2)  将光标移动到最后。
# tell 获取光标位置 按照字节。  ***
# flush 刷新 保存  ***
# truncate 截取原文件，从头开始截，
#
# f = open('log3',encoding='utf-8')
# f.seek(1)
# print(f.read())
# print(f.tell())
# f.seek(0) # 将光标移动到开始
# f.seek(0,2)  # 将光标移动到最后。

# print(f.read())
# print(f.writable())
# if f.writable():
#     f.write('111')
# f.close()

# f = open('log3',encoding='utf-8',mode='w')
# f.write('fjdsklafjdfjksa')
# f.flush()
# f.close()

#截取原文件，从头开始截，需要在可写的模式下，并且不清空原文件
# f = open('log3',encoding='utf-8',mode='r+')
# f.truncate(3)
# f.close()
