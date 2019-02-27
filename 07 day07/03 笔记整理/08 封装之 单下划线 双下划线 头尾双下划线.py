#!/usr/bin/env python3
#author:Alnk(李成果)

'''
单下划线、双下划线、头尾双下划线说明：
    __foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。
    _foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问。（约定成俗，不限语法）
    __foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。

变量      public          公共的
_变量     protected       受保护的
__变量    private         私有的
'''


class A(object):
    _x = 10


a = A()
print(a._x)  # 10 约定成俗，不限语法