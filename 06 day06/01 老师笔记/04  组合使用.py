# -*- coding: utf-8 -*-
# @Time    : 2019/2/17 14:38
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 04  组合使用.py
# @Software: PyCharm



class Weapon:

    def __init__(self,name,color,shashangli):
        self.name=name
        self.color=color
        self.shashangli=shashangli

jiguangqiang=Weapon("激光枪","red",1000)
yidalipao=Weapon("意大利炮","black",20000)
print(jiguangqiang)



class Hero:

    def __init__(self,name,sex,hp,exp,ce,weapon):
        self.name=name
        self.sex=sex
        self.hp=hp
        self.exp=exp
        self.ce=ce
        self.weapon=weapon


alex=Hero("alex","male",100,70,60,jiguangqiang)
print(alex.ce)

print(alex.weapon.color)




