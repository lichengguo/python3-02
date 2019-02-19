# -*- coding: utf-8 -*-
# @Time    : 2019/2/17 14:38
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 04  组合使用.py
# @Software: PyCharm


class Hero:
    x=100
    role="警察"
    name="yuan"
    sex="male"
    def __init__(self,name,sex,hp,exp,ce):
        self.name=name
        self.hp=hp
        self.exp=exp
        self.ce=ce

    def attack(self,dog):  # 实例方法
        print("%s攻击了%s"%(self.name,dog.name))


class Dog:
    def __init__(self,name,type,hp,ce):
        self.name=name
        self.type=type
        self.hp=hp
        self.ce=ce

    def bite(self,hero):
        print("%s 咬了%s" % (self.name,hero.name))



alex=Hero("alex","male",100,70,60)
egon=Hero("egon","male",100,70,60)

xiaohei=Dog("xiaohei","藏獒",100,5)
dahuang=Dog("dahuang"," 中华田园犬",100,1)

alex.attack(xiaohei)
xiaohei.bite(alex)


# alex.attack("小黑")
# egon.attack("大黄")

# print(alex.x)
# print(alex.role)
# print(egon.x)
# print(egon.role)

# print(id(alex.name))
# print(id(egon.name))
# print(id(alex.x))
# print(id(egon.x))
# print(alex.name)


