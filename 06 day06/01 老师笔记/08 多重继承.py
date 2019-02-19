# -*- coding: utf-8 -*-
# @Time    : 2019/2/17 17:51
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 08 多重继承.py
# @Software: PyCharm

class Animal:
    def __init__(self, name):
        self.name = name
    def run(self):
        print("self",self)
        print("running....")
    def sleep(self):
        print("sleeping")


class Dog(Animal):

    def toshetou(self):
        print("toshetou....")

    # def run(self):
    #     print("run run run !!!")

class Cat(Animal):

    def climb_tree(self):
        print("toshetou....")

class Fly:
    def fly(self):
        print("flying...")


class Bat(Animal,Fly):
    pass

class Ying(Animal,Fly):
    pass


y=Ying("xiaoying")
y.fly()