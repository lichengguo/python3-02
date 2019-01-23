#!/usr/bin/env python3
#author:Alnk(李成果)

# 生成器表达式 与 列表推导式非常类似
# 列表推导式         [   ]
# 生成器表达式       (   )


# 列表推导式: 用一行代码构建一个列表，列表推导式只能构建简单的或者比较复杂的列表
#
# 构建一个列表,[100以内所有的偶数]，[0,2,4,6,8....100]
# 方法1
# l1 = []
# for i in range(0,101,2):
#     l1.append(i)
# print(l1)
#
# 列表推导式分为两种模式：
# 1，循环模式。 [变量(加工后的变量) for 变量 in iterable]
# 构建一个列表,[100以内所有的偶数]
# print( [ i for i in range(0,1001,2) ] )
#
# [1,4,9,16,25,36,49]
# print([ i**2 for i in range(1,8)])
#
# ['python1期', 'python2期', .....'python20期']
# print(['python%s期'% i  for i in range(1,21)])

# 2，筛选模式。[变量（加工后的变量） for 变量 in iterable if 条件]
# 30以内能被2整除的数的平方
# print([ i**2 for i in range(1,31) if i % 2 == 0])
#
# [1,2,3,4,6,7,8]
# print([i for i in range(1,9) if i != 5])
#
# l1 = ['wusir','ba', 'aa' ,'alex']
# 过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
# print([i.upper() for i in l1 if len(i) > 3])
#
#names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
# 将列表中的至少含有两个'e'的人名留下来。
# 方法1
# l1 = []
# for l in names:
#     for name in l:
#         if name.count('e') >= 2:
#             l1.append(name)
# print(l1)
#
#print([name for l in names for name in l if name.count('e') >= 2])


# 生成器表达式：
# 优势：
# 1，一行搞定。
# 2，节省内存。
#
# 两种模式：
# 1，循环模式。 （变量(加工后的变量) for 变量 in iterable）
# （变量（加工后的变量） for 变量 in iterable if 条件）
#
#2，筛选模式。(变量（加工后的变量） for 变量 in iterable if 条件)