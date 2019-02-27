#!/usr/bin/env python3
#author:Alnk(李成果)

# 私有属性不仅适用于实例属性，也适用于类属性

# class Parent(object):
#     x = 100
#
#
# p1 = Parent()
# print(p1.x)
# print(p1.__dict__)  # {}  这里为空的原因是：实例空间没有实例属性
# # 类对象
# print(Parent.x)
# print(Parent.__dict__)


class Parent(object):
    __x = 100

p1 = Parent()
# print(p1.__x)  # 类私有属性，外部不能直接访问

# print(Parent.__x)  # 类私有属性，外部不能直接访问
print(Parent.__dict__)  #{'_Parent__x': 100}

print(Parent._Parent__x)  # 可以通过这种方法访问，但是强烈建议不要这么使用
