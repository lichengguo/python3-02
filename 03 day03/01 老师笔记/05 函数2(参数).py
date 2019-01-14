# -*- coding: utf-8 -*-
# @Time    : 2019/1/13 15:07
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 05 函数2(参数).py
# @Software: PyCharm

# def Tantan(sex):  #函数的定义:sex形式参数，形参
#     print('搜索')
#     print('左滑动一下')
#     print('右滑动一下')
#     print('发现美女，打招呼')
#     return '小萝莉', '肯德基', '御姐'
#
# # 函数的参数
# Tantan('女') # 函数的执行：'女' 实际的数据， 实参。

# 实参
    # 位置参数。  从左至右，一一对应

# def Tantan(sex,age):
#
#     print('筛选性别%s,年龄%s左右' %(sex,age))
#     print('搜索')
#     print('左滑动一下')
#     print('右滑动一下')
#     print('发现美女，打招呼')
# Tantan('女',28,)
# 练习：
# # n = 3 if 你看到卖西瓜 :n = 1
# def max_(a,b): return a if a > b else b
#     # if a > b:
#     #     return a
#     # else:
#     #     return b
#     # return a if a > b else b
# print(max_(100,200))

# 三元运算符
# a = '饼'
# b = '西瓜'
# ret = a if 3 > 2 else b
# print(ret)

    # 关键字参数。 一一对应。
    # 函数参数较多 记形参顺序较麻烦时，需要关键字参数。
# def Tantan(sex,age,area):
#
#     print('筛选性别%s,%s 附近，年龄%s左右的美女' %(sex,area,age))
#     print('搜索')
#     print('左滑动一下')
#     print('右滑动一下')
#     print('发现美女，打招呼')
# Tantan(sex='女',area='南山区',age='28')
    # 混合参数 : 一一对应,关键字参数必须要在位置参数后面。

# def Tantan(sex,age,area):
#
#     print('筛选性别%s,%s 附近，年龄%s左右的美女' %(sex,area,age))
#     print('搜索')
#     print('左滑动一下')
#     print('右滑动一下')
#     print('发现美女，打招呼')
# Tantan('女',28,area='南山区')

# 形参。
    # 位置参数。 从左至右，一一对应。

# def Tantan(sex,age):
#
#     print('筛选性别%s,年龄%s左右' %(sex,age))
#     print('搜索')
#     print('左滑动一下')
#     print('右滑动一下')
#     print('发现美女，打招呼')
# Tantan('女',28,)

    # 默认参数  : 使用最多的一般不更改的参数，默认参数一定放在位置参数后面

# def Tantan(area,age,sex='girl'):
#
#     print('筛选性别%s, %s 附近，年龄%s左右的美女' %(sex,area,age))
#     print('搜索')
#     print('左滑动一下')
#     print('右滑动一下')
#     print('发现美女，打招呼')
# Tantan('南山区',28,'laddboy')

    # 万能参数 *args, **kwargs

# def Tantan(*args,**kwargs):
#     # 函数的定义： * 代表聚合。
#     # * 将实参角度所有的位置参数放到一个元祖中，并将元组给了args
#     # ** 将实参角度所有的关键字参数放到一个字典中中，并将子弹给了kwargs
#     # print('筛选性别%s, %s 附近，年龄%s左右的美女' %(sex,area,age))
#     # print(args)
#     # print(kwargs)
#     print('筛选地域：%s,年龄%s' % args)
#     print('搜索')
#     print('左滑动一下')
#     print('右滑动一下')
#     print('发现美女，打招呼')
#
# # Tantan('南山区','28', '性格好','身材好', '家境好')
# Tantan('南山区','28',body='身材好',voice='萝莉音',money='白富美')


# def Tantan(*args,**kwargs):
#     # 函数的定义： * 代表聚合。
#     # * 将实参角度所有的位置参数放到一个元祖中，并将元组给了args
#     # ** 将实参角度所有的关键字参数放到一个字典中中，并将子弹给了kwargs
#     print(args)
#     print(kwargs)

# Tantan('南山区','28',body='身材好',voice='萝莉音',money='白富美')
# l1 = [1,2,3]
# l2 = (4,5,6)
# Tantan(*l1,*l2)  # 函数的执行：*iterable 打散  **dic 将所有的键值对添加到kwargs。
# Tantan(1, 2, 3, 4, 5, 6)
# dic1 = {'name':"alex"}
# dic2 = {'age':46}
# Tantan(**dic1,**dic2)

# 形参的最终顺序

# 位置参数  *args  默认参数 **kwargs
#
# def func(a,b,*args,sex='女',):
#     print(a,b,sex,args)
# func(1,2,4,5,6,sex='男')


# def func(a,b,*args,sex='女',**kwargs):
#     print(a,b,sex,args,kwargs)
# func(1,2,4,5,6,name='alex',age=73)