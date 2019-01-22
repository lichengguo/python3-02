# -*- coding: utf-8 -*-
# @Time    : 2019/1/19 17:54
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 08 匿名函数，内置函数.py
# @Software: PyCharm
# 匿名函数： 一句话函数
# def func(a,b):
#     return a + b
# print(func(1,3))
# func1 = lambda x,y: x + y
# # print(func1(1,3))
# print(func1)
# 将 x, y 较大者返回
# func2 = lambda x,y: x if x > y else y
# print(func2(100,200))


# eval 慎用
# print('1 + 2')
# print(eval('1 + 2'))

# n=81
# print(eval("n + 4"))  # 85
#
# exec
# s1 = '''
# for i in range(4):
#     print(i)
# '''
# exec(s1)

#
# print(1,2,3,sep='|')  # 分隔符
# print(1,2,3,end=' ')  # 换行符
# f = open('log','w',encoding='utf-8')
# print('写入文件',file=f,flush=True)
# print(help(str))

# def func():
#     pass
# ret = 888
# # print(callable(func))
# print(callable(ret))

# print(float(100),type(float(100)))
# print(bin(100))
# print(abs(-100))
#
# ret = divmod(10,3)
# print(ret)  # (商，余数)


# sum  ***
# print(sum([i for i in range(101)]))
# print(sum([i for i in range(101)],100))

# min 可以加key=函数  ***
# max    ***
# l1 = [3,4,1,2,7,-5]
# print(min(l1))
l1 = [('a',3),('b',2),('c',1)]
# def func(x):
#     '''
#     x = (c,1)   1
#     '''
#     return x[1]
# 改成lambda
# func = lambda x : x[1]
# # # print(lambda x : x[1])
# # # print(func)
# # print(min(l1,key=lambda x : x[1]))

#
# l1 = [i for i in range(10)]
# # print(l1)
# # print(reversed(l1))   ***
# for i in reversed(l1):
#     print(i)
s = 'alex'
# b = s.encode('utf-8')
# s1 = b.decode('utf-8')

# b = s.encode('utf-8')
# print(b)
# bs = bytes(s,encoding='utf-8')
# print(bs)
# print(chr(97))
# print(chr(65))

# repr
# s1 = 'alex'
# # print(s1)
# # print(repr(s1))
# s2 = '我叫%s'%('barry')
# s2 = '我叫%r'%('barry')
# print(s2)

# sorted ***
# l1 = [1,2,8,7,5]
# print(min(l1))

# l1 = [('c',2),('b',3),('a',1)]
# # print(sorted(l1))
# print(sorted(l1,key=lambda x:x[1]))

# print(all([1,2,[1,2,3],'alex',True]))
# print(any([1,'',[],(),False]))
# zip 拉链方法  ***
# l1 = [1,2,3,4]
# tu1 = ('a','b','c')
# tu2 = ('a1','b1','c1')
# g = zip(l1,tu1,tu2)
# # print(list(g))
# for i in g:
#     print(i)
l1 = [1,2,3,4,5,6,7]
# print([i for i in l1 if i > 3])
# ret = filter(lambda x:x>3,l1)
# # # print(ret)
# # # print(list(ret))
# [1,4,9,16,25]
# map
# print([i**2 for i in range(1,6)])
# ret = map(lambda x:x*x,range(1,6))
# print(list(ret))

from functools import reduce

# def func(x,y):
#     return x + y  # 3
ret = reduce(lambda x,y: x + y,[1,2,3,4,5])
print(ret)