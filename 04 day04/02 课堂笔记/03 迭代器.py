# f = open('01 闭包.py',encoding='utf-8',mode='r')
#
# from  collections import Iterable   #可迭代对象
# from collections import Iterator    #迭代器
#
# print(isinstance(f,Iterator))

# 迭代器
# l1 = [1,2,3,]
# obj1 = iter(l1) #把l1 转化为迭代器
# print(obj1)
# print(next(obj1))   #获取迭代器里的元素
# print(next(obj1))
# print(next(obj1))
# # print(next(obj1))


# while 模拟 for 循环  循环可迭代对象
l1 = [1,2,3,4,5,6,7,8,9]
# obj = l1.__iter__()
obj = iter(l1)
while 1:
    try:
        # print(obj.__next__())
        print(next(obj))
    except StopIteration:
        break