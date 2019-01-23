# -*- coding: utf-8 -*-
# @Time    : 2019/1/19 16:14
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 05 生成器.py
# @Software: PyCharm
# 生成器：本质就是迭代器，自己可以通过代码写出来的迭代器。
# 生成器的生成方式：
    #1 ,函数式生成器。
    #2，生成器表达式。

# def func():
#     print(111)
#     return 5
# # func()
# print(func())

# def func():
# #     # print(111)
# #     yield 5
# #     yield 6
# #     yield 7
# #     yield 8
# # g = func() # 生成器对象
# # # print(g)
# # # 一个next对应一个 yield
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))

# def func():
#     # print(111)
#     yield 5
#     yield 6
#     yield 7
#     yield 8
# g = func() # 生成器对象
# # print(g)
# # 一个next对应一个 yield
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


def book():
    for i in range(1,501):
        print('python全栈开发  编号%s' %i)
# book()

def book_niu():
    for i in range(1,501):
        yield 'python全栈开发  编号%s' %i

# book()
# book()
#
# gen = book_niu()
# for i in range(50):
#     print(next(gen))
#
# for i in range(30):
#     print(next(gen))

# 函数中只要有yield 他就不是函数了，他是生成器函数
# yield 与 return的区别
# return直接终止函数，yield不会终止函数。
# return给函数的执行者返回值，yield是给next(生成器对象)返回值。

# send

def func():
    # print(111)
    a = 1
    b = 2
    c = 3
    count = yield a + b + c
    print(count)
    yield 6
    yield 7
    yield 8
g = func()
# print(next(g))
# print(g.send(None))
# print(g.send(None))
# print(g.send(None))
# print(next(g))
# print(g.send('barry'))
# send 与 yield的区别
# send不仅可以取值，还可以给上一个yield发送一个值
# g.send(None)
# 最后一个yield 永远不会收到send发送的值

# yield from
# def func():
#     l1 = ['barry', 'alex', 'wusir', '日天']
#     # yield l1
#     yield from l1  # 将一个可迭代对象转化成了生成器返回
# g = func()
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
# for i in g:
#     print(i)