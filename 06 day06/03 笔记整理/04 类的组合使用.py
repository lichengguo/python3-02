#!/usr/bin/env python3
# author:Alnk(李成果)

# 在一个类中以另外一个 类的对象(类的实例对象) 作为数据属性，称为类的组合

class Weapon:
    def __init__(self, name, color, shangshangli, ):
        self.name = name
        self.color = color
        self.shangshangli = shangshangli


class Hero:
    def __init__(self, name, sex, hp, exp, ce, weapon):
        self.name = name
        self.sex = sex
        self.hp = hp
        self.exp = exp
        self.ce = ce
        self.weapon = weapon


jiguangqiang = Weapon('激光枪', 'red', 1000)
alex = Hero('alex', 'male', 100, 70, 60, jiguangqiang)  # 把一个类的实例作为参数传入另外一个类的实例化过程

# 获取alex的武器属性
print(alex.weapon.name)
print(alex.weapon.color)
print(alex.weapon.shangshangli)
