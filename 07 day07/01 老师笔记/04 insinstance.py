# -*- coding: utf-8 -*-
# @Time    : 2019/2/24 12:01
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 04 insinstance.py
# @Software: PyCharm


# s='hello'
#
# print(isinstance(s,int))


class Animal(object):
    pass

class Dog(Animal):
    pass

alex=Dog()
print(isinstance(alex,Dog))
print(isinstance(alex,Animal))

print(type(123))
print(type("hello"))
print(type(alex)== Dog)
print(type(alex)== Animal)

egon=Animal()
print(isinstance(egon,Animal))
print(isinstance(egon,Dog))