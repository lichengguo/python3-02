#!/usr/bin/env python3
#author:Alnk(李成果)
# 函数的嵌套
# 举例1
# def func():
#     print(111)
#
# def func1():
#     print(222)
#     func()
#
# def func3():
#     print(333)
#     func1()
#
# print(444)
# func()
# print(555)
# 444 111 555
#
#举例2
# def func():
#     print(111)
#
# def func1():
#     print(222)
#     func()
#
# def func3():
#     print(333)
#     func1()
#
# print(444)
# func3()
# print(555)
# 444 333 222 111 555
#
# def wrapper():
#     print(222)
#     def inner():
#         print(111)
#     print(444)
#     inner()
#     print(333)
#
# wrapper()
# 222 444 111 333