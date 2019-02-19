# -*- coding: utf-8 -*-
# @Time    : 2019/2/17 18:43
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 09 C3算法.py
# @Software: PyCharm
class A1: pass
class A2: pass
class A3: pass
class B1(A1,A2): pass
class B2(A2): pass
class B3(A2,A3): pass
class C1(B1): pass
class C2(B1,B2): pass
class C3(B2,B3): pass
class D(C1, C2, C3): pass

print("从D开始查找：")
for s in D.__mro__:
    print(s)

print("从C3开始查找：")
for s in C3.__mro__:
    print(s)
