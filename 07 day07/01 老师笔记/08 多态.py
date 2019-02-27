
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

class ApplePay(Payment):
    def pay(self):
        print('%s通过apple消费了%s元' % (self.name, self.money))

class CardPay(object):
    def __init__(self, name, money):
        self.money = money
        self.name = name
    def pay(self):
        print('%s通过银联卡消费了%s元' % (self.name, self.money))


alipay=AliPay("yuan",100)
wechatpay=WeChatPay('yuan',200)
applepay=ApplePay("alex",1000)


cardpay=CardPay("egon",9000)


def pay_func(pay_obj):
    pay_obj.pay()

pay_func(alipay)
pay_func(wechatpay)
pay_func(applepay)
pay_func(cardpay)

##################################################

class A(object):
    pass



class B(A):
    pass

b=B()


def pay_func(pay_obj):
    pay_obj.pay()






