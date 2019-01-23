# -*- coding: utf-8 -*-
# @Time    : 2019/1/19 15:23
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 05 可迭代对象 与 迭代器 .py
# @Software: PyCharm
# for i in 'abc':
#     print(i)
#
# for i in [1,2,3]:
#     print(i)

# for i in 1234:
#     print(i)


# 可迭代对象：这个对象由多个元素组成，他就是可迭代的。
# 这个对象内部只要含有"__iter__"方法,他就是可迭代的。
# 遵循可迭代协议。
# s1 = 'alex'
# print(dir(s1))
# i = 100
# print(dir(i))

# int str bool list tuple dict set bytes range 文件句柄
# int bool
# str list tuple dict set bytes range 文件句柄
# 判断一个对象是否是可迭代的 方法一：
# print('__iter__' in dir(range))

# 迭代器：内部含有__iter__方法并且含有__next__方法的就是迭代器。
# 如何判断此对象是不是迭代器？
# l1 = [1,2,3]
# print('__iter__' in dir(l1))
# print('__next__' in dir(l1))


# 判断一个对象是否是迭代器，可迭代对象的另一种方式:
# from collections import Iterator
# from collections import Iterable
# l1 = [1,2,3,4]
# print(isinstance(l1,Iterator))
# print(isinstance(l1,Iterable))
# 文件句柄？
# with open('01 今日内容大纲',encoding='utf-8') as f1:
#     print(isinstance(f1,Iterator))
# 可迭代对象不能直接取值，必须转化成迭代器进行取值。
# l1 = [1,2,3]
# for i in l1:
#     print(i)
#
# 将一个可迭代对象 转化成迭代器
l1 = [1, 2, 3]
obj1 = iter(l1)
print(obj1)
# 一个next对应一个值
print(next(obj1))
print(next(obj1))
print(next(obj1))
# print(next(obj1))

# 迭代器有什么作用？
# 1，节省内存。
# 2，一条路走到底，不反复。
# 3，不易看出。

# while 模拟for循环循环可迭代对象的机制。
# 1,将可迭代对象转化成迭代器。
# 2，利用next进行取值。
# 3，利用异常处理停止循环。
l1 = [1, 2, 2, 3, 4, 4, 5, 5]
# obj = l1.__iter__()
obj = iter(l1)
while 1:
    try:
        print(next(obj))
    except StopIteration:
        break
