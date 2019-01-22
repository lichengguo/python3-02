# -*- coding: utf-8 -*-
# @Time    : 2019/1/19 10:07
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 03 闭包.py
# @Software: PyCharm

# 闭包：
# 1，闭包存在于函数中。
# 2，闭包就是内层函数对外层函数（费全局变量）的引用。
# 3，最内存函数名会被逐层的返回直至返回给最外层。
# name = 1
# def func():
#     print(name)

# def func():
#     name = 'alex'
#     def inner():
#         print(name)
#     return inner
#
# ret = func()  # inner
# # ret()
# print(ret.__closure__)  # 只要返回cell 他就是闭包
# print(ret.__closure__[0].cell_contents)  # 只要返回cell 他就是闭包

# name = 'barry'
# def func():
#     def inner():
#         print(name)
#     return inner
#
# ret = func()  # inner
# # ret()
# print(ret.__closure__)  # 只要返回None他就不是闭包
# def func(a,b):
#     a = 2
#     b = 1
#     b = 2
#     a = 1
#     print(a,b)
# func(2,1)

# def func(name):
#     def inner():
#         print(name)
#     return inner
# n1 = 'barry'
# ret = func(n1)  # inner
# print(ret.__closure__)  #

# 闭包的作用是什么？

# def func(step):
#     num = 1
#     num += step
#     print(num)
#
# for i in range(5):
#     func(2)


# 闭包的作用：解释器遇到闭包，会触发一个机制，这个闭包不会随着他的结束而释放。
# def func(step):
#     num = 1
#     def inner():
#         nonlocal num
#         num += step
#         print(num)
#     return inner
#
# f = func(2)
# for i in range(5):
#     f()

from urllib.request import urlopen
def func():
    content = urlopen("http://www.cnblogs.com/jin-xin/articles/8259929.html").read()
    return content

# s1 = func()


# print(content.decode('utf-8'))
# def but(a):
#     content = urlopen(a).read()
#     def get_content():
#         return content
#     return get_content
# fn = but('http://www.cnblogs.com/jin-xin/articles/8259929.html')
# fn = but('http://www.cnblogs.com/jin-xin/articles/8254334.html')
# fn = but('http://www.cnblogs.com/jin-xin/articles/fdsffdsdf.html')
# con = fn()   # 获取内容
# print(con.decode('utf-8'))
# print(con.decode('utf-8'))
# print(con.decode('utf-8'))
# print(con.decode('utf-8'))
# print(content.decode('utf-8'))   #中文显示
# content2 = fn()  # 重新获取内容
# print(content2.decode('utf-8'))

# but()
# but()
