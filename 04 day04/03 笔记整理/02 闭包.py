#!/usr/bin/env python3
#author:Alnk(李成果)
"""
# 什么是闭包：
    # 1，闭包存在于函数中。
    # 2，闭包就是内层函数对外层函数（非全局变量）的引用。
    # 3，最内层函数名会被逐层的返回，直至返回给最外层。
"""
# 不是闭包,name 是全局变量
# name = 1
# def func():
#     print(name)

# 这才是闭包
# def func():
#     name = 'alex'
#     def inner():
#         print(name)
#     return inner
# ret = func()
# print(ret.__closure__)  #如果返回cell，就证明是一个闭包。返回None 就不是闭包
# print(ret.__closure__[0].cell_contents)

# 这也是闭包
# def func(name):
#     # name = 'barry'    #name参数 相当于这行代码
#     def inner():
#         print(name)
#     return inner
# n1 = 'barry'
# ret = func(n1)
# print(ret.__closure__)


#闭包的作用
# 解释器遇到闭包，会触发一个机制，这个闭包不会随着函数的结束而释放

# 不是闭包的情况，函数里面定义的变量会随着函数的结束而释放
# def func(step):
#     num = 1
#     num += step
#     print(num)
# for i in range(5):
#     func(2)
# # 3 3 3 3 3


# 闭包情况下：不会随着函数的结束而释放
# def func(step):
#     num = 1
#     def inner():
#         nonlocal num
#         num += step
#         print(num)
#     return inner
# f = func(2)
# for i in range(5):
#     f()
# # 3 5 7 9 11


# 闭包举例 爬虫
# from urllib.request import urlopen
# def but():
#     context = urlopen("http://www.cnblogs.com/jin-xin/articles/8259929.html").read()
#     def get_content():
#         return context
#     return get_content
# fn = but()
# content = fn()      #获取内容
# print(content.decode('utf-8'))      #中文显示
# content2 = fn()
# print(content2.decode('utf-8'))