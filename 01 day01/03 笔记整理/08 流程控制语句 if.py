#!/usr/bin/env python3
#author:Alnk(李成果)
"""
流程控制语句if
	根据不同的条件，选择不同的结果。回家，三条路可选择。
    1，基本用法：
        if 条件:
            执行结果
        其他语言：
            if{条件}{结果}
    2,5种结构：
        if 条件:
            执行结果
    大量的出现在你的程序中，让你的程序有不同的执行流程。
"""

# 单独if
'''
age = int(input('请输入年龄'))

if age > 18:
    print('做你想做的事儿')
print(666)	
'''

# if else
'''	
age = int(input('请输入年龄'))

if age > 18:
    print('做你想做的事儿')
else:
    print('安心上学....')
'''

# if elif elif ...
"""
num = input('请输入数字：')

if num == '5':
    print('请你吃饭')
elif num == '1':
    print('带你去香港')
elif num == '3':
    print('请你去大宝剑')
"""

# if elif elif ... else
'''
score = int(input("输入分数:"))

if score > 100:
    print("我擦，最高分才100...")
elif score >= 80:
    print("B")
elif score >= 90:
    print("A")
elif score >= 60:
    print("C")
elif score >= 40:
    print("D")
else:
    print("太笨了...E")
print(666)
'''
# if 嵌套
'''
code = 'ABCD'
your_code = input('输入验证码')
username = input('请输入用户名')
password = input('请输入密码')
if your_code == code:
    if username == 'alex' and password == '123':
	    print('登录成功')
    else:
	    print('用户名或者密码错误')
else:
    print('您输入的验证码错误')
'''