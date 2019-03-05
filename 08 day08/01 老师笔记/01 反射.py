# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 10:33
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 01 反射.py
# @Software: PyCharm

# class Animal(object):
#      gender="male"
#      def __init__(self,name,age):
#          self.name=name
#          self.age=age
#      # def foo(self):
#      #     print("foo.....")
#
# alex=Animal("alex",34)
# print(alex.name)
# print(alex.age)
# while 1:
#     attr = input("请问查看alex的什么属性>>>")
#     # print("attr",attr)
#     # print("attr",type(attr))
#     # print(alex.attr)
#     print(getattr(alex,attr))  # alex.gender

##########################################

# print(getattr(alex,"foo")) # alex.foo
# getattr(alex,"foo")()  # # alex.foo()

# if hasattr(alex,"foo"):
#      getattr(alex,"foo")()
# else:
#     print("没有该方法！")
#
# setattr(alex,"gender","female") # alex.gender=female
# print(alex.gender)
#
# print(alex.age)
# setattr(alex,"age",1000)
# print(alex.age)
###################################### 反射应用
# 基于字典映射的分发方式

# def check():pass
# def pay():pass
# def withdraw():pass
# data={
#     "check":check,
#     "pay": pay,
#     "withdraw": withdraw,
# }
# action=input(">>>")
# data[action]()


# 基于类反射的分发

class FtpServer(object):
    def run(self):
        print("OK")
        while 1:
            action = input(">>>")
            if hasattr(self, action):
                getattr(self, action)()
            else:
                print("输入参数有误！")
    def put(self):
        print("上传....")
    def download(self):
        print("下载...")
    def remote_handle(self):
        print("远程控制...")


fs=FtpServer()
fs.run()






