#!/usr/bin/env python3
#author:Alnk(李成果)

# int str bool list tuple dict
# 数据类型的转换。
# str ————> list split
# list ————> str join
# #
# list tuple
# print(list((1,2,3,'alex')))
# print(tuple([1, 2, 3, 'alex']))
# dic = {"name": "jin", "age": 18, "sex": "male"}
# #
# # print(list(dic))

# 补充
# tuple
# 元组中如果只有一个元素且没有逗号（那他不是元组），则与该元素数据类型相同。
# tu1 = (1)
# tu2 = ('alex')
# print(tu1,type(tu1))
# print(tu2,type(tu2))
#
# list
# l1 = [11, 22, 33, 44, 55]
# # 将列表中索引为奇数位的元素删除
# # 正常思路（错误示范）：
# # for index in range(len(l1)):
# #     if index % 2 == 1:
# #         del l1[index]
# # print(l1)
#
# # 方法一：
# # del l1[1::2]
# # print(l1)
#
# # 方法二：
# # 倒叙删除
# for index in range(len(l1)-1,-1,-1):
#     if index % 2 == 1:
#         l1.pop(index)
# print(l1)

#方法三
# count = []
# for index in range(len(l1)):
#     if index % 2 == 1:
#         count.append(index)
#
# for i in count:
#     l1.pop(i)
#
# print(l1)
#
#
# 总结：对于列表来说，你在循环一个列表时，不要改变列表的大小，会影响你的最终结果。

# 字典：
# dic = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'name': '太白'}
# 将字典的键中含有k元素的所有键值对删除
#错误示范
# for key in dic:
#     if 'k' in key:
#         dic.pop(key)
# print(dic)
#
# 满足条件的key添加到一个新列表中，循环列表删除相应的键值对。
# l1 = []
# for key in dic:
#     if 'k' in key:
#         l1.append(key)
# # print(l1)
# for i in l1:
#     dic.pop(i)
# print(dic)