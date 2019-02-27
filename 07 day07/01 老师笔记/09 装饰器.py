# -*- coding: utf-8 -*-
# @Time    : 2019/2/24 18:19
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 09 装饰器.py
# @Software: PyCharm
import time

# def new_home(func):
#     t1=time.time()
#     func()
#     t2 = time.time()
#     print(t2-t1)
# new_home(home)


def wrapper_timer(func):
    def inner():
        t1=time.time()
        func()
        t2=time.time()
        print("cost timer",t2-t1)
    return inner

@wrapper_timer
def home():
    print("home....")

# home=wrapper_timer(home)


home()





