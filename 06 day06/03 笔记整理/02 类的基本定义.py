#!/usr/bin/env python3
# author:Alnk(李成果)
'''
类的基本结构：

class 类名：
    x=10       # 类变量
    def __init__(self, name): #  初始化方法 或 构造函数
        self.name = name    # 实例的属性，实例变量
    def run(self):   # 普通的实例方法
        pass
'''


# 类
# 类变量
#
# 类的实例
# 类的实例变量
# 类的实例方法


class Dog:  # 类名首字母大写
    def __init__(self, name, age, sex):  # 注意这里的self就是类的实例对象，此处的self就是Dog('alex', 40, '男')的内存地址或类的实例对象
        self.name = name
        self.age = age
        self.sex = sex


alex = Dog('alex', 40, '男')  # 类的实例化
# print(alex)     # <__main__.Dog object at 0x0000000002229518>  内存地址。alex叫做实例对象

egon = Dog("egon", 22, "母")  # 类的实例化
# print(egon)     # <__main__.Dog object at 0x00000000026F9CC0>
'''
egon=Dog("egon",22,"母")
实例化的过程：
    1 开辟一块内存空间，假如内存地址0x00000000026F9CC0
    2 执行Dog类的__init__方法，注意，self参数是内存地址0x00000000026F9CC0的内存空间
    3 将实例变量赋值给egon变量
'''

# 类的实例变量/属性  增删改查
# 增
# alex.gf = 'tiechui'
# print(alex.gf)

# 删
# del egon.name
# print(egon.name)

# 改
# alex.name = '小李子'
# print(alex.name)
# print(egon.name)

# 查
# print(alex.name)
# print(alex.sex)
# print(alex.age)
# print(egon.name)
# print(egon.sex)
# print(egon.age)


# 类实例对象的名称空间
# print(alex.__dict__)  # {'name': 'alex', 'age': 40, 'sex': '男'}
