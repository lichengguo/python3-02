#!/usr/bin/env python3
#author:Alnk(李成果)

# 装饰器
    # 在不改变函数原本调用方式的基础上添加一些功能
    # @装饰器名
    # 如何写一个装饰器
    # 例子
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
# @wrapper
# def f():
#     print('in f')
# f()


# 多个装饰器装饰一个函数
# def wrapper1(func):
#     def inner(*args,**kwargs):
#         print('wrapper1 before')
#         ret = func(*args,**kwargs)
#         print('wrapper1 after')
#         return ret
#     return inner
#
# def wrapper2(func):
#     def inner(*args,**kwargs):
#         print('wrapper2 before')
#         ret = func(*args,**kwargs)
#         print('wrapper2 after')
#         return ret
#     return inner
#
# @wrapper2   #wrapeer2 装饰 wrapper1
# @wrapper1   #wrapper1 装饰 f
# def f():
#     print('in f')
# f()

# 考题
# 两个装饰器装饰一个函数，统计func函数的执行时间
# 登录 -- 装饰器 auth
# 计算函数的执行时间 -- 装饰器 timmer
#
# @auth
# @timmer
# def func()


# 带参数的装饰器
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
# @outer(flag)       # 把这里拆分成@ 和outer(flag)看。先看outer(flag),他就等于timmer 。然后 @outer(flag) = @timmer
# def f1():
#     print('in f1')
#
# @outer(flag)
# def f2():
#     print('in f2')
#
# @outer(flag)
# def f500():
#     print('in f500')
#
# f1()
# f2()
# f500()


# 迭代器和生成器

# 可迭代对象 : list str range
# 可以通过 for/iter 方法将一个可迭代对象转换成一个迭代器  ，

# 迭代器 : 文件句柄
# 使用迭代器 ： 节省内存，迭代器一项一项的取

# 生成器
    # 我们自己写的迭代器
    # 生成器的本质就是迭代器，所有的生成器都是迭代器
# 实现生成器的方法 ：
    # 生成器函数 ：一定带yield关键字 g = func()
    # 生成器表达式 : 用小括号表示的推导式
# 生成器的特点：
    # 1.可以用next/send方法从中取值
    # 2.生成器中的数据只能从头到尾取一次 ***
    # 3.惰性运算 ：不取生成器是不工作的 ***

# 考题
# def demo():
#     for i in range(4):
#         yield i
# g = demo()
#
# g2 = (i for i in g)
# g1 = (i for i in g)
#
# print(list(g1))  # [0，1，2，3]   # 这一步才开始从g1中取值
# print(list(g2))  # []


# 列表推导式(排序)
    # [i**2 for i in lst]
    # [i**2 for i in lst if i%2 ==0]
# 生成器表达式(不能排序)
    # (i**2 for i in lst)
    # (i**2 for i in lst if i%2 ==0)


# 匿名函数
    # lambda 参数1,参数2,参数3 : 返回值/返回值相关的表达式

# 内置函数
    # min max map filter sorted   单记，可以和 lambda 连用。考点 用匿名函数实现某些功能的时候
    # reduce --> functool   2.7中，3.x放到functool中去了
    # zip sum enumerate

# min max
# l1 = [('a',3), ('b',2), ('c',1)]
# # def func(x):
# #     return x[1]
# # ret = min(l1,key=func)  # 注意这里 min 会先把l2列表中的每个元素传递到func函数中去，然后在取最小的
# # print(ret)
# # 改成lambda
# ret = min(l1,key=lambda x : x[1])
# print(ret)

# filter 函数用于过滤序列。过滤掉不符合条件的元素，返回一个迭代器对象
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判
# 然后返回 True 或 False，最后将返回 True 的元素放到新列表中
# l1 = [1,2,3,4,5,6,7,8,9,10,]
# def is_odd(n):
#     return n % 2 == 1
# g = filter(is_odd, l1)
# for i in g:
#     print(i)

# sorted   排序
# l1 = [1,2,8,7,5]
# print(sorted(l1))
# l2 = [('c',2),('b',3),('a',1)]
# print( sorted(l2, key=lambda x:x[1]) )  # 这个和 min max 有点类似

# zip 拉链方法，会以最短的那个列表或其他的 去组合。生成一个迭代器
# l1 = [1,2,3,4]
# tu1 = ('a','b','c')
# g = zip(l1,tu1)
# print(next(g))
# print(next(g))
# print(next(g))
# 双排拉链方法
# l1 = [1,2,3,4]
# tu1 = ('a','b','c')
# tu2 = ('a1','b1','c1')
# g1 = zip(l1,tu1,tu2)      # 也可以多个元素组合
# for i in g1:
#     print(i)

# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，
# 一般用在 for 循环当中。
# l1 = ['a','b','c','d']
# for index,i in enumerate(l1):
#     print(index,i)