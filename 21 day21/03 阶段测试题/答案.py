# 1.简述列表与元组的区别
# 列表：可以添加、修改、删除、排序
# 元组：不能添加、修改、删除、排序


# 2.简述核⼼数据类型列表中 append() | extend() | insert() ⽅法的功能与区别
# append():是在列表最后添加元素
# extend():可以把可迭代对象中的元素一个一个的添加到列表末尾
# insert():可以指定插入位置，在列表任意地方插入元素


# 3.⽤尽可能多的⽅法描述如何规避在对字典进⾏key索引取值时引发 KeyError错误
# 第一用get()方法，第二用异常处理try
# 例如：
# d1 = {
#     "name": "alnk",
#     "age": 19,
#     "sex": 1,
# }
#
# d1.get('c')
#
# try:
#     d1['c']
# except KeyError:
#     print('键不存在')


# 4. 什么是线程？ 什么是进程？ 什么是协程？ 在Python中多线程适⽤于什么场景？为什么？
# 不会


# 5.介绍⼀下⼆分查找算法 并⽤Python代码来实现它
# 不会


# 6.什么是装饰器，它的应⽤场景是什么？ 请写出通过装饰器装饰⼀个带参数的函数的代码
# 在不改变被装饰函数的内部代码的前提下，给函数添加新的功能。应用场景如：打印日至，统计函数执行时间，权限校验等
# def wrapper(fun):
#     def inner(*args, **kwargs):
#         print('函数被装饰之前')
#         func = fun(*args, **kwargs)
#         print('函数被装饰之后')
#         return func
#     return inner
#
#
# @wrapper
# def func(x, y):
#     print('%s+%s=%s' % (x, y, x+y))
#
#
# func(1, 2)


# 7. 简述什么是深拷贝? 什么是浅拷贝? 并说出如下代码得出的结果是什么？
# x = ['lily', '20', 'hr']
# y = x
# x[0] = 'lucy'
# z = list(x)
# x[0] = 'lilei'
# 请问 变量 y 的结果和 z的结果分别是什么

# x = ['lily', 20, ['study', 'coding']]
# y = x[:]
# import copy
# z = copy.deepcopy(x)
# x[2][0] = 'lol'
# 请问此时变量 y 和 z 的值分别是什么？ 为什么？

# 深拷贝：会在内存中开辟新空间，将原列表以及列表里面的可变的数据类型重新创建一份，不可变的数据类型则沿用之前的，指向之前的数据
# 浅拷贝：只拷贝数据的第一层，在内存中独立存放。其他的还是指向原来的数据
# 代码结果1：y = ['lilei', '20', 'hr']    x = ['lucy', '20', 'hr']
# 代码结果2：y = ['lily', 20, ['lol', 'coding']]    z = ['lily', 20, ['study', 'coding']]


# 8. 尽可能多的写出你掌握的创建字典的⽅式
# 第一种
# d1 = {
#     'name': 'alnk',
# }

# 第二种
# d2 = dict(name='alnk', age=18,)

# 第三种
# list1 = [('name', 'alnk'), ('age', 18), ]
# d3 = dict(list1)


# 9. 有列表 a =[‘apple’, ‘banana’, ‘orange’] 现需要将其中各元素通过”|”拼接起来,请写出你的实现⽅式，并说明为什么你要这样实现
# 直接用字符串内置函数join()实现，简单
# a = ['apple', 'banana', 'orange']
# print("|".join(a))


# 10. 根据类的命名空间相关知识 说出下⾯代码会得出什么结果
# class c1:
#     var1 = 'apple'
#
#     def __init__(self):
#         self.var2 = 10
#
#
# x = c1()
# y = c1()
# x.var1 = 100
# # 此时下⾯两句print会打印出什么内容
# print(x.var1, x.var2)  # 100,10
# print(y.var1, y.var2)  # 'apple',10

# 结果
# print(x.var1, x.var2)  # 100,10
# print(y.var1, y.var2)  # 'apple',10


# 11. 请简述 __new__ 与 __init__ 的区别
# __new__：构造方法，获得内存空间地址，将空间地址作为第一个参数传递给__init__,完成实例空间属性赋值的过程
# __init__：初始化方法，在类的实例化时就执行，完成数据属性赋值


