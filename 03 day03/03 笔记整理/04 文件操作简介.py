#!/usr/bin/env python3
#author:Alnk(李成果)
"""
文件三参数
    path：文件的路径
    encoding:文件以什么编码方式存储，就以什么编码方式读取
    mode:读，写，，读写，写读，追加，改等等

    三个大方向：
        带b的模式操作对象都是非文字类的文件：视频，音频，图片。

        读（r rb r+ rb+）
            r   读模式
            rb
            r+  读写模式
            rb+

        写 w wb w+ w+b ：如果原文件存在，则清空原文件，在写入。这个慎用
            w   写模式
            wb
            w+  写读模式
            wb+

        追加(a ab a+ a+b)
            a   追加
            ab
            a+
            ab+

    文件操作的其他方法：
        f.read()
        f.write()
        f.readline()
        f.readlines()
        f.close()
        f.seek()
        f.tell()
"""


# f1 = open("文件读写test.txt",encoding='utf-8',mode='r')
# content = f1.read()
# print(content)
# f1.close()
"""
f1变量,文件句柄。
open 内置函数,底层调用的操作系统的操作文件功能的接口。
windows: gbk，linux：utf-8  ios: utf-8
操作文件总共3步；
    1，打开文件，产生文件句柄。
    2，对文件句柄进行操作。
    3，关闭文件句柄。
"""


"""
# 错误示范：
# 1，UnicodeDecodeError: 'gbk' codec can't decode...   编解码错误。
# 2,路径错误。路径分隔符 与后面的字符产生特殊的意义。 解决方式 r 或者 \
    #f1 = open(r"d:\test\r文件读写test.txt",encoding='utf-8',mode='r')
"""



