#!/usr/bin/env python3
#author:Alnk(李成果)

# 装饰器
# 需求：测试其他函数的执行效率

# 第一版：写一个功能测试其他同事的函数执行效率
# import time
# def func():
#     time.sleep(0.2)
#     print('非常复杂')
#
# def func1():
#     time.sleep(0.3)
#     print('超级复杂')
#
# 如果被测试的函数很多的话，代码不能重用，会冗余
# start_time = time.time()
# func()
# end_time = time.time()
# print('此函数耗时秒数 %s' % (end_time - start_time))


# 第二版：函数实现这个功能
# import time
# def func():
#     time.sleep(0.2)
#     print('非常复杂')
#
# def func1():
#     time.sleep(0.3)
#     print('超级复杂')
#
# def timmer(f):
#     start_time = time.time()
#     f()
#     end_time = time.time()
#     print('此函数耗时秒数 %s' % (end_time - start_time))
#
# timmer(func)
# timmer(func1)
# 假如函数有1500个，那么你1500个timmer(func)，工作量很大
# 你要在不改变函数执行的指令下，同时测试效率


# 第三版：在不改变函数的执行方式下，同时测试执行效率
# import time
# def func():
#     time.sleep(0.2)
#     print('非常复杂')
#
# def func1():
#     time.sleep(0.3)
#     print('超级复杂')
#
# def timmer(f):
#     start_time = time.time()
#     f()
#     end_time = time.time()
#     print('此函数耗时秒数 %s' % (end_time - start_time))
#
# f1 = func
# func = timmer
# func(f1)        #timmer(func)


# 第四版：装饰器雏形
# import time
# def func():
#     time.sleep(0.2)
#     print('非常复杂')
#
# def func1():
#     time.sleep(0.3)
#     print('超级复杂')
#
# def timmer(f):      #f = func 函数名
#     def inner():
#         start_time = time.time()
#         f()
#         end_time = time.time()
#         print('此函数耗时秒数 %s' % (end_time - start_time))
#     return  inner
#
# func = timmer(func)     #执行timmer函数，将func函数名传给f。等到返回值inner函数名，所以func --> inner
# func()


# 第五版：装饰器雏形的优化，语法糖@
# import time
# def timmer(f):      #f = func 函数名
#     def inner():
#         start_time = time.time()
#         f()
#         end_time = time.time()
#         print('此函数耗时秒数 %s' % (end_time - start_time))
#     return  inner
#
# @timmer     # func = timmer(func)
# def func():
#     time.sleep(0.2)
#     print('非常复杂')
#
# #func = timmer(func)     #执行timmer函数，将func函数名传给f。等到返回值inner函数名，所以func --> inner
# func()


# 其他：被装饰函数带有参数
# import time
# def timmer(f):
#     def inner(*args,**kwargs):      # 函数的定义： * 聚合 args = (1,2,3,444,)
#         start_time = time.time()
#         f(*args,**kwargs)          # 函数执行： * 打散 f(*(1,2,3,4,5,6,))
#         end_time = time.time()
#         print('此函数耗时秒数 %s' % (end_time - start_time))
#     return  inner
#
# @timmer     # func = timmer(func)
# def func(a,b):
#     time.sleep(0.2)
#     print('非常复杂 %s  %s ' % (a,b))
#
# func('aaa','bbb')


# 其他：被装饰的函数要有返回值
# import time
# def timmer(f):
#     def inner(*args,**kwargs):
#         start_time = time.time()
#         ret = f(*args,**kwargs)
#         end_time = time.time()
#         print('此函数耗时秒数 %s' % (end_time - start_time))
#         return ret
#     return  inner
#
# @timmer     # func = timmer(func)
# def func(a,b):
#     time.sleep(0.2)
#     print('非常复杂 %s  %s ' % (a,b))
#     return 666
#
# ret = func('aaa','bbb')
# print(ret)


# 装饰器常用格式
# def wrapper(f):
#     def inner(*args,**kwargs):
#         """执行被装饰函数之前的操作"""
#         ret = f(*args,**kwargs)
#         """执行被装饰函数之后的操作"""
#         return ret
#     return inner
#
# @wrapper
# def func():
#     print(333)
#
# func()


