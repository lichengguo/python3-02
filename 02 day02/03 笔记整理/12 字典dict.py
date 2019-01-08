#!/usr/bin/env python3
#author:Alnk(李成果)
'''
列表的不足：
1,列表的数据量越大，查询速度越慢。
2，列表存储的数据没有什么关联性。

基础数据类型之dict
dic = {'name': 'barry'}
字典是以键值对的形式存储的。
数据类型的划分：
    可变的（不可哈希）数据类型：list dict set
    不可变（可哈希）的数据类型：tuple str int bool

字典的键key：必须是不可变得数据类型：int str
字典的值：任意数据类型 变量，对象。
字典可以存储大量的数据，而且字典的查询速度非常快。
字典的key 唯一的不重复的。

字典 3.5之前是无序的。
字典在3.5之后是有序的 初始化时的顺序。

构建数据类型：大量的关系型数据时，要想到字典。
'''
# dic = {'name': 'alex', 'age': 46, 'sex': 'laddyboy'}

# 增删改查其他方法
# 增：
# 有则修改，无则增加
# dic['high'] = 175
# print(dic)
# dic['name'] = '日天'
# print(dic)
# 有则不变，无则增加
# dic.setdefault('weight',200)
# print(dic)
# dic.setdefault('age',73)
# print(dic)

# 删除
# pop 按照key删除键值对,有返回值
# ret = dic.pop('name')
# print(ret)
# clear 清空字典
# dic.clear()
# print(dic)
#
#del 删除整个字典或者某个键值对
# del dic
# del dic['name']

# 改
# dic['name'] = '日天'
# dic = {"name":"jin","age":18,"sex":"male"}
# dic2 = {"name":"alex","weight":75}
# dic2.update(dic)   # 将dic的键值对覆盖添加到dic2中，dic不变。
# print(dic2)
# print(dic)

# 查
# print(dic['name'])
# print(dic['name1'])
# ret = dic.get('name')
# ret = dic.get('name1', '没有此键')
# print(ret)
#
# for i in dic:
#     print(i,dic[i])

# 其他方法：
# dic.keys() dic.values() dic.items()
# print(dic.keys(),type(dic.keys()))
#
# for key in dic.keys():
#     print(key,type(key))
#
# for v in dic.values():
#     print(v)


# 分别赋值
# a, b = 1, 4
# print(a,b)
# a, b = (1,4)
# a, b = [[1,2,3],'alex']
# print(a,b)
# print(dic.items())  # dict_items([('name', 'alex'), ('age', 46), ('sex', 'laddyboy')])
# for k,v in dic.items():
#     print(k,v)
# print(list(dic.items()))

# 嵌套
# dic = {
#     'name_list': ['张三', '李四', 'BARRY'],
#     1:{'name':'taibai', 'age': 18}
#     'barry': {}
# }
# 1，给列表追加一个值：'王五'
# dic['name_list'].append('王五')
# print(dic)
# 2，将BARRY 变成全部小写
# print(dic['name_list'][-1].lower())
# dic['name_list'][-1] = dic['name_list'][-1].lower()
# print(dic)
# 3，给{'name':'taibai', 'age': 18} 增加一个键值对 sex: 男。
# print(dic[1])
# dic[1]['sex'] = '男'
# print(dic)


#