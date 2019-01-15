#!/usr/bin/env python3
#author:Alnk(李成果)
# global nonlocal
#
# global
#1，声明一个全局变量。
# def func():
#     global name
#     name = 'alex'
# func()
# print(name)

# 2,修改一个全局变量。
# 原因：局部作用域只能引用全局变量而不能改变全局变量。如果改变则报错
# global 可以实现通过局部作用域而去改变全局变量
# count = 1
# def func1():
#     global count
#     count += 1
# print(count)
# func1()
# print(count)


# nonlocal： 子级函数可以通过nonlocal修改父级（更高级非全局变量）函数的变量。
# 现象：子级函数可以引用父级函数的变量但是不能修改。
def func():
    count = 1
    def func1():
        def inner():
            nonlocal count
            count += 1
            print(count)  # 2
        print(count)      # 1
        inner()
        print(count)      # 2
    func1()
func()

# 这个不行，会报错
# count = 1
# def func1():
#     def inner():
#         nonlocal count
#         count += 1
#         print(count)
#     inner()
#
# func1()