#!/usr/bin/env python3
#author:Alnk(李成果)

# 一般属性存储关系
# class Student(object):
#
#     def __init__(self, name, age):
#         self.name = name  # 一般属性
#         self.age =age
#
#
# alex = Student('alex', 24)
# print(alex.name)
# # __dict__ 打印alex实例对象的所有变量
# print(alex.__dict__)  # {'name': 'alex', 'age': 24}
# alex.sex = 'F'
# # __dict__ 打印alex实例对象的所有变量
# print(alex.__dict__)  # {'name': 'alex', 'age': 24, 'sex': 'F'}


# 私有属性存储关系
class Student(object):

    def __init__(self, name, age):
        self.__name = name  # 私有属性
        self.__age =age

    def get_age(self):  # 提供可读属性接口
        return self.__age

    def set_age(self, new_age):  # 提供可写属性接口
        if isinstance(new_age, int) and ( 0 < new_age < 120):
            self.__age = new_age
        else:
            print("年龄不符合条件")


# 1 外部可以控制私有属性，强烈不建议使用，不规范
# alex = Student('alex', 24)
# print(alex.__dict__)  # 私有属性  "_当前类名__私有变量":实际值 {'_Student__name': 'alex', '_Student__age': 24}
# alex.sex = 'F'
# print(alex.__dict__)  # {'_Student__name': 'alex', '_Student__age': 24, 'sex': 'F'}
# print(alex._Student__name)  # 直接访问私有属性
# #
# alex._Student__age = 10000  # 直接修改私有属性，但是不建议这么用，不规范，私有变量不能改
# print(alex.get_age())
# #
# # 结论：python的私有变量并不是真正的私有变量，还是有方法可以控制的。但是，注意不建议使用，不规范
#
#
# 2
# alex = Student('alex', 24)
# alex.__age = 1000  # 相当于在alex的实例内存空间追加了一个变量 __age = 1000
# print(alex.__age)
# print(alex.__dict__)  # {'_Student__name': 'alex', '_Student__age': 24, '__age': 1000}
