#!/usr/bin/env python3
#author:Alnk(李成果)
from abc import ABCMeta,abstractmethod

class Payment(metaclass=ABCMeta):  # Payment看做是一只鸭子

    def __init__(self, name, money):
        self.name = name
        self.money = money

    @abstractmethod
    def pay(self):
        pass

class AliPay(Payment):

    def pay(self):
        print('%s通过支付宝消费了%s元' % (self.name, self.money))


class WeChatPay(Payment):

    def pay(self):
        print('%s通过微信消费了%s元' % (self.name, self.money))


class CardPay(object):  # 像鸭子
    def __init__(self,name,money):
        self.money=money
        self.name=name
    def pay(self):
       print('%s通过银联卡支付消费了%s元'%(self.name,self.money))


def pay_func(pay_obj):  # 传入的值只要像鸭子就行
            pay_obj.pay()


alipay = AliPay('alex',100)
wechatpay = WeChatPay('egon', 200)
pay_func(alipay)
pay_func(wechatpay)

# 调用鸭子的接口
cp=CardPay("alvin",1000)
pay_func(cp)

'''
对于静态语言（例如Java）来说，如果需要传入Payment类型，则传入的对象必须是Payment类型或者它的子类，
否则，将无法调用pay()方法。

对于Python这样的动态语言来说，则不一定需要传入Payment类型。我们只需要保证传入的对象有一个pay()方法就可以了

这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，
那它就可以被看做是鸭子
'''