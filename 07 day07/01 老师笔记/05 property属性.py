# -*- coding: utf-8 -*-
# @Time    : 2019/2/24 12:01
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 04 insinstance.py
# @Software: PyCharm



class  Student(object):
    x=100
    def __init__(self,name,age):
        self.__name=name   # 私有属性  __变量
        self.__age=age

    @property
    def get_age(self):
        # print("年龄：%s"%self.__age)
        return self.__age

    def set_age(self,new_age):
        if isinstance(new_age,int) and (new_age>0 and new_age <100):
            self.__age=new_age
        else:
            raise ValueError("年龄不符合条件！")
            #print("年龄不符合条件！")

alex=Student("alex",34)
# print(alex.get_age())
# alex.set_age(44)
# print(alex.get_age())

print(alex.get_age)