#!/usr/bin/env python3
# author:Alnk(李成果)


class Hero:
    def __init__(self, name, sex, hp, exp, ce):
        self.name = name
        self.sex = sex
        self.hp = hp
        self.exp = exp
        self.ce = ce

    def attack(self, dog):
        print("%s 攻击了 %s" % (self.name, dog.name))


class Dog:
    def __init__(self, name, type, hp, ce):
        self.name = name
        self.type = type
        self.hp = hp
        self.ce = ce

    def bite(self, hero):
        print("%s 咬了 %s" % (self.name, hero.name))


alex = Hero('alex', 'male', 100, 70, 60)
xiaohei = Dog('xiaohei', '藏獒', 100, 5)

alex.attack(xiaohei)
xiaohei.bite(alex)
