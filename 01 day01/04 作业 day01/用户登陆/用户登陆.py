#!/usr/bin/env python3
#author:Alnk(李成果)
"""
作业需求:
    1. 三次重试机会
    2. 每次输错误时显示剩余错误次数
"""
name = "alex"
password = "123"
code = "abcd"
flag = True
#密码可输错次数
count = 3

while flag:
    your_name = input("请输入账号：")
    your_password = input("请输入密码：")
    your_code = input("请输入验证码：")

    #判断验证码
    if your_code.lower() != code:
        print("验证码有误，请重新输入。")
        continue

    #判断账号密码
    if your_name == name:
        if your_password == password:
            flag = False
            print("恭喜，登录成功！")
        else:
            count = count - 1
            print("密码错误，剩余次数为[%s]" % (count))
    else:
        print("账号有误，请重新输入。")

    if count == 0:
        print("账号冻结，请联系系统管理员")
        flag = False