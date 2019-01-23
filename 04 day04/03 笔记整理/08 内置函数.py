#!/usr/bin/env python3
#author:Alnk(李成果)

# 重要的***
# sum 求和
# print(sum([i for i in range(101)]))
# print(sum([i for i in range(101)],100))

# min 可以加 key=函数 最小值
# max 可以加 key=函数 最大值
# l1 = [3,4,1,2,7,-5]
# print(min(l1))
# print(max(l1))
# l2 = [('a',3),('b',2),('c',1)]
# def func(x):
#     return x[1]
# print(min(l2,key=func))     # 注意这里min 会先把l2列表中的每个元素传递到func函数中去，然后在取最小的
# print(max(l2,key=func))
# 改成lambda
# print(min(l2,key=lambda x:x[1]))

# reversed 翻转。会生成一个迭代器
# l1 = [i for i in range(10)]
# print(l1)
# from collections import Iterator
# g =  reversed(l1)
# print(isinstance(g,Iterator))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# sorted   排序
# l1 = [1,2,8,7,5]
# print(sorted(l1))
# l2 = [('c',2),('b',3),('a',1)]
# print( sorted(l2, key=lambda x:x[1]) )  # 这个和min max 有点类似

# zip 拉链方法，会以最短的那个列表或其他的 去组合。生成一个迭代器
# l1 = [1,2,3,4]
# tu1 = ('a','b','c')
# g = zip(l1,tu1)
# print(next(g))
# print(next(g))
# print(next(g))
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


# 其他
# abs() 函数返回数字的绝对值
# print(abs(-1))
# print(abs(1))

# all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
# 元素除了是 0、空、FALSE 外都算 TRUE
# print( all('a') )
# print( all([1,2,3,'',5,]) )

# any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。
# 元素除了是 0、空、FALSE 外都算 TRUE
# print( any(['',0,False]) )
# print( any([1,0,False]) )

# bin() 返回一个整数 int 或者长整数 long int 的二进制表示 只能是数字
# print(bin(100))

# bool() 函数用于将给定参数转换为布尔类型，如果没有参数，返回 False
# print( bool(0) )
# print( bool(1) )
# print( bool('') )

# callable() 函数用于检查一个对象是否是可调用的。如果返回 True，object 仍然可能调用失败；
# 但如果返回 False，调用对象 object 绝对不会成功
# print( callable(0) )
# a = 1
# print( callable(a) )
# def f():
#     pass
# print( callable(f) )

# chr() 用一个整数作参数，返回一个对应的字符 。对应的ascii码 。可以用于验证码
# print( chr(97) )

# compile() 函数将一个字符串编译为字节代码。 慎用
# s1 = "for i in range(10):print(i)"
# f = compile(s1,'','exec')
# exec(f)

# dict() 函数用于创建一个字典

# dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表
# 带参数时，返回参数的属性、方法列表
# print(dir())
# print(dir(str))

# divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)
# print( divmod(7,3) )

# eval() 函数用来执行一个字符串表达式，并返回表达式的值。
# print( eval("3*7") )

# exec 执行储存在字符串或文件中的 Python 语句，相比于 eval，exec可以执行更复杂的 Python 代码。
# exec( 'print("hello world")' )

# filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，
# 然后返回 True 或 False，最后将返回 True 的元素放到新列表中
# l1 = [1,2,3,4,5,6,7,8,9,10,]
# def is_odd(n):
#     return n % 2 == 1
# g = filter(is_odd, l1)
# for i in g:
#     print(i)

# float() 函数用于将整数和字符串转换成浮点数
# print( float(1) )
# print( float("100") )

# format() 格式化输出函数

# frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素
# a = frozenset(range(10))
# print(a)

# globals() 函数会以字典类型返回全部全局变量
# def f():
#     name = 'alex'
#     print(globals())
# print(globals())
# f()

# hash() 用于获取取一个对象（字符串或者数值等）的哈希值
# print( hash('abc') )

# help() 函数用于查看函数或模块用途的详细说明
# print(help('sys'))
# print(help('str'))

# hex() 函数用于将一个指定数字转换为 16 进制数
# print( hex(10) )

# id() 函数用于获取对象的内存地址
# s = 'a'
# print( id(s) )

# input() 函数接受一个标准输入数据，返回为 string 类型

# int() 函数用于将一个字符串或数字转换为整型
# print( int("10") )
# print( int(10.1) )

# isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()
# a = 2
# print( isinstance(a,int) )
# s = 'alnk'
# print( isinstance(s, str))

# iter() 函数用来生成迭代器
# l1 = [1,2,3,4,]
# print( type(l1) )
# g1 = iter(l1)
# print( type(g1) )

# len() 方法返回对象（字符、列表、元组等）长度或项目个数
# print( len('abc'))

# list() 方法用于将元组或字符串转换为列表
# t1 = (1,2,3,)
# print( list(t1))

# locals() 函数会以字典类型返回当前位置的全部局部变量
# name = 'alnk'
# def f():
#     age = 12
#     print(locals())
# f()
# print(locals())

# map() 会根据提供的函数对指定序列做映射
# def squ(x):
#     return x ** 2
# l1 = [1,2,3,4,5]
# g = map(squ,l1)
# for i in g:
#     print(i)

# next() 返回迭代器的下一个项目

# oct() 函数将一个整数转换成8进制字符串
# print( oct(10))

# open() 方法用于打开一个文件，并返回文件对象

# ord() 函数是 chr() 函数（对于 8 位的 ASCII 字符串）的配对函数，
# 它以一个字符串（Unicode 字符）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值
# print( ord('a'))
# print( chr(97))

# pow() 方法返回 xy（x的y次方） 的值。
# print( pow(2,3))

# print() 方法用于打印输出，最常见的一个函数
# print('abcd',end='|')
# print(1234)
# print('ABCD',end='')
# print('efgh')

# range() 函数返回的是一个可迭代对象（类型是对象），而不是列表类型， 所以打印的时候不会打印列表

# repr() 函数将对象转化为供解释器读取的形式
# s = "abcd"
# print( repr(s))
# dic = {'runoob': 'runoob.com', 'google': 'google.com'}
# print(repr(dic))

# round() 方法返回浮点数x的四舍五入值
# print( round(70.23456,4))
# print( round(70.23456))

# set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等

# str() 函数将对象转化为适于人阅读的形式

# tuple 函数将列表转换为元组

# type() 函数如果你只有第一个参数则返回对象的类型


# 和类相关的内置函数
# classmethod() 学习类以后再来补充
# delattr() 学习类以后再来补充
# getattr() 学习类以后再来补充
# hasattr() 学习类以后再来补充
# issubclass() 学习类以后再来补充
# property()  学习类以后再来补充
# setattr() 学习类以后再来补充
# staticmethod() 学习类以后再来补充
# super() 学习类以后再来补充