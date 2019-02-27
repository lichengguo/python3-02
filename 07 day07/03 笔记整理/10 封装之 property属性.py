#!/usr/bin/env python3
#author:Alnk(李成果)

# 什么是特性property
# property是一种特殊的属性，访问它时会执行一段功能（函数）然后返回值
# 把一个方法属性化

# 为什么要用property？
# 将一个类的函数定义成特性以后，对象再去使用的时候obj.name,根本无法察觉自己的name是执行了一个函数然后计算出来的，
# 这种特性的使用方式遵循了统一访问的原则在C++里一般会将所有的数据都设置为私有的，
# 然后提供set和get方法（接口）去设置和获取，在python中通过property方法可以实现


class People(object):
    def __init__(self, name, weight, height):
        self.name = name
        self.wight = weight
        self.height = height

    @property  # 改变一个方法的调用方式
    def bmi(self):
        return self.wight / (self.height**2)


p1 = People('egon', 75, 1.85)
print(p1.bmi)  # 改变一个方法的调用方式
