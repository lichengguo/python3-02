# -*- coding: utf-8 -*-
# @Time    : 2019/2/24 16:32
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 06 classmethod方法与staticmethod方法.py
# @Software: PyCharm



class  Student(object):
    school="oldboy"
    def __init__(self,name,age):
        self.name=name   # 私有属性  __变量
        self.age=age

    def run(self):
        print("self",id(self))
        print("%s is running..."%self.name)

    def bar(self):
        print("学校名称：%s" % Student.school)

    @classmethod
    def foo(cls):
        print('cls',id(cls))
        print("学校名称：%s"%cls.school)

    @staticmethod
    def multi(x,y):
        return x*y



alex=Student("alex",34)
egon=Student("egon",34)

# 1 实例方法是由实例对象调用的
alex.run()  # 基于实力方法调用
egon.run()
Student.run(alex) # 等同于alex.run()，基于函数调用

# # 2  类方法:逻辑涉及类信息
# alex.foo()
# egon.foo()
# Student.foo()
# alex.bar()

# 3 静态方法   基于函数调用

ret=alex.multi(3,4)
print(ret)
ret=Student.multi(3,6)
print(ret)


