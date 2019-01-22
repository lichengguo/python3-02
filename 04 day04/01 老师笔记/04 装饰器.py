# -*- coding: utf-8 -*-
# @Time    : 2019/1/19 10:57
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 04 装饰器.py
# @Software: PyCharm

# 装饰器
# 第一版：写一个功能测试其他同事的函数的执行效率
# import time
#
# def func():
#     time.sleep(0.2)
#     print('非常复杂')
#
# def func1():
#     time.sleep(0.3)
#     print('超级复杂')
#
# # print(time.time())
# start_time = time.time()
# func()
# end_time = time.time()
# print('此函数的执行效率为%s' % (end_time - start_time))

# 第二版：
# import time
#
# def func():
#     time.sleep(0.2)
#     print('非常复杂')
# func()
# def func1():
#     time.sleep(0.3)
#     print('超级复杂')
#
# def timmer(f):
#     start_time = time.time()
#     f()
#     end_time = time.time()
#     print('此函数的执行效率为%s' % (end_time - start_time))
#
# #
# timmer(func)
# # timmer(func1)
# # func()
# func()
# 如果在实际项目中测试函数，
# 假如函数有1500个，那么你1500个timmer(func)，工作量很大。
# 你要在不改变函数执行的指令下，同时测试效率。


# 第三版：在不改变函数的执行方式下，同时测试执行效率。
# import time
#
# def func():
#     time.sleep(0.2)
#     print('非常复杂')
# # func()
# def func1():
#     time.sleep(0.3)
#     print('超级复杂')
#
# def timmer(f):
#     start_time = time.time()
#     f()
#     end_time = time.time()
#     print('此函数的执行效率为%s' % (end_time - start_time))

# timmer(func)
# timmer(func1)
# func()
# f1 = func
# func = timmer
# func(f1)  # timer(func)
# func = 3
# func()

# 装饰器的雏形
# import time
# def func():
#     time.sleep(0.2)
#     print('非常复杂')
# # func()

# def func1():
#     time.sleep(0.3)
#     print('超级复杂')
# def timmer(f):
#     def inner():
#         start_time = time.time()
#         f()
#         end_time = time.time()
#         print('此函数的执行效率为%s' % (end_time - start_time))
#     return inner
#
# func = timmer(func)
# # 语法糖 @
# func()
# func1 = timmer(func1)
# func2 = timmer(func2)
# func1()



#
# def f2():
#     return 666
# print(f2())

# 装饰器的雏形的优化
# timmer 就是装饰器: 在不改变原函数的调用指令情况下，给原函数增加额外的功能。
# import time
#
# def timmer(f):
#     def inner():
#         start_time = time.time()
#         f()
#         end_time = time.time()
#         print('此函数的执行效率为%s' % (end_time - start_time))
#     return inner
#
# @timmer # func = timmer(func)
# def func():
#     time.sleep(0.2)
#     print('非常复杂')
# func()
# @timmer # func1 = timmer(func1)
# def func1():
#     time.sleep(0.3)
#     print('超级复杂')
#
#
# @timmer # func1 = timmer(func1)
# def func2():
#     time.sleep(0.3)
#     print('超级复杂')
# 语法糖 @
# func()
# func1()

# age1 = 12
# age2 = age1
# age3 = age2
# age2 = 18
# print(age1,age2,age3)

# 被装饰函数带参数
# import time
#
# def timmer(f):
#     def inner(*args,**kwargs):  # 函数的定义： * 聚合。args = (1,2,3,434545,4234.)
#         # a1 = 'wusir'
#         # b1 = 'alex'
#         start_time = time.time()
#         f(*args,**kwargs)  # 函数执行：* 打散。f(*(1,2,3,434545,4234.),)
#         end_time = time.time()
#         print('此函数的执行效率为%s' % (end_time - start_time))
#     return inner
#
# @timmer # func = timmer(func)
# def func(a,b):
#     time.sleep(0.2)
#     print('非常复杂%s%s'% (a,b))
# func('wusir','alex')  # inner()
#
#
# @timmer # func = timmer(func)
# def func(a,b,c):
#     time.sleep(0.2)
#     print('非常复杂%s%s%s'% (a,b,c))
# func('wusir','alex','barry')  # inner()

# 被装饰的函数要有返回值

# import time
#
# def timmer(f):  # f = func
#     def inner(*args,**kwargs):
#         start_time = time.time()
#         ret = f(*args,**kwargs)  # func()
#         end_time = time.time()
#         print('此函数的执行效率为%s' % (end_time - start_time))
#         return ret
#     return inner
#
# @timmer # func = timmer(func)
# def func(a,b):
#     time.sleep(0.2)
#     print('非常复杂%s%s'% (a,b))
#     return 666
# ret = func('wusir','alex')  # inner()
# print(ret)

# @timmer # func = timmer(func)
# def func(a,b,c):
#     time.sleep(0.2)
#     print('非常复杂%s%s%s'% (a,b,c))
# func('wusir','alex','barry')  # inner()



def wrapper(f):
    def inner(*args,**kwargs):
        """执行被装饰函数之前的操作"""
        ret = f(*args,**kwargs)
        """执行被装饰函数之后的操作"""
        return  ret
    return inner

@wrapper
def func():
    print(333)

# 装饰器用途：登录认证，打印日志等等。


# @timmer



# def func3(a,b):
#     return a + b
#
# print(666)
# ret = func3(1,2)
# print(ret)
#
# print(666)
# func3(2,3)
# print(666)
# func3(2,3)
# func3(2,3)
# func3(2,3)
# func3(2,3)


# def wrapper(f): # f = func3函数名
#     def inner(*args,**kwargs):
#         print(666)
#         ret = f(*args,**kwargs)
#         return ret
#     return inner
#
# @wrapper  # func3 = wrapper(func3)
# def func3(a,b):
#     print('in func3')
#     return a + b
#
# ret = func3(1,2)
# print(ret)
# 其实装饰器本质是闭包，他的传参，返回值都是借助内层函数inner，
# 他之所以借助内层函数inner 就是为了让被装饰函数 在装饰器装饰前后，没有任何区别。
# 看起来没有变化。

flag = False

def login():
    username = input('用户名')
    password = input('密码')
    if username == 'alex' and password == '123':
        print('登陆成功')
        global flag
        flag = True

def auth(f): # f = func3函数名
    def inner(*args,**kwargs):
        while 1:
            if flag:
                ret = f(*args,**kwargs)
                return ret
            else:
                login()
    return inner


@auth
def comment():
    print('欢迎来到评论页面')

@auth
def artcle():
    print('欢迎来到文章页面')

@auth
def dairy():
    print('欢迎来到日记页面')

comment()
artcle()
dairy()

dic = {
    1: artcle,
    2:dairy,
    3:comment,
}

