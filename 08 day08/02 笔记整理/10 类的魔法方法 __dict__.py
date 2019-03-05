#!/usr/bin/env python3
# author:Alnk(李成果)


class Dog(object):
    def __init__(self, name):
        self.name = name

    def talk(self):
        print('%s is wang wang wang ' % self.name)


print(Dog.__dict__)  # 通过类调用，以字典形式打印类中的所有方法和属性，不包括实例属性
d = Dog('tom')
print('=' * 30)
print(d.__dict__)  # 只打印实例属性，不包括类属性
