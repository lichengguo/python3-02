# -*- coding: utf-8 -*-
# @Time    : 2019/2/17 10:19
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 01 老师笔记  楔子.py
# @Software: PyCharm





def hero(name,sex,hp,ce,level=2,exp=2000,money=10000):
    hero_info = {
        'name':name,
        'sex':sex,
        'hp':hp, # 血值
        'ce':ce,  # 战斗力
        "level":level, # 级别
        "exp":exp,     # 经验
        "money":money  # 金币
    }

    def attack(dog):
        print("%s攻击了%s" % (hero_info["name"], dog["name"]))

    hero_info["attack"]=attack

    return hero_info

def dog(name,dog_type,hp,ce):
    dog_info = {
        'name':name,
        'dog_type':dog_type,
        'hp':hp,
        'ce':ce,
    }

    def bite(hero):
        print("%s咬了%s" % (dog_info["name"], hero["name"],))

    dog_info["bite"]=bite

    return dog_info


alex=hero("alex","male",100,80)
xiaohei=dog("小黑","male",100,5)
'''
alex  = {
        'name':name,
        'sex':sex,
        'hp':hp, # 血值
        'ce':ce,  # 战斗力
        "level":level, # 级别
        "exp":exp,     # 经验
        "money":money,  # 金币
        "attack":attack
    }
alex["attack"]=attack
alex["attack"]()=attack()

'''
alex["attack"](xiaohei)
xiaohei["bite"](alex)
alex['bite'](xiaohei)
