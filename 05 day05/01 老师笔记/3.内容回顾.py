# -*- coding: utf-8 -*-
# @Time    : 2019/1/27 9:42
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 3.内容回顾.py
# @Software: PyCharm

# 函数进阶
# 装饰器
    # 在不改变函数原本调用方式的基础上添加一些功能
    # @装饰器名
    # 如何写一个装饰器
    # 计算函数执行时间
    # 用户认证
    # 给函数添加日志
# def wrapper(func):
#     def inner(*args,**kwargs):
#         '''在被装饰的函数之前添加功能'''
#         ret = func(*args,**kwargs)
#         '''在被装饰的函数之后添加功能'''
#         return ret
#     return inner
#
# @wrapper    # func = wrapper(func)
# def func():
#     pass
# def wrapper2(func):
#     def inner(*args,**kwargs):
#         print('wrapper2 before')
#         ret = func(*args,**kwargs)
#         print('wrapper2 after')
#         return ret
#     return inner
#
# def wrapper1(func):
#     def inner(*args,**kwargs):
#         print('wrapper1 before')
#         ret = func(*args,**kwargs)
#         print('wrapper1 after')
#         return ret
#     return inner
#
# @wrapper2
# @wrapper1    # func = wrapper(func)
# def func():
#     print('in func')
# func()

# 登陆 -- 装饰器 auth
# 计算函数的执行时间 -- 装饰器 timmer
# @auth
# @timmer
# def func():
#     pass

# flag = False
# def outer(flag):
#     def timmer(func):
#         def inner(*args,**kwargs):
#             if flag:
#                 print('wrapper1 before')
#                 ret = func(*args,**kwargs)
#                 print('wrapper1 after')
#             else:
#                 ret = func(*args, **kwargs)
#             return ret
#         return inner
#     return timmer
#
# @outer(flag)   #outer(flag) =  timmer    @outer(flag) =  @timmer
# def func():
#     print('in func')
#
# func()


# 迭代器和生成器
# 可迭代对象
# 可迭代对象可以通过for/iter方法将一个可迭代对象转换成一个迭代器  ，list str range
# 迭代器
# 使用迭代器 ： 节省内存，迭代器一项一项的取，节省内存 文件句柄
# 生成器
    # 我们自己写的迭代器
    # 生成器的本质就是迭代器，所有的生成器都是迭代器
# 实现生成器的方法 ：
    # 生成器函数 ：一定带yield关键字
    # g = func()
    # 生成器表达式 : 用小括号表示的推导式
# 生成器的特点：
    # 1.可以用next/send方法从中取值
    # 2.生成器中的数据只能从头到尾取一次
    # 3.惰性运算 ：不取生成器是不工作的

# def demo():
#     for i in range(4):
#         yield i
# g=demo()
#
# g2=(i for i in g)
# g1=(i for i in g)
#
# print(list(g1))  # 0，1，2，3   # 这一步才开始从g1中取值
# print(list(g2))  #

# 列表推导式(排序)
    # [i**2 for i in lst]
    # [i**2 for i in lst if i%2 ==0 ]
# 生成器表达式
    # (i**2 for i in lst)

# 匿名函数
    # lambda 参数1,参数2,参数3 : 返回值/返回值相关的表达式

# 内置函数
    # min max map filter sorted   单记
    # reduce --> functool
    # zip sum enumerate
















