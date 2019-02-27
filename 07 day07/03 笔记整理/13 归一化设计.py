#!/usr/bin/env python3
#author:Alnk(李成果)

# 归一化设计：做成一个接口
# l = [1,2,3]
# dic = {1:2,3:4,5:6}
# s = 'hello'
#
# # 需求：求一个序列对象的长度
# print(l.__len__())
# print(dic.__len__())
# print(s.__len__())
#
# # 归一接口:len()
# print(len(l))
# print(len(dic))
# print(len(s))


# 支付接口归一化
# class Payment(object):
#
#     def __init__(self, name, money):
#         self.name = name
#         self.money = money
#
#
# class AliPay(Payment):
#
#     def pay(self):
#         print('%s通过支付宝消费了%s元' % (self.name, self.money))
#
#
# class WeChatPay(Payment):
#
#     def pay(self):
#         print('%s通过微信消费了%s元' % (self.name, self.money))
#
#
# def pay_func(pay_obj):  # 接口归一
#             pay_obj.pay()
#
#
# alipay = AliPay('alex',100)
# wechatpay = WeChatPay('egon', 200)
# # 调用归一接口
# pay_func(alipay)
# pay_func(wechatpay)


# 支付接口归一化，规范的写法
'''
规范化方法
支付宝 微信 银行卡 nfc支付
同事协作之间的代码规范问题
规定:Payment 就是一个规范类,这个类存在的意义不在于实现实际的功能,而是为了约束所有的子类必须实现pay的方法
Payment : 抽象类
    pay = Payment() # 抽象类: 不能实例化
    抽象类主要就是作为基类/父类,来约束子类中必须实现的某些方法
    抽象类的特点:
        必须在类定义的时候指定metaclass = ABCMeta
        必须在要约束的方法上方加上@abstractmethod方法
'''
from abc import ABCMeta,abstractmethod  # (抽象方法)

class Payment(metaclass=ABCMeta):  # metaclass 元类  metaclass = ABCMeta表示Payment类是一个规范类

    def __init__(self, name, money):
        self.name = name
        self.money = money

    @abstractmethod  # 当子类继承的时候，必须重构pay方法，不然在子类实例化的时候就报错
    def pay(self):
        pass

class AliPay(Payment):

    def pay(self):
        print('%s通过支付宝消费了%s元' % (self.name, self.money))


class WeChatPay(Payment):

    def pay(self):
        print('%s通过微信消费了%s元' % (self.name, self.money))


def pay_func(pay_obj):  # 接口归一
            pay_obj.pay()


alipay = AliPay('alex',100)
wechatpay = WeChatPay('egon', 200)
# 调用归一接口
pay_func(alipay)
pay_func(wechatpay)

