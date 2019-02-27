#!/usr/bin/env python3
# author:Alnk(李成果)

# 实例方法:涉及到实例变量的时候使用
# 类方法classmethod:涉及到类变量的时候使用
# 静态方法staticmethod:不涉及到类变量和实例变量的时候使用

class Student(object):
    school = 'oldboy'

    def __init__(self, name, age):
        self.name = name
        self.age =age

    def run(self):
        print('%s is running... ' % self.name)

    @classmethod
    def foo(cls):
        print(cls)
        print('cls',id(cls))
        print('学校名称:%s' % cls.school)


    @staticmethod
    def mutil(x,y):  # 没有self了
        return x*y

alex = Student('alex', 26)

# 调用静态方法
ret = Student.mutil(3, 6)  # 不需要传入self了
print(ret)

ret2 = alex.mutil(2,8)
print(ret2)
