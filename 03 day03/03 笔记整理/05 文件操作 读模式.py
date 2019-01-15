#!/usr/bin/env python3
#author:Alnk(李成果)

# 读模式（r rb r+ rb+）

# r模式
# 默认就是r模式
# 1.1 read()    #全部读取文件内容，如果文件过大，可能会导致内存不足
# f1 = open('文件读写test.txt', encoding='utf-8',mode='r')
# content = f1.read()
# print(content,type(content))  #对文件进行读取出来的都是字符串类型

# 1.2 read(n)
# r模式下,  n代表字符。
# f1 = open('文件读写test.txt', encoding='utf-8',mode='r')
# content = f1.read(3)
# print(content)

# 1.3 readline() 按行读取
# f1 = open('文件读写test.txt', encoding='utf-8',mode='r')
# print(f1.readline().strip())
# print(f1.readline().strip())
# f1.close()

# 1.4 readlines()  返回一个列表,列表里面的元素是原文件每一行
# f1 = open('文件读写test.txt', encoding='utf-8',mode='r')
# content = f1.readlines()
# print(content)
# f1.close()


# 1.5 for循环  **注意平常读取大文件就需要用这种方法
# f1 = open('文件读写test.txt', encoding='utf-8',mode='r')
# for line in f1:
#     print(line.strip())
# f1.close()


# rb模式  ---读取一些非文字类的文件，如图片，视频等
# 也有上面说的那5中读的模式， read()  read(n)  readline()  readlines()  for循环读取
#如果是 rb 模式，就不需要规定编码了 encoding不是编码或解码，它是规定你这个文件到底采用哪种编码模式而已
## f1 = open('文件读写test.txt', encoding='utf-8',mode='rb')
# f1 = open('文件读写test.txt',mode='rb')
# content = f1.read()
# print(content.decode('utf-8'))  #解码 utf-8 ---> unicode
# f1.close()

# rb 模式读取图片
# f1 = open('time1.jpg', mode='rb')
# content = f1.read()
# print(content)
# f1.close()

# r+ 读写模式
# f = open('log1',encoding='utf-8',mode='r+')
# print(f.read())
# f.write('666')
# f.close()

# 先写后读会出问题
# f = open('log1',encoding='utf-8',mode='r+')
# f.write('松岛岛')
# print(f.read())
# f.close()

#rb+ 模式