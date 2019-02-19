#!/usr/bin/env python3
# author:Alnk(李成果)


class Animal:
    def __init__(self, name):
        self.name = name

    def run(self):
        print('running')

    def sleep(self):
        print('sleeping')


class Dog(Animal):
    def tushetou(self):
        print('tushetou')


class Cat(Animal):
    def climb_tree(self):
        print('climb_tree')

    def run(self):  # 会覆盖父类的run方法
        print('cat running')


# alex = Dog('alex')  # 注意虽然Dog类没有__init__初始化，但是父类有，所以还是需要传参
# print(alex.name)
# alex.run()  # 在父类中找到了run方法
#
# egon = Cat('egon')
# print(egon.name)
# egon.run()


# 面试题
class Base:
    def __init__(self):
        self.func()

    def func(self):
        print('in base')


class Son(Base):
    def func(self):
        print('in son')


s = Son()  # in son
# 一个实例对象查找某个对象一定严格按照如下顺序
# 实例对象的内存空间 ---> 实例对象对应的类空间里查找  ---> 实例对象对应的类空间的父类空间查找
