#!/usr/bin/env python3
#author:Alnk(李成果)

# 生成器：本质就是迭代器，自己可以通过代码写出来的迭代器。
# 生成器的生成方式：
    #1 ,函数式生成器。
    #2，生成器表达式。

# 函数式生成器
# def func():
#     # print(111)
#     yield 5
#     yield 6
#     yield 7
#     yield 8
#
# g = func()  # 生成器对象
# # 一个next对应一个 yield
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


# 举例
# def book():
#     for i in range(1,501):
#         print("python书籍 编号%s" % i)
# # book()
#
# def book_niu():
#     for i in range(1,501):
#         yield  "python书籍 编号%s" % i
# gen = book_niu()
#
# for i in range(50):
#     print(next(gen))
#
# 函数中只要有yield 他就不是函数了，他是生成器函数
#
# yield 与 return的区别
# return直接终止函数，yield不会终止函数。
# return给函数的执行者返回值，yield是给next(生成器对象)返回值。


# send：不仅可以取值，还可以给上一个yield发送一个值
# def f():
#     a = 1
#     b = 2
#     count = yield a + b
#     print(count)
#     yield 5
#     yield 6
#     yield 7
#
# g = f()
# send 与 next的区别
#
# 1、第一个yield 不能用 send 取值
# print(g.send(1))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
#
# print(next(g))
# print(g.send(None))
# print(g.send(None))
# print(g.send(None))

# 2、最后一个yield 永远不会得到 send 发送的值
# print(next(g))
# print(g.send('a'))


# yield from：将一个可迭代对象转化成了生成器返回
# def func():
#     l1 = ['barry', 'alex', 'wusir', '日天']
#     yield l1
# g = func()
# print(next(g))


# yield from
# def func():
#     l1 = ['barry', 'alex', 'wusir', '日天']
#     yield from l1  # 将一个可迭代对象转化成了生成器返回
# g = func()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