# 12. 在Python中⼦类如何重写⽗类的构造函数
# 直接在子类中定义 父类中需要重写的构造函数，构造函数名字相同即可


# 13. 请简述Python中的实例⽅法 静态⽅法 类⽅法
# 实例方法：第一个参数必须是实例对象，只能实例对象调用
# 静态方法：没有cls和self参数，实例对象和类对象都可以调用
# 类方法：第一个参数必须是类对象，实例对象和类对象都可以调用


# 14. 多态 封装 继承 是OOP的三⼤基⽯, 请简述封装的意义是什么？ 并⽤Python来实现
# 封装：是指隐藏对象的属性和实现细节，仅仅对外提供公共的访问方式
# 好处：将变化隔离，便于使用，提高重用性，提高安全性
# class Student(object):
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def get_age(self):  # 提供可读的属性接口
#         return self.__age
#
#     def set_age(self, new_age):  # 提供可写的属性接口
#         if isinstance(new_age, int) and (0 < new_age < 120):
#             self.__age = new_age
#         else:
#             print('年龄超过范围')
#
#
# alnk = Student('alex', 24)
# print(alnk.get_age())


# 15. 简述Python代码异常处理中 raise 与 assert语句的作⽤， 默认情况下, try 与 assert只能
# 触发内置异常如(TypeError, KeyError)，现需要实现引发⽤户⾃定义异常（badString），请写出代码
# raise:抛出异常，一旦抛出异常后，后续的代码讲无法运行。
# assert:断言,必须为真，如果发生异常，则说明表达式为假，用来测试表达式，返回为假，就会触发异常
# class BadString(Exception):
#     """自定义异常类"""
#     def __str__(self):
#         print('不是字符串')
#
#
# def test(name):
#     if isinstance(name, str):
#         pass
#     else:
#         raise BadString()  # 抛出异常
#
#
# test(1)


# 16.如何实现Python多进程之间的数据共享？
# 不会


# 17. 简述内置函数 map() | zip() | filter() | reduce() 的功能
# map() 会根据提供的函数对指定的序列做映射
# def squ(x):
#     return x ** 2
#
#
# l1 = [1, 2, 3, 4]
# g = map(squ, l1)
# for i in g:
#     print(i)

# zip() 拉链方法，会以最短的那个列表或其他的去组合，生成一个迭代器
# l1 = [1, 2, 3, 4]
# t1 = ('a', 'b', 'c')
# g = zip(l1, t1)
# for i in g:
#     print(i)
# t2 = ('a2', 'b2', 'c2')
# g2 = zip(l1, t1, t2)  # 多个元素组合
# for i in g2:
#     print(i)

# filter() 用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，
# 接收2个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递到函数进行判断，然后返回True和False，最后将返回True
# 的元素放到新的列表中
# l1 = [1, 2, 3, 4, 5, 6]
#
#
# def is_odd(x):
#     return x % 2 == 1  # 奇数
#
#
# g = filter(is_odd, l1)
# for i in g:
#     print(i)

# reduce() 函数会对参数序列中的元素经行累计
# from functools import reduce
# def add(x, y):
#     return x + y
#
# l1 = [1,2,3,4,5]
# print(reduce(add, l1))


# 19. 通过列表解析与三元表达式处理列表 [1， 2， 3， 4， 5], 对其中⼩于3的元素加2 对⼤于等于3的元素加3
# print([i+2 if i<3 else i+3 for i in range(1, 6)])


# 20.简述Python中正则表达式的贪婪模式与⾮贪婪模式
# 贪婪模式：正则表达式默认都是贪婪模式，会尽量多的帮我们匹配内容
# 非贪婪模式：在量词后面加一个问号，开启非贪婪模式，尽量少的匹配
# 举例
# import re
# s1 = "<a>bbb<a>"
# s2 = re.findall('<.*>', s1)  # 贪婪模式
# print(s2)  # '<a>bbb<a>'
# s3 = re.findall('<.*?>', s1)  # 非贪婪模式
# print(s3)  # '<a>', '<a>'
