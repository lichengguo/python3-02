#!/usr/bin/env python3
# author:Alnk(李成果)
from math import pi


class Circle:
    def __init__(self, r):
        self.r = r  # 半径

    def get_area(self): # 面积
        area = pi * self.r * self.r
        return area

    def get_zhouchang(self):    # 周长
        zhouchang = 2 * pi * self.r
        return zhouchang


class Ring:
    def __init__(self, outer_r, inner_r):
        self.outer_r = outer_r
        self.inner_r = inner_r
        self.outer_circle = Circle(self.outer_r)
        self.inner_circle = Circle(self.inner_r)

    def get_area(self):     # 环形面积
        return self.outer_circle.get_area() - self.inner_circle.get_area()

    def get_zhouchang(self):    # 总周长
        return self.outer_circle.get_zhouchang() + self.inner_circle.get_zhouchang()


r = Ring(5, 3)
print(r.get_area()) # 面积
print(r.get_zhouchang())    # 总周长
