#!/usr/bin/env python3
#author:Alnk(李成果)

# 一般属性
# class Student(object):
#
#     def __init__(self, name, age):
#         self.name = name  # 一般属性
#         self.age =age
#
#
# alex = Student('alex', 24)
# print(alex.age)  # 可以直接在类的外面访问


# 私有化属性 __变量
# 保护数据，不让类外部直接访问
# class Student(object):
#
#     def __init__(self, name, age):
#         self.__name = name  # 实例私有属性：__变量
#         self.__age =age
#
#     def print_age(self):
#         print('年龄：%s' % self.__age)  # 私有化属性可以在类的内部访问
#
#
# alex = Student('alex', 24)
# # print(alex.age)  # 不可以直接在类的外部访问
# alex.print_age()  #


# 需求：要在类的外部访问私有化属性。
# 开接口：能在外部修改类的私有属性，但是能更加精确的控制
# 好处：可以更加精确的控制数据
# class Student(object):
#
#     def __init__(self, name, age):
#         self.__name = name  # 私有属性
#         self.__age =age
#
#     def get_age(self):  # 提供可读属性接口
#         return self.__age
#
#     def set_age(self, new_age):  # 提供可写属性接口
#         if isinstance(new_age, int) and ( 0 < new_age < 120):
#             self.__age = new_age
#         else:
#             # raise ValueError("年龄不符合条件")  # 直接让程序报错，停止程序
#             print("年龄不符合条件")
#
#
# alex = Student('alex', 24)
# # 可读接口
# print(alex.get_age())
# # 可写接口
# alex.set_age(1000)
# print(alex.get_age())
