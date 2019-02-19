# -*- coding: utf-8 -*-
# @Time    : 2019/2/17 10:19
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 01  楔子.py
# @Software: PyCharm





'''

def  函数名（参数）：
     函数体


class 类名：
    x=10       # 类变量
    def __init__(self): #  初始化方法
        pass
    def run(self):   # 普通的实例方法
        pass

'''

def foo():
    pass


class Dog:  # 类名首字母大写

     def __init__(self,name,age,sex):
         print("self",self)
         print(name,age,sex)
         self.name=name
         self.age=age
         self.sex=sex

alex=Dog("alex",40,"公")
egon=Dog("egon",22,"母")


#  类的实例变量/属性

#  查看属性
print(alex)
print(alex.name)
print(alex.age)
print(alex.sex)

# 修改
alex.name="李杰"
print(alex.name)
print(egon.name)

# 添加属性

alex.gf="铁锤"
print(alex.gf)

#  删除属性
# del alex.gf
# print(alex.gf)

# 类实例对象的名称空间
print(alex.__dict__) # {'name': '李杰', 'age': 40, 'sex': '公', 'gf': '铁锤'}




'''
egon=Dog("egon",22,"母")
实例化的过程：
    1 开辟一开内存空间，假如内存地址00001100
    2 执行Dog类的__init__方法，注意，self参数是内存地址00001100的空间
    3 j将实例对象赋值给egon变量

'''






