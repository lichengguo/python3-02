#!/usr/bin/env python3
#author:Alnk(李成果)

# 需求：Dog类要新增一个实例属性，但是Cat类不需要


class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run...')

    def sleep(self):
        print('sleep...')


class Cat(Animal):
    pass


class Dog(Animal):
    def __init__(self, name, age, type):
        # 执行父类方法
        super().__init__(name, age)
        self.type = type


alex = Dog('alex', 23, '松狮')
print(alex.type)
