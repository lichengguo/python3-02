# -*- coding: utf-8 -*-
# @Time    : 2019/2/24 11:45
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 03 封装概念.py
# @Software: PyCharm


# class  Student(object):
#
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
# alex=Student("alex",34)
# # print(alex.name)
# # alex.age="1000"
# # print(alex.age)
# alex.gender="male"
# print(alex.__dict__) # {'name': 'alex', 'age': 34}

###########################################

class  Student(object):
    x=100
    def __init__(self,name,age):
        self.__name=name   # 私有属性  __变量
        self.__age=age

    def get_age(self):
        # print("年龄：%s"%self.__age)
        return self.__age

    def set_age(self,new_age):
        if isinstance(new_age,int) and (new_age>0 and new_age <100):
            self.__age=new_age
        else:
            raise ValueError("年龄不符合条件！")
            #print("年龄不符合条件！")

alex=Student("alex",34)
#print(alex.__name)
# 提供可读属性接口
# print(alex.get_age())
# # 提供可写属性接口
# alex.set_age(580)
# print(alex.get_age())

##########################################################
# 注意点：
# 1  外部可以控制私有属性，强烈不建议去这样做，不符合规范
# alex.gender="male"
# print(alex.__dict__) # 私有变量 "_当前类名__私有变量":实际值     {'_Student__name': 'alex', '_Student__age': 34}
# print(alex._Student__name)
# alex._Student__age=10000
# print(alex.get_age())
# 2
# alex.__age=1000
# print(alex.__age)
# alex._Student__gender="male"
# print(alex.__dict__)
# 3 私有化不止适用于实例变量，也适用于类变量

# class Parent(object):
#     x=100
#
# p1=Parent()
# print(p1.x)
# print(p1.__dict__) # {}
# # Parent:类对象
# print(Parent.x)
# print(Parent.__dict__)

######################################
# class Parent(object):
#     __x=100
#
# # print(Parent.__x)
# print(Parent.__dict__)

# 4
# class A(object):
#     __x=100
#
# class B(A):
#     # __x = 10
#     def  __init__(self):
#         print(self.__x)
# B()

# 结论;私有变量不能继承!

# 5 单下划线、双下划线、头尾双下划线说明：
class B(object):
     _x = 10
b=B()
print(b._x)

###################################### 私有方法 #################################


class A(object):
     def __fa(self):
         print('from A')
     def test(self):
        self.__fa()

class B(A):
        def __fa(self):
            print('from B')
b=B()
b.test()


















