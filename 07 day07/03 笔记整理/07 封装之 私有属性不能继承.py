#!/usr/bin/env python3
# author:Alnk(李成果)

# class A(object):
#     __x = 100
#
#
# class B(object):
#     __x = 10  # 在类内存空间存储格式：_B__x = 10
#     __name = 'alex'
#
#     def __init__(self, name):
#         self.__name = name
#         print(self.__x)  # self.__x = self._B__x
#
#
# b = B('bob')  # 10
# print(b.__dict__)
# print(B.__dict__)


# 私有属性不能继承
class A(object):
    __x = 100  # 在类内存空间存储方式：_A__x = 100


class B(object):
    # __x = 10  # 在类内存空间存储方式：_B__x = 10

    def __init__(self):
        print(self.__x)  # self.__x = self._B__x


B()  # 报错，找不到 __x 变量
