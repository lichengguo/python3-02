#!/usr/bin/env python3
#author:Alnk(李成果)

# 1、整理装饰器的形成过程，背诵装饰器的固定格式
# 形成过程
# 第一版：写一个功能测试其他同事的函数执行效率
# 第二版：函数实现这个功能
# 第三版：在不改变函数的执行方式下，同时测试执行效率
# 第四版：装饰器雏形
# 第五版：装饰器雏形的优化，语法糖@
# 其他：被装饰函数带有参数
# 其他：被装饰的函数要有返回值

# 固定格式
# def wrapper(func):
#     def inner(*args,**kwargs):
#         """执行被装饰函数之前的操作"""
#         ret = func(*args,**kwargs)
#         """执行被装饰函数之后的操作"""
#         return ret
#     return inner



# 2、编写装饰器,在每次执行被装饰函数之前打印一句 '每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码'
# def wrapper(func):
#     def inner(*args,**kwargs):
#         print('每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码')
#         result = func(*args,**kwargs)
#         return result
#     return inner
# 
# @wrapper
# def f1(a):
#     print('in f1 参数[%s]' % a )
# 
# f1(1111111)



# 3、编写装饰器,在每次执行被装饰函数之后打印一句’每次执行完被装饰函数之后都得先经过这里,这里根据需求添加代码
# def wrapper(func):
#     def inner(*args,**kwargs):
#         print('每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码')
#         result = func(*args,**kwargs)
#         return result
#     return inner
# 
# @wrapper
# def f1(a):
#     print('in f1 参数[%s]' % a )
# 
# f1(1111111)



# 4、编写装饰器,在每次执行被装饰函数之前让用户输入用户名,密码,给用户三次机会,登录成功之后,才能访问该函数
# flag = False
# 
# def login():
#     username = input("请输入用户名>>>:").strip()
#     password = input("请输入密码>>>:").strip()
#     if username == "alnk" and password == "123":
#         print('登陆成功！\n')
#         global flag
#         flag = True
#     else:
#         print("账号或者密码错误!")
# 
# def auth(func):
#     def inner(*args,**kwargs):
#         count = 0
#         while count < 3:
#             if flag:
#                 result = func(*args,**kwargs)
#                 return result
#             else:
#                 login()
#                 count += 1
#     return inner
# 
# @auth
# def func1():
#     print('恭喜访问func1函数')
# 
# func1()



# 5、编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件,只支持单用户的账号密码,给用户三次机会），
# 要求登录成功一次，后续的函数都无需再输入用户名和密码
# flag = False
#
# def login():
#     with open('user_info',encoding='utf-8',mode='r') as f:
#         user_list = f.readline().strip().split('|')
#     name = user_list[0]
#     pwd = user_list[1]
#     username = input("请输入用户名>>>:").strip()
#     password = input("请输入密码>>>:").strip()
#     if username == name and password == pwd:
#         print('登陆成功！')
#         global flag
#         flag = True
#     else:
#         print('账号或者密码错误')
#
# def auth(func):
#     def inner(*args,**kwargs):
#         count = 0
#         while count < 3:
#             if flag:
#                 ret = func(*args,**kwargs)
#                 return ret
#             else:
#                 login()
#                 count += 1
#     return inner
#
# @auth
# def f1():
#     print('in f1 ')
#
# @auth
# def f2():
#     print('in f2 ')
#
# @auth
# def f3():
#     print('in f3 ')
#
# f1()
# f2()
# f3()



# 6、编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件,可支持多账号密码），
# 要求登录成功一次（给三次机会），后续的函数都无需再输入用户名和密码。
# import os
#
# flag = False
#
# def login():
#     username = input("请输入用户名>>>:").strip()
#     password = input("请输入密码>>>:").strip()
#
#     if os.path.exists('user/%s' % username):    # 判断是否存在以用户名命名的文件
#         with open('user/%s' % username,encoding='utf-8',mode='r') as f:
#             user_list = f.readline().strip().split('|')
#         name = user_list[0]
#         pwd = user_list[1]
#
#         if username == name and password == pwd:
#             print('登陆成功！')
#             global flag
#             flag = True
#         else:
#             print('账号或者密码错误')
#     else:
#         print('账号或者密码错误')
#
# def auth(func):
#     def inner(*args,**kwargs):
#         count = 0
#         while count < 3:
#             if flag:
#                 ret = func(*args,**kwargs)
#                 return ret
#             else:
#                 login()
#                 count += 1
#     return inner
#
# @auth
# def f1():
#     print('in f1 ')
#
# @auth
# def f2():
#     print('in f2 ')
#
# @auth
# def f3():
#     print('in f3 ')
#
# f1()
# f2()
# f3()



# 7、给每个函数写一个记录日志的功能，
# 功能要求：每一次调用函数之前，要将函数名称，时间节点记录到log的日志中
# 所需模块：
# import time
# struct_time = time.localtime()
# print(time.strftime("%Y‐%m‐%d %H:%M:%S",struct_time))
#
# import time
#
# def write_log(func_name,time_node):
#     with open('log.txt',encoding='utf-8',mode='a') as f:
#         f.write("函数名:[%s] 时间:[%s]\n" % (func_name,time_node) )
#
# def wrapper(func):
#     def inner(*args,**kwargs):
#         # 获取时间戳
#         struct_time = time.localtime()
#         time_node = time.strftime("%Y-%m-%d %H:%M:%S",struct_time)
#         # 获取被装饰的函数名
#         func_name = func.__name__
#         # 调用日志函数
#         write_log(func_name,time_node)
#         res = func(*args,**kwargs)
#         return res
#     return inner
#
# @wrapper
# def f1():
#     time.sleep(4)
#     print('in f1')
#
# @wrapper
# def f2():
#     time.sleep(10)
#     print('in f2')
#
# @wrapper
# def f3():
#     time.sleep(5)
#     print('in f3')
#
# f1()
# f2()
# f3()