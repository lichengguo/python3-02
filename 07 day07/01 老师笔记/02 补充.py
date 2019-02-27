# -*- coding: utf-8 -*-
# @Time    : 2019/2/24 11:12
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 02 补充.py
# @Software: PyCharm
class Animal(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def run(self):
        print("animal run.....")

    def sleep(self):
        print('sleep....')


class Dog(Animal):
    def __init__(self,name,age,type):
        # 执行父类方法
        # super(Dog,self).__init__(name,age)
        super().__init__(name, age)
        self.type=type


alex=Dog("alex",34,"金毛")
print(alex.type)
alex.run()

