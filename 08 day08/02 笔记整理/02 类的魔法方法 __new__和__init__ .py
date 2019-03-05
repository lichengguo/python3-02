#!/usr/bin/env python3
#author:Alnk(李成果)

# __方法：私有方法
# __方法__：魔法方法


# class Animal(object):
#
#     def __new__(cls, *args, **kwargs):  # 构造方法
#         print('这是一个构造方法')
#         addr = super().__new__(cls)  # 开辟一块内存空间
#         print('addr',addr)
#         return addr  # 一定要return，addr会传到__init__ 方法中的self
#
#     def __init__(self, name, age):  # 初始化方法
#         print('这是一个初始化方法')
#         print('self',self)  # 这个self就是 __new__ 中的addr
#         self.name = name
#         self.age = age
#
#
# alex = Animal('alex', 34)
'''
alex = Animal('alex', 34)
    1.__new__ 方法获得内存空间地址
    2.将空间地址作为第一个参数传给 __init__ ，完成实例空间赋值属性的过程
'''


# 应用场景
# 单例模式：一个类只能实例化一个对象。例如配置文件类，只要加载一次就行了，节省资源

# class Dog(object):
#     pass
# alex = Dog()
# egon = Dog()
# # 不同的内存地址，等于开辟了两块内存空间
# print('alex',id(alex))  # 40867152
# print('egon',id(egon))  # 40867208

# 应用
class Config(object):  # 配置文件
    file_path = ''
    data = 'mysql'
    app = 'LOL'

    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


cf1 = Config()
cf2 = Config()
# 相同的内存地址，等同于只开辟了一块内存空间
print('cf1', id(cf1))  # 32152712
print('cf2', id(cf2))  # 32152712
