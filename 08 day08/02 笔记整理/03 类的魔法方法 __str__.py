#!/usr/bin/env python3
#author:Alnk(李成果)

# 打印类的任何实例对象，都返回 __str__ 的返回值。注意：返回值必须是字符串

class Animal(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # 打印类的任何实例对象，都返回 __str__ 的返回值
        return self.name  # 返回值必须是字符串
        # return "姓名：%s，年龄：%s" % (self.name, str(self.age))


alex = Animal('alex', 34)
egon = Animal('egon', 24)
print(alex)
print(egon)
