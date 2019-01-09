#!/usr/bin/env python3
#author:Alnk(李成果)
'''
# 变量：将程序运行的中间结果暂存起来，以遍后续程序调用
#
# 变量命名规则：
#     1，变量名必须由数字 字母 下划线 任意组合。
#     2，变量名不能是数字开头。
#     3，变量名不能是Python中的关键字
#         ['and', 'as', 'assert', 'break', 'class', 'continue', 'def',
#         'del', 'elif', 'else', 'except', 'exec', 'finally',
#         'for', 'from', 'global', 'if', 'import', 'in', 'is',
#         'lambda', 'not', 'or', 'pass', 'print', 'raise',
#         'return', 'try', 'while', 'with', 'yield']
#     4，变量名不能使用中文。
#     5，变量名要具有可描述性。
#         name = 'alex'
#         age = 46
#     6，变量名不能过长。
#     7，变量名的推荐：
#         驼峰体： AgeOfOldboy = 47
#         下划线： age_of_oldboy = 47   建议使用这种。

age1 = 12
age2 = age1
age3 = age2
age2 = 36
print(age1,age2,age3)
# 12 36 12

'''

'''
# 常量：一直不变的量
# 
# 命名规则：全部大写的变量 设置为常量。并且放在文件的最上面，设置一些不想让别人改变的变量

BIRTH_OF_CHINA = 1949
BIRTH_OF_CHINA = 1980
print(BIRTH_OF_CHINA)
'''
