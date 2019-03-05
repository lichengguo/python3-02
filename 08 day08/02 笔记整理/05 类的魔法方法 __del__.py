#!/usr/bin/env python3
#author:Alnk(李成果)

# 析构方法：__del__
# 在程序结束，或者类在内存中被删除的时候，就会执行 __del__ 方法
# python 垃圾回收机制：任何对象在执行过程中失去了指引，则被回收

import time

class Animal(object):

    def  __init__(self, name, age):
        self.name = name
        self.age = age

    def foo(self):
        print('foo...')

    def __del__(self):
        print('i am 析构')


# 会等待5s，程序结束，然后执行 __del__ 析构方法
# alex = Animal('alex', 34)
# time.sleep(5)

# 会先执行 __del__ 析构方法，然后等待5s 程序结束
alex = Animal('alex', 34)
del alex
time.sleep(5)


# 应用场景
# 例如：关闭数据库连接，关闭文件连接等
