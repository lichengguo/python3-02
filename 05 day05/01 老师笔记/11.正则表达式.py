# -*- coding: utf-8 -*-
# @Time    : 2019/1/27 16:47
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 11.正则表达式.py
# @Software: PyCharm

# 正则表达式
# re模块

# 我们使用的模块和这个模块要完成的功能是分不开的
# re模块 ：是用来在python中操作 正则表达式 的
# 要先知道正则表达式是什么？做什么用的？怎么用

# 邮箱地址
# 用户名 密码
# 要检测一个用户输入的内容是否符合我的规则

# 用户输入的内容对于程序员来说都是字符串
# 一个文件是一堆字符串，有很多内容

# 检测某一个字符串是否符合规则 -- 本质 -- 需求一
# 从一大段文字中找到符合规则的字符串 -- 需求二

# 正则表达式  --> 字符串规则匹配的
# 1.判断某一个字符串是否符合规则
# 2.从一段文字中提取出符合规则的内容

# 初识正则表达式
# 字符组
# [1-9]
# [0-9]
# [1-5]
# [a-z]
# [a-f]
# 1.对字母来说 区分大小写
# 2.a-f可以 f-a不行

# 一个字符位置上可以出现的内容是 匹配数字和字母
# [0-9a-zA-Z]

# 正则表达式 ：两位数

# \d    数字              digit
# \w    数字 字母 下划线  word
# \s    space enter table space
# \t    table             table
# \n    回车              next
# \b    匹配一个单词的边界

# \D    非数字
# \W    非数字字母下划线
# \S    非空白

# ^      一个字符串的开始
# $      一个字符串的结尾
# ^xxxx$  约束的了整个字符串中的内容必须一一与表达式对应上

# |       表示或
# ()      分组
    # a(b|c)d
# .       表示除了换行符以外的任意字符

# [^ABC]  非字符组

# {n}   在这个量词前面的一个元字符出现n次
# {n,}  在这个量词前面的一个元字符出现n次或n次以上
# {n,m}  在这个量词前面的一个元字符出现n次到m次以上
# ?     出现0次或者1次
# +     出现1次或者多次
# *     出现0次或者多次


# 身份证号
# ^([1-9]\d{16}[\dx]|[1-9]\d{14})$
# ^[1-9]\d{14}(\d{2}[\dx])?$

import re

# ret = re.findall('\d+','h2b3123') # 匹配所有
# print(ret)

# ret = re.search('\d+','h2b3123')  # 只匹配从左到右的第一个
# print(ret)  # 变量
# print(ret.group())

# ret = re.search('\d+','aaaab123')  # 只匹配从左到右的第一个
# if ret:
#     print(ret.group())

# '\d+'  --> 正则规则 --> python代码 --> 将字符串按照代码执行匹配
# re.findall('\d+','ahkfgilWIVKJBDKvjgheo')
# re.findall('\d+','ahkfgilsk0194750dfjWIVKJBDKvjgheo')
# re.findall('\d+','ahkfgilsk0vv194750dfjWIVKJBDKvjgheo')
# ret = re.compile('\d+')
# ret.findall('ahkfgilWIVKJBDKvjgheo')
# ret.search('ahkfgilsk0194750dfjWIVKJBDKvjgheo')

# ret = re.finditer('\d+','dskh1040dsvk034fj048d3g5h4j')
# for r in ret:
#     print(r.group())

# search
# findall
# compile 节省时间 一条正则表达式用多次
# finditer 节省空间 结果的条数很多的时候

# ret = re.findall('www.(?:baidu|oldboy).com', 'www.oldboy.com')
# print(ret)
# 分组遇到findall，优先显示分组中匹配到的内容
# 如何取消分组优先？


s = '<h1>abc</h1>'
# ret = re.search('<(\w+)>(.*?)<(/\w+)>',s)
# print(ret.group(1))
# print(ret.group(2))
# print(ret.group(3))

# ret = re.search('<(?P<tag>\w+)>(.*?)<(/\w+)>',s)
# print(ret.group('tag'))

s = '<h1>abc</h1>'
ret = re.search('<(?P<tag>\w+)>(.*?)</(?P=tag)>',s)
print(ret)