# 装饰器小结
# 其实装饰器本质是闭包，他的传参，返回值都是借助内层函数inner，
# 他之所以借助内层函数inner 就是为了让被装饰函数 在装饰器装饰前后，没有任何区别。
# 看起来没有变化。


# 装饰器用途：
# 登录认证，打印日志等等。给函数增加额外的功能，但是不能影响函数的执行方式,返回值等
#
# 日志
# def wrapper(f):
#     def inner(*args,**kwargs):
#         print("记录日志开始")
#         ret = f(*args,**kwargs)
#         print("记录日志结束")
#         return ret
#     return inner
#
# @wrapper
# def func(a,b):
#     print('我是被装饰的函数')
#     return a + b
#
# ret = func(1,2)
# print(ret)


# 登录认证
# 需求 三个页面需要登录才能访问，只要有一次登录成功就能访问
#
# flag = False
#
# def login():
#     username = input("账号>>>:")
#     password = input("密码>>>:")
#     if username == "alnk" and password == "123":
#         print('登录成功')
#         global flag
#         flag = True
#
# def auth(f):
#     def inner(*args,**kwargs):
#         while 1:
#             if flag:
#                 ret = f(*args,**kwargs)
#                 return ret
#             else:
#                 login()
#     return inner
#
# @auth
# def comment():
#     print('评论页面')
#
# @auth
# def artcle():
#     print('文章页面')
#
# @auth
# def dairy():
#     print('日记页面')
#
# comment()
# artcle()
# dairy()



# 1.对扩展是开放的
# 为什么要对扩展开放呢？
# 我们说，任何一个程序，不可能在设计之初就已经想好了所有的功能并且未来不做任何更新和修改。
# 所以我们必须允许代码扩展、添加新功能。
#
# 2.对修改是封闭的
# 为什么要对修改封闭呢？
# 就像我们刚刚提到的，因为我们写的一个函数，很有可能已经交付给其他人使用了，
# 如果这个时候我们对其进行了修改，很有可能影响其他已经在使用该函数的用户。
#
# 装饰器完美的遵循了这个开放封闭原则。


# 装饰器的进阶
#
# 1、正常情况下查看被装饰的函数的信息的方法在此处都会失效
# 解决办法
# import time
# from functools import wraps
#
# def timmer(func):
#     @wraps(func)            #加在内层函数的正上方
#     def inner(*args,**kwargs):
#         start = time.time()
#         ret = func(*args,**kwargs)
#         print(time.time() - start)
#         return ret
#     return inner
#
# @timmer
# def index():
#     """这是一个主页的信息，哈哈哈"""
#     time.sleep(0.5)
#     print("from index")
#
# index()
# print(index.__doc__)


# 2、带有参数的装饰器
"""
假如你有成千上万个函数使用了一个装饰器，现在你想把这些装饰器都取消掉，你要怎么做？
一个一个的取消掉？ 没日没夜忙活3天。
过两天你领导想通了，再让你加上。
"""
# def outer(flag):
#     # flag = True
#     def timmer(func):
#         def inner(*args,**kwargs):
#             if flag:
#                 print("""执行函数之前要做的""")
#             ret = func(*args,**kwargs)
#             if flag:
#                 print("""执行函数之后要做的""")
#             return ret
#         return inner
#     return timmer
#
# @outer(False)
# def func():
#     print(111)
#
# func()


# 3、多个装饰器，装饰一个函数
# def wrapper1(f):
#     def inner(*args,**kwargs):
#         print('我是装饰器1')
#         ret = f(*args,**kwargs)
#         return ret
#     return inner
#
# def wrapper2(f):
#     def inner(*args,**kwargs):
#         print('我是装饰器2 开头')
#         ret = f(*args,**kwargs)
#         print('我是装饰器2 结束')
#         return ret
#     return inner
#
# @wrapper2
# @wrapper1
# def func():
#     print("in func")
# func()