# -*- coding: utf-8 -*-
# @Time    : 2019/1/13 10:13
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 02 深浅copy.py
# @Software: PyCharm

# 赋值运算
l1 = [1,2,3]
l2 = l1
l3 = l2
l1.append(666)
# print(l1,l2,l3)
# print(id(l1),id(l2),id(l3))

# 浅copy
# copy一个新列表(dict)，列表在内存中是新的，但是列表里面的元素，完全沿用之前的元素。
# l1 = [1, 2, 3,[22,33]]
# l2 = l1.copy()
# # print(id(l1),id(l2))
# # l1.append(666)
# # print(l1,l2)
# # print(id(l1[0]))
# # print(id(l2[0]))
# l1[-1].append(666)
# print(l1,l2)


# 深copy
import copy
# 总结：深copy则会在内存中开辟新空间，将原列表以及列表里面的可变的数据类型重新创建一份，
# 不可变的数据类型则沿用之前的。

# l1 = [1, 2, 3, [22, 33]]
# l2 = copy.deepcopy(l1)
# # print(id(l1), id(l2))
# l1[-1].append(666)
# print(l1,l2)
# id 测试对象的内存地址
# == 比较 比较两边的数值是否相等
# print(2 == 2)
# is 判断 判断的两边对象的内存地址是否是同一个。

# l1 = [1, 2, 3, [22, 33]]
# l2 = l1[:]  # 切片 是 浅copy
# l1[-1].append(666)
# # print(id(l1),id(l2)) 不是赋值关系
# print(l1,l2)
