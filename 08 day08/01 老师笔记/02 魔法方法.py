# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 10:33
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 01 反射.py
# @Software: PyCharm

# class Animal(object):
#
#      def __new__(cls, *args, **kwargs):
#          print("this is 构造方法")
#          addr=super().__new__(cls)
#          print("addr",addr)
#          return addr
#      def __init__(self,name,age):
#          print("self",self)
#          print("this is 初始化方法")
#          self.name=name
#          self.age=age
#
# alex=Animal("alex",34)
'''
alex=Animal("alex",34)
类实例化过程：
   1 __new__方法获得空间地址
   2 将空间地址作为第一个位置参数传给__init__ ,完成实例空间赋值属性的过程
'''
############################### 1  __init__, __new__ ###############################
# 单例模式：

# class Dog():
#     pass
# alex=Dog()
# egon=Dog()

# class A(object):
#     def __new__(cls,*args):
#         addr=super().__new__(cls)
#         print('addr',addr)
#         return addr
#     def __init__(self,name):
#         print("self",self)
#         self.name=name
#
# a=A("alex")

# class Config(object):
#     _instance=None
#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance=super().__new__(cls)
#         return cls._instance
#     file_path=""
#     data="mysql"
#     app=["app01","app02"]

# cf=Config()
# cf2=Config()
#
# print(id(cf))
# print(id(cf2))
# print(cf == cf2)


###############################  2 __str__  ###############################

# class Animal(object):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def __str__(self): # __str__必须是字符串
#         return  "姓名：%s，年龄：%s"%(self.name,str(self.age))
#
#
# alex=Animal("alex",34)
# egon=Animal("egon",24)
# print(alex)
# print(egon)

###############################  3 __call__  ###############################


# class Animal(object):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def run(self):
#         pass
#
#     def __call__(self, *args, **kwargs):
#         print(" i am call 方法！")
#
# alex=Animal("alex",12)
# print(callable(Animal))
# print(callable(Animal.run))
# print(callable(alex.run))
# print(callable(alex)) # False
# alex()

###############################  4 析构方法 __del__ ###############################
# python 垃圾回收机制： 任何对象在执行过程中失去了指引，则被回收
# a=1
# a=2

# class Animal(object):
#     def __del__(self):
#         print("i am 析构方法！")
#
# a=Animal()
# del a
# import time
# time.sleep(10)
#
#
# class FileHanlde(object):
#     path="......."
#     def __init__(self):
#         self.f=open(self.path,"r")
#     def read(self):
#         return self.f.read()
#     def __del__(self):
#         self.f.close()
#
# fh=FileHanlde()
# fh.read()

###############################  5 getitem ###############################

# class Animal(object):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def __getitem__(self,item):
#         print('item',item)
#         return getattr(self,item,None)
#
#     def __setitem__(self, key, value):
#         print(key)
#         print(value)
#
#     def __delitem__(self, key):
#         print("del item",key)
#
# alex=Animal("alex",45)
# print(alex.name)
# alex.name="xxxx"
# print(alex.name)
# print(alex["name"]) # alex.name
# print(alex["age"]) # alex.age
# alex["gender"]="male"
# del alex["xxx"]


# info={"name":"alex","age":"123"}
# info["gneder"]="male"

###############################  6 getattr ###############################

# class Animal(object):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def __getattr__(self, item):
#         print("getattr",item)
#         return "对象没有%s属性！"%item
#
#     def __setattr__(self, key, value):
#         print("空间地址%s为%s属性赋值%s"%(self,key,value))
#         super().__setattr__(key, value)
#
# alex=Animal("alex",56)
# # print(alex.gender)
# # alex.name="李杰"
# print(alex.name)

###############################  6 __eq__  __len__ ###############################
# class Data(object):
#
#     def __len__(self):
#         return 345
#
# d=Data()
# print(len(d))
#
# class Student(object):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def __eq__(self, other):
#         return self.name==other.name and self.age==other.age
#
# alex=Student("alex",34)
# egon=Student("alex",34)
#
# print(alex==egon)
