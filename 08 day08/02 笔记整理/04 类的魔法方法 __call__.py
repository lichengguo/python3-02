#!/usr/bin/env python3
# author:Alnk(李成果)

# __call__ ：调用
# 只要可以调用的类，内部一定有 __call__ 方法，如果没有则不能调用

# Python中万物都可称为对象，但对象与对象之间也有差别。对象有可被调用和不可被调用之分
# 当一个对象为可被调用对象时，callable(object)返回为True，否则为False：
# 实例是不可以被调用的,但是通过 __call__ 方法可以让实例可以调用

class Animal(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def foo(self):
        print('foo...')

    def __call__(self, *args, **kwargs):
        print('i am call...')


alex = Animal("alex", 12)

# callable :判断一个对象是否可以调用
# print(callable(alex.foo))  # True alex.foo() 可以调用
# print(callable(Animal.foo))  # True Animal.foo() 可以调用
# print(callable(alex))  # False   alex()肯定不能调用呀


# 在上面的类中增加 __call__ 方法
# def __call__(self, *args, **kwargs):
#     print('i am call...')
print(callable(alex))  # 可以调用了
