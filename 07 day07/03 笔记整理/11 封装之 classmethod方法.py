#!/usr/bin/env python3
#author:Alnk(李成果)

class Student(object):
    school = 'oldboy'

    def __init__(self, name, age):
        self.name = name
        self.age =age

    def run(self):
        print('%s is running... ' % self.name)

    @classmethod
    def foo(cls):
        print(cls)  # 和 Student 的内存地址相同
        print('cls',id(cls))  # 是同一个内存地址
        print('学校名称:%s' % cls.school)


alex = Student('alex', 23)
egon = Student('egon', 24)

# 实例方法是由实例对象调用的,不能直接由类调用
alex.run()
egon.run()

# 类方法 逻辑涉及类信息
# 类方法，可以直接由类调用
Student.foo()
# 当然，实例也可以调用类方法
alex.foo()
