#!/usr/bin/env python3
#author:Alnk(李成果)
# 函数名的应用
# 1,函数名是一个特殊的变量 函数名() 执行此函数
# def func():
#     print(666)
# func()

# 2,函数名可以当做变量进行赋值运算。
# def func():
#     print(666)
#
# f = func
# f()

# 3，函数名可以作为容器型数据的元素 ***
# def func():
#     print(666)
#
# def func1():
#     print(777)
#
# def func2():
#     print(888)
#
# def func3():
#     print(999)
#
# l1 = [func, func1, func2, func3]
# for i in l1:
#     i()
#
# dic = {
#     1: func,
#     2: func1,
#     3: func2,
#     4: func3,
# }
#
# while 1:
#     num = input('请输入序号：').strip()
#     num = int(num)
#     dic[num]()

# 4，函数名可以作为函数的参数。
# def func1():
#     print(111)
#
# def func2(x):
#     x()
#     print(222)
#
# func2(func1)

# 5，函数名可以作为函数的返回值。
# def func1():
#     print(111)
#
# def func2(x):
#     print(222)
#     return x
#
# ret = func2(func1)
# ret()