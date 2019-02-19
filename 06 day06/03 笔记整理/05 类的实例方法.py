#!/usr/bin/env python3
# author:Alnk(李成果)


class Hero:
    def __init__(self, name, sex, hp, exp, ce):
        self.name = name
        self.sex = sex
        self.hp = hp
        self.exp = exp
        self.ce = ce

    def attack(self, dog):  # 类的实例方法，简称方法
        print('%s 攻击了 %s' % (self.name, dog))


alex = Hero('alex', 'male', 100, 70, 60, )
egon = Hero('egon', 'male', 100, 70, 20, )
alex.attack('小黑')
egon.attack('大黄')
