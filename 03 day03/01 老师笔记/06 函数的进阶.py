"""
本文件主要是研究函数的进阶
"""


# name = 'barry'
# age = 18
#
# def func():
#     sex = '男'
#
# func()
# python的空间三种：
    # 全局名称空间
    # 局部名称空间
    # 内置名称空间
# print()
# len()

# def func():
#     name = 'alex'
# func()
# print(name)
# func()
# python中的作用域：
    # 全局作用域：内置名称空间 全局名称空间
    # 局部作用域：局部名称空间

# 取值顺序: 就近原则
    # 局部名称空间 ——————> 全局名称空间 ——————> 内置名称空间
# input = 'barry'
# def func():
#     # input = 'alex'
#     print(input)
# func()
# print(input)

# 加载顺序
#     内置名称空间  ------->  全局名称空间 ------->  局部名称空间


#
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
# 444 333 555
# 444 333 222 111 555

# def wraaper():
#     print(222)
#     def inner():
#         print(111)
#     print(444)
#     inner()
#     print(333)
#
# wraaper()
# 222 444 111 333


# globals() locals()

# name = 'alex'
# age = 46

# def func():
#     sex = '男'
#     hobby = '女'
#     print(globals())  # 返回一个字典：全局作用域的所有内容
#     print(locals())  # 当前位置的内容
# func()

# print(globals())  # 返回一个字典：全局作用域的所有内容
# print(locals())  # 当前位置的内容

# 函数名的运用
# def func():
#     print(666)

# 1,函数名是一个特殊的变量 函数名() 执行此函数
# func()


# 2,函数名可以当做变量进行赋值运算。
# def func():
#     print(666)
# age1 = 12
# age2 = age1
# age3 = age2
# print(age3)
# f = func
# f()
# 下面不能执行
# age1 = 33
# age1()
# print(globals())

# 3，函数名可以作为容器型数据的元素。
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
# a = 1
# b = 2
# c = 3
# d = 4
# l1 = [a, b, c, d]
# l1 = [func, func1, func2, func3]
# # for i in l1:
# #     i()
#
# dic = {
#     1: func,
#     2: func1,
#     3: func2,
#     4: func3,
# }
# # dic[1]()
# # dic[2]()
# # dic[3]()

# # while 1:
# #     num = input('请输入序号：').strip()
# #     if num == '1':
# #         func()
# #     elif num == '2':
# while 1:
#     num = input('请输入序号：').strip()
#     num = int(num)
#     dic[num]()
#
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

# 函数名的应用：问题

# def func():
#     print(1111)
# func()
# f = func
# func = 1
# print(func)
# print(f)

# age1 = 12
# age2 = age1
# age3 = age2
# age2 = 46
# print(age1,age2,age3)  # 12 46 12
#
# age1 = [1,2,3]
# age2 = age1
# age1.append(666)
# print(age1,age2)



# global nonlocal

# global
#1，声明一个全局变量。
# def f():
#     print(name)
#
# def func():
#     global name
#     name = 'alex'
# func()
# f()
# print(name)
# print(globals())
# 2,修改一个全局变量。

# 原因：局部作用域只能引用全局变量而不能改变全局变量。
# count = 1
# def func1():
#     global count
#     count += 1
# print(count)
# func1()
# print(count)

# nonlocal： 子级函数可以通过nonlocal修改父级（更高级非全局变量）函数的变量。

# 现象：子级函数可以引用父级函数的变量但是不能修改。
# def func():
#     count = 1
#     def func1():
#         def inner():
#             nonlocal count
#             count += 1
#             print(count)  # 2
#         print(count)  # 1
#         inner()
#         print(count)  # 2
#     func1()
# func()

# count = 1
# def func1():
#     def inner():
#         nonlocal count
#         count += 1
#         print(count)
#     inner()
#
# func1()


