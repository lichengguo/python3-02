#!/usr/bin/env python3
#author:Alnk(李成果)

# 在继承中，父类如果不想让子类覆盖自己的方法，可以将方法定义为私有的
# 私有方法不能继承


# 正常情况
# class A(object):
#     def fa(self):
#         print('from A')
#
#     def test(self):
#         self.fa()
#
# class B(A):
#     def fa(self):
#         print('from B')
#
# b = B()
# b.test()  # from B


# 把 fa 定义为私有的，即 __fa
class A(object):
    def __fa(self):  # 在定义的时候就变形为 _A__fa
        print('from A')

    def test(self):
        self.__fa()  # 只会以自己所在的类为准，基调用 _A__fa

class B(A):
    def __fa(self):
        print('from B')

b = B()
b.test()  # from A
