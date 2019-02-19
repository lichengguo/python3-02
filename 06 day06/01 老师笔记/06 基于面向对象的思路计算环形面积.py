# -*- coding: utf-8 -*-
# @Time    : 2019/2/17 16:27
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 06 基于面向对象的思路计算环形面积.py
# @Software: PyCharm

from math import pi
class Circle:
    def __init__(self,r):
        self.r=r  #  半径

    def get_area(self):
        area=pi*self.r*self.r
        return area

    def get_zhouchang(self):
        zhouchang=2*pi*self.r
        return zhouchang

# c=Circle(5)
# print(c.get_area())
# print(c.get_zhouchang())

class Ring:
    def __init__(self,outer_r,inner_r):
        self.outer_r=outer_r
        self.inner_r=inner_r
        self.outer_circle = Circle(self.outer_r)
        self.inner_circle = Circle(self.inner_r)

    def get_area(self):
        return self.outer_circle.get_area()-self.inner_circle.get_area()

    def get_zhouchang(self):
        return self.outer_circle.get_zhouchang()+self.inner_circle.get_zhouchang()


r=Ring(5,3)
print(r.get_area())
print(r.get_zhouchang())







