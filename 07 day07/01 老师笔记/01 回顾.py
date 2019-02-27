# -*- coding: utf-8 -*-
# @Time    : 2019/2/24 10:49
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 01 回顾.py
# @Software: PyCharm

class Base:
    def __init__(self):
        self.func()
    def func(self):
        print('in base')

class Son(Base):
    func="yuan"

s = Son()



