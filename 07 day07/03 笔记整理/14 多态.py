#!/usr/bin/env python3
# author:Alnk(李成果)
##################################################### 景老师博客抄录 ############################
# 多态：指的是一类事物有多种形态
# 动物有多种形态：人，狗，猪
# import abc
# class Animal(metaclass=abc.ABCMeta):  # 同一类事物：动物
#
#     @abc.abstractmethod
#     def talk(self):
#         pass
#
# class People(Animal):  # 动物形态之一：人
#     def talk(self):
#         print('say hello')
#
# class Dog(Animal):  # 动物的形态之二:狗
#     def talk(self):
#         print('say wangwangwang')
#
# class Pig(Animal): #动物的形态之三:猪
#     def talk(self):
#         print('say aoao')


# # 文件有多种形态：文本文件，可执行文件
# import abc
# class File(metaclass=abc.ABCMeta): #同一类事物:文件
#     @abc.abstractmethod
#     def click(self):
#         pass
#
# class Text(File): #文件的形态之一:文本文件
#     def click(self):
#         print('open file')
#
# class ExeFile(File): #文件的形态之二:可执行文件
#     def click(self):
#         print('execute file')


# 什么是多态动态绑定（在继承的背景下使用时，有时也称为多态性）?
# 多态性是指在不考虑实例类型的情况下使用实例
# 在面向对象方法中一般是这样表述多态性：
# 向不同的对象发送同一条消息
# （obj.func():是调用了obj的方法func，又称为向obj发送了一条消息func），不同的对象在接收时会产生不同的行为（即方法）
# 也就是说，每个对象可以用自己的方式去响应共同的消息。所谓消息，就是调用函数，不同的行为就是指不同的实现，即执行不同的函数。
# 比如：老师.下课铃响了（），学生.下课铃响了()，老师执行的是下班操作，学生执行的是放学操作，虽然二者消息一样，但是执行的效果不同

# 多态性
# peo = People()
# dog = Dog()
# pig = Pig()

# peo、dog、pig都是动物,只要是动物肯定有talk方法
# 于是我们可以不用考虑它们三者的具体是什么类型,而直接使用
# peo.talk()
# dog.talk()
# pig.talk()

# 更进一步,我们可以定义一个统一的接口来使用
# def func(obj):
#     obj.talk()
# func(peo)
# func(dog)
# func(pig)
##################################################### 景老师博客抄录 ############################


##################################################################################################
from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    def __init__(self, name, money):
        self.money = money
        self.name = name

    @abstractmethod
    def pay(self):
        pass


class AliPay(Payment):
    def pay(self):
        # 支付宝提供了一个网络上的联系渠道
        print('%s通过支付宝消费了%s元' % (self.name, self.money))


class WeChatPay(Payment):
    def pay(self):
        # 支付宝提供了一个网络上的联系渠道
        print('%s通过微信消费了%s元' % (self.name, self.money))


class ApplePay(Payment):
    def pay(self):
        print('%s通过apple消费了%s元' % (self.name, self.money))


alipay = AliPay("yuan", 100)
wechatpay = WeChatPay('yuan', 200)
applepay = ApplePay("alex", 1000)


def pay_func(pay_obj):
    pay_obj.pay()


pay_func(alipay)
pay_func(wechatpay)
pay_func(applepay)

'''
# 多态的概念
# 要理解什么是多态，我们首先要对数据类型再作一点说明。
# 当我们定义一个class的时候，我们实际上就定义了一种数据类型。
# 我们定义的数据类型和Python自带的数据类型，比如str、list、dict没什么两样
#
# a = list() # a是list类型
# b = Animal() # b是Animal类型
# c = Dog() # c是Dog类型

# 判断一个变量是否是某个类型可以用isinstance()判断：
# >>> isinstance(a, list)
# True
# >>> isinstance(b, Animal)
# True
# >>> isinstance(c, Dog)
# True　
# 看来a、b、c确实对应着list、Animal、Dog这3种类型。
# 但是等等，试试：
# >>> isinstance(c, Animal)
# True
# 看来c不仅仅是Dog，c还是Animal！
# 不过仔细想想，这是有道理的，因为Dog是从Animal继承下来的，
# 当我们创建了一个Dog的实例c时，我们认为c的数据类型是Dog没错，但c同时也是Animal也没错，Dog本来就是Animal的一种！
# 所以，在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。
# 但是，反过来就不行：
# >>> b = Animal()
# >>> isinstance(b, Dog)
# False
# Dog可以看成Animal，但Animal不可以看成Dog
# 所以，上面的支付的例子，如果我们再定义一个ApplePay类型，也从Payment类派生：
# class ApplePay(Payment):
#     def pay(self):
#        print('%s通过苹果支付消费了%s元'%(self.name,self.money))
# 
# applepay=ApplePay("egon",800)

# 你会发现，新增一个Payment的子类，不必对pay()做任何修改，
实际上，任何依赖Payment作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。
# 
# 多态的好处就是，当我们需要传入AliPay、WeChatPay、ApplePay……时，
我们只需要接收Payment类型就可以了，因为AliPay、WeChatPay、ApplePay……都是Payment类型，
# 然后，按照Payment类型进行操作即可。由于Payment类型有pay()方法，
# 因此，传入的任意类型，只要是Payment类或者子类，就会自动调用实际类型的pay()方法，这就是多态的意思：
# 
# 对于一个变量，我们只需要知道它是Payment类型，无需确切地知道它的子类型，
# 就可以放心地调用pay()方法，而具体调用的pay()方法是作用在AliPay、WeChatPay、ApplePay哪个类对象上，
# 由运行时该对象的确切类型决定，这就是多态真正的威力：调用方只管调用，不管细节，
# 而当我们新增一种Payment的子类时，只要确保pay()方法编写正确，不用管原来的代码是如何调用的。
# 这就是著名的“开闭”原则：
# 对扩展开放：允许新增Payment子类；
# 对修改封闭：不需要修改依赖Payment类型的pay()等函数。
'''
