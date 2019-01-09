#!/usr/bin/env python3
#author:Alnk(李成果)
"""
用户交互input。
	类似于qq等app 输入用户名，密码等功能。

	input('提示语') 字符串数据类型

	想要与程序交互一些重要信息时，账号，身份证号，密码等等。
	python2x:
			raw_input() 相当于python3xinput。
			input() 只接受数字类型。
	python3x:input
"""
# 用户交互input
# input出来的数据全部都是str类型。
'''
name = input('请输入姓名：')
age = input('请输入年龄：')
print(name, age)
print(type(name))
# '我的姓名xx,我的年龄xx,我的性别xx.'

#name = input('请输入姓名：')
#age = input('请输入年龄：')
#sex = input('请输入性别：')
#msg = '我的姓名是' + name + ',我的年龄是' + age + ',我的性别是' + sex
#print(msg)
#print('我的名字', '是', '太白')
#print('我的姓名是' + name + ',我的年龄是' + age + ',我的性别是' + sex)
'''