# -*- coding: utf-8 -*-
# @Time    : 2019/1/13 14:41
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 04 函数1(结构,作用，返回值).py
# @Software: PyCharm

# 面向过程编程
# 面向函数式编程

# 面向过程编程
# s1 = 'fjksdfjsdklf'
# count = 0
# for i in s1:
#     count += 1
# print(count)
#
# l1 = [1, 2, 3, 4, 5]
# count = 0
# for i in l1:
#     count += 1
# print(count)

# 缺点：
# 1，代码重复太多。
# 2，代码的可读性差。

# 面向函数式编程：

# def my_lf_len(s):
#     count = 0
#     for i in s:
#         count += 1
#     print(count)
#
# s1 = 'fjdsklafsdkalfjsda'
# l1 = [1,2,3,3,5,56,6,6]
# # my_lf_len(s1)
# my_lf_len(l1)

# 函数是什么？
# 功能体，一个函数封装的一个功能，


# 结构：
'''
def 函数名():
    函数体
'''

# 函数什么时候执行？
# def my_lf_len(s):
#     count = 0
#     for i in s:
#         count += 1
#     print(count)
#
# my_lf_len('fdskfjskdlf')


# 函数的返回值

def Tantan():
    print('搜索')
    print('左滑动一下')
    print('右滑动一下')
    # return
    print('发现美女，打招呼')
    # return '美女一枚'
    # return ['恐龙一堆']
    return '小萝莉', '肯德基', '御姐'


# 调用一次执行一次
# Tantan()
# Tantan()
# Tantan()

# 返回值
'''
return: 
    1,终止函数。
    2，给函数的调用者（执行者）返回值。
        return       --->   函数名()  None
        return   单个值    --->   函数名()  单个值
        return   多个值    --->   函数名()  (多个值,)
'''
ret = Tantan()
print(ret)
print(type(ret))






