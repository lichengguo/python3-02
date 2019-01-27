# -*- coding: utf-8 -*-
# @Time    : 2019/1/27 12:00
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 6.random模块.py
# @Software: PyCharm

# 和随机相关的内容 random模块

import random
# 随机小数
print(random.random())   # (0,1)
print(random.uniform(5,50))   # (n,m)
# 随机整数
print(random.randint(1,5))  # [1,2]
print(random.randrange(1,5))  # [1,5)
print(random.randrange(1,5,2))  # [1,5)
# 随机从一个列表中取值
ret = random.choice([1,2,3,('k','k2'),{'k1':'v1'}])
print(ret)
ret = random.sample([1,2,3,('k','k2'),{'k1':'v1'}],2)
print(ret)
# 打乱顺序
l = [1,2,3,4,5]
random.shuffle(l)
print(l)

# 生成验证码 ：中午
# 发红包 ：课后作业