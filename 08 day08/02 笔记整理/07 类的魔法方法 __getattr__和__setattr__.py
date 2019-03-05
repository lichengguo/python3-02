#!/usr/bin/env python3
# author:Alnk(李成果)
#
#
# 如果属性查找在实例以及对应的类中（通过__dict__)失败，
# 那么会调用到类的__getattr__函数,
# 如果没有定义这个函数，那么抛出AttributeError异常。
# 由此可见，__getattr__ 一定是作用于属性查找的最后一步，兜底。


class Animal(object):

    def __init__(self, name, age):
        self.name = name  # object类一定会有__setattr__方法
        self.age = age  # 注意:初始化的时候会调用 __setattr__(self, key, value) 进行赋值

    # def __getattr__(self, item):
    #     print('getattr',item)
    #     return '对象没有%s属性' % item

    def __setattr__(self, key, value):
        # 打印日志
        print("空间地址%s为%s属性赋值%s" % (self, key, value))
        super().__setattr__(key, value)  # 继承父类的__setattr__ 方法


# __getattr__为内置方法，当使用点号获取实例属性时，如果属性不存在就自动调用__getattr__方法
# alex = Animal('alex', 55)
# print(alex.age)
# print(alex.gender)  # 实例中没有gender属性，所以调用__getattr__方法

# __setattr__：当设置类实例属性时自动调用 __init__ 设置属性的时候会调用该方法
alex = Animal('alex', 55)
# alex.name = '李杰'
# print(alex.name)


'''
alex = Animal('alex', 55)
类实例化的过程：
1. __new__ :开辟内存空间,传递空间地址给 __init__
2.__init__ :接收 __new__ 传递过来的空间地址，并且进行赋值操作
3.__setattr__ : 接收 __init__ 的赋值，在内存中进行赋值
'''
