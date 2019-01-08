#!/usr/bin/env python3
#author:Alnk(李成果)
l1 = [11, 22, 33, 44, 55]
# 将列表中索引为奇数位的元素删除
#方法1
# count = []
# for index in range(len(l1)):
#     if index % 2 == 1:
#         count.append(index)
#
# for i in count:
#     l1.pop(i)
#
# print(l1)

#方法2
# print(l1[::2])

#方法3
# for index in range(len(l1)-1, -1, -1):
#     if index % 2 == 1:
#         l1.pop(index)
# print(l1)