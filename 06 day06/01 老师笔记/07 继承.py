# -*- coding: utf-8 -*-
# @Time    : 2019/2/17 17:08
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 07 继承.py
# @Software: PyCharm


# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def run(self):
#         print("self",self)
#         print("running....")
#
#     def sleep(self):
#         print("sleeping")
#
# class Dog(Animal):
#
#     def toshetou(self):
#         print("toshetou....")
#
#     # def run(self):
#     #     print("run run run !!!")
#
#
# class Cat(Animal):
#
#
#
#     def climb_tree(self):
#         print("toshetou....")
#
# alex=Dog("alex")
# egon=Cat("egon")
# # print(alex.name)
# # alex.sleep()
# # egon.run()
# alex.run()

################################### 面试题 ###############################

class Base:
    def __init__(self):
        self.func()
    def func(self):
        print('in base')

class Son(Base):
    def func(self):
        print('in son')

s = Son()