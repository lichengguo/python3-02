#!/usr/bin/env python3
# author:Alnk(李成果)

class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if self.name == other.name and self.age == other.age:
            return True


alex = Student('alex', 34)
egon = Student('alex', 34)

print(alex == egon)  # __eq__ 方法注释就为False，否则为True
