#!/usr/bin/env python3
#author:Alnk(李成果)

class Animal(object):
    gender = 'male'

    def  __init__(self, name, age):
        self.name = name
        self.age = age

    def __getitem__(self, item):
        # print('__getitem__ 被调用')
        print('业务逻辑')
        # print('itme:',item)
        return getattr(self, item, None)  # 如果找不到item变量，则返回None
        # return self.__dict__[item]

    def __setitem__(self, key, value):
        print('__setitem__ 被调用')
        # print(key)
        # print(value)
        self.__dict__[key] = value
        # print(self.__dict__)

    # def __delitem__(self, key):
    #     print('__delitem__被调用')
    #     del self.__dict__[key]

#__getitem__(self, item)：返回键对应的值
# 调用一个属性的前加自己的业务逻辑等
# alex = Animal('alex', 34)
# print(alex['name'])  # alex.name
# print(alex['age'])  # alex.age
# print(alex['gender'])  # alex.gender
# print(alex['job'])  # alex.job


# __setitem__(self, key, value):设置给定键的值
# alex = Animal('alex', 34)
# alex['job'] = 'IT'
# # alex['gender'] = 'male'
# print(alex['job'])
# print(alex.__dict__)


# __delitem__:删除给定键对应的元素
# alex = Animal('alex', 34)
# print(alex.__dict__)  # {'name': 'alex', 'age': 34}
# del alex['name']
# print(alex['name'])
# print(alex.__dict__)  # {'age': 34}
