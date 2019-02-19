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
    def climb_stree(self):
        print('climb_stree')


class Fly:
    def fly(self):
        print('fly...')


class Bat(Animal, Fly):     # 多重继承
    pass


class Ying(Animal, Fly):    # 多重继承
    pass


y = Ying('鹰')
y.fly()
