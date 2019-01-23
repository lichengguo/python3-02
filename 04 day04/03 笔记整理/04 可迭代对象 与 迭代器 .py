#!/usr/bin/env python3
#author:Alnk(李成果)

# 可迭代对象：这个对象由多个元素组成，他就是可迭代的
# 这个对象内部只要含有"__iter__"方法,他就是可迭代的
#
# for i in 'abc':
#     print(i)
#
# for i in [1,2,3]:
#     print(i)
#
# for i in 1234:    # 数字是一个不可迭代对象
#     print(i)
#
# int bool                  ---- 不可迭代
# str list tuple dict set bytes range 文件句柄      --可以迭代
#
# 判断一个对象是否是可迭代的
# 方法一：内部是否有 "__iter__方法"
# s1 = "alex"
# print("__iter__" in dir(s1))
#
# n = 1
# print("__iter__" in dir(n))
#
#print("__iter__" in dir(range))
#
# f = open('a.txt',encoding='utf-8',mode='w')
# print("__iter__" in dir(f))
#
#方法二：
# from collections import Iterable        #判断一个对象是不是可迭代对象
# l1 = [1,2,3]
# print(isinstance(l1,Iterable))


# 迭代器：内部含有__iter__方法并且含有__next__方法的就是迭代器
# 如何判断此对象是不是迭代器？
# 方法1
# l1 = [1,2,3]    # 不是迭代器
# print('__iter__' in dir(l1))
# print('__next__' in dir(l1))
#
#方法2
# from collections import  Iterator
# f = open('a.txt',encoding='utf-8',mode='w')     # 文件句柄是一个迭代器
# print(isinstance(f,Iterator))


#迭代器和可迭代对象的区别
#
# 1、可迭代对象不能直接取值，必须转化成迭代器进行取值。把索引这个方法除外哈
# l1 = [1,2,3]
# for i in l1:      #for循环内部会把可迭代对象转化为迭代器，用__next__ 进行取值
#     print(i)
#
# 将一个可迭代对象转化为迭代器 iter()
# l1 = [1,2,3]
# obj = iter(l1)
# print(obj)
# print(next(obj))
# print(next(obj))
# print(next(obj))


# 迭代器有什么作用？
# 1，节省内存。
# 2，一条路走到底，不反复。
# 3，不易看出。
#
# while 模拟for循环循环可迭代对象的机制。
# 1,将可迭代对象转化成迭代器。
# 2，利用next进行取值。
# 3，利用异常处理停止循环。
# l1 = [1,2,3,4,5,6,]
# # obj = l1.__iter__()  # 不建议用这种方法把可迭代对象转化为迭代器
# obj = iter(l1)
# while 1:
#     # print(obj.__next__())   # 不建议用这种方法去取值
#     try:
#         print(next(obj))
#     except StopIteration:
#         break