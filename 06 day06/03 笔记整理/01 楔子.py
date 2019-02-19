#!/usr/bin/env python3
# author:Alnk(李成果)
# 人狗大战例子引入面向对象
'''
# 版本1
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

    return hero_info


def dog(name,dog_type,hp,ce):
    dog_info = {
        'name':name,
        'dog_type':dog_type,
        'hp':hp,
        'ce':ce,
    }
    return dog_info


def bite(dog,hero):
    print("%s咬了%s"%(dog["name"],hero["name"]))

def attack(hero,dog):
    print("%s攻击了%s"%(hero["name"],dog["name"]))


alex=hero("alex","male",100,80)
xiaohei=dog("小黑","藏獒",100,5)

# 但是方法之间没有关联性,就会出现如下问题
bite(alex,xiaohei) # alex咬了小黑
'''


# 版本2
def hero(name, sex, hp, ce, level=2, exp=2000, money=10000):
    hero_info = {
        'name': name,
        'sex': sex,
        'hp': hp,
        'ce': ce,
        'level': level,
        'exp': exp,
        'money': money,
    }

    def attack(dog):        # 闭包
        print('%s攻击了%s' % (hero_info['name'], dog['name']))

    hero_info['attack'] = attack

    return hero_info


def dog(name, dog_type, hp, ce):
    dog_info = {
        'name': name,
        'dog_type': dog_type,
        'hp': hp,
        'ce': ce,
    }

    # 这里形成了闭包
    def bite(hero):
        print('%s咬了%s' % (dog_info['name'], hero['name']))

    dog_info['bite'] = bite

    return dog_info


alex = hero('aelx', 'm', 100, 80)
xiaohei = dog('xiaohei', '松狮', 100, 5)

alex['attack'](xiaohei)
xiaohei['bite'](alex)


# 这里其实已经有用到面线对象的思维编程了。