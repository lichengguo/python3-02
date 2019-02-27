# -*- coding: utf-8 -*-
# @Time    : 2019/2/24 17:32
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 07 归一化设计.py
# @Software: PyCharm


# l=[123,456,789]
# info={"name":"alex","age":1000}
# s="hello"


# 归一化设计
# print(l.__len__())
# print(info.__len__())
# print(s.__len__())
#
# len(l)
# len(info)
# len(s)

# def my_len(obj):
#     return obj.__len__()
# print(my_len(s))
############################## 归一接口 ######################

# class Payment(object):
#     def __init__(self,name,money):
#         self.money=money
#         self.name=name
#
# class AliPay(Payment):
#
#     def pay(self):
#         # 支付宝提供了一个网络上的联系渠道
#         print('%s通过支付宝消费了%s元'%(self.name,self.money))
#
# class WeChatPay(Payment):
#
#     def pay(self):
#         # 支付宝提供了一个网络上的联系渠道
#         print('%s通过微信消费了%s元'%(self.name,self.money))
#
#
# def pay_func(pay_obj):
#     pay_obj.pay()
#
# alipay=AliPay("yuan",100)
# wechatpay=WeChatPay('yuan',200)
#
# pay_func(alipay)
# pay_func(wechatpay)

################################### 规范方法 ###########################
from abc import ABCMeta,abstractmethod

class Payment(metaclass=ABCMeta):
    def __init__(self,name,money):
        self.money=money
        self.name=name

    @abstractmethod
    def pay(self):
        pass

class AliPay(Payment):

    def pay(self):
        # 支付宝提供了一个网络上的联系渠道
        print('%s通过支付宝消费了%s元'%(self.name,self.money))

class WeChatPay(Payment):

    def pay(self):
        # 支付宝提供了一个网络上的联系渠道
        print('%s通过微信消费了%s元'%(self.name,self.money))

alipay=AliPay("yuan",100)
wechatpay=WeChatPay('yuan',200)

def pay_func(pay_obj):
    pay_obj.pay()

pay_func(alipay)
pay_func(wechatpay)



