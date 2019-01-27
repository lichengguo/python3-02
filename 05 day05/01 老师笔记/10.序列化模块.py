# -*- coding: utf-8 -*-
# @Time    : 2019/1/27 15:35
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 10.序列化模块.py
# @Software: PyCharm

# 序列化模块
# 序列化
# 序列 ： list str tuple bytes
# 可迭代的都是序列？ 字典？集合？
# 狭义的序列 ：str / bytes
# 序列化？把。。。变得有序，把。。。变成str或者是bytes
# 反序列化？把str/bytes 还原回原来的 。。。

# 为什么要有序列化？
# 字典
# d = {'k':'v'}
# 文件存储 ：字节
# ''.encode('utf-8')
# b''.decode('utf-8')

# 1.存储在文件中
# 2.在网络上传递
# {'cardid':kshkahgkj,'username':'sjkdhajghd','aim':sajgjdgjg,'price':100}


# 序列化模块
# json
# 能够支持所有的计算机高级语言
# 对数据类型的要求非常严格
import json
# dic = {"key":"value"}
# ret = json.dumps(dic)   # 序列化方法
# print(dic,type(dic))
# print(ret,type(ret))
# # ret['key'] 错误
# with open('json_file','w') as f:
#     f.write(ret)

# with open('json_file') as f:
#     content = f.read()
# d = json.loads(content)    # 反序列化方法
# print(d)
# print(d['key'])

# 坑1：json格式规定所有的key必须是字符串数据类型
# dic = {1:2}
# ret = json.dumps(dic)
# print(dic[1])
# print(ret)
# new_dic = json.loads(ret)
# print(new_dic)

# 坑2 ： json中的所有tuple都会被当作list处理
# dic = {1:(1,2,3)}
# ret = json.dumps(dic)
# print(ret)
# new_dic = json.loads(ret)
# print(new_dic)

# dic = {(1,2):(1,2,3)}
# ret = json.dumps(dic)
# print(ret)
# new_dic = json.loads(ret)
# print(new_dic)

# 特性3： json能支持的数据类型非常有限，字符串 数字 列表 字典

# dumps loads   字符串 和 其他基础数据类型之间转换
# dump  load    文件   和 其他基础数据类型之间转换
# dic = {"key":"value"}
# with open('json_file2','w') as f:
#     json.dump(dic,f)

# with open('json_file2') as f:
#     ret = json.load(f)
# print(ret['key'])

# json
# json不可以dump多次
# dic = {"key":"value"}
# with open('json_file2','w') as f:
#     json.dump(dic,f)
#     json.dump(dic,f)

# str_dic = {"name": "alex","sex":None}
# ret = json.dumps(str_dic)
# with open('json_file2','w') as f:
#     f.write(ret+'\n')

# pickle
# 1.支持几乎所有python中的数据类型
# 2.只在python语言中通用
# 3.pickle适合bytes类型打交道的
import pickle
s = {1,2,3,4}
s = {1:2,3:4}
s = {(1,2,3):2,3:4}
# result = pickle.dumps(s)
# print(result)
# with open('pickle_file','wb') as f:
#     f.write(result)
# new_s = pickle.loads(result)
# print('new_s :',new_s)

# with open('pickle_file','rb') as f:
#     content = f.read()
# ret = pickle.loads(content)
# print(ret,type(ret))

# pickle 可以支持多个对象放入文件
# s1 = {1,2,3}
# s2 = {1:2,3:4}
# s3 = ['k','v',(1,2,3),4]
# with open('pickle_file2','wb') as f:
#     pickle.dump(s1,f)
#     pickle.dump(s2,f)
#     pickle.dump(s3,f)

# with open('pickle_file2','rb') as f:
#     count = 1
#     while count <= 3:
#         try:
#             content = pickle.load(f)
#             print(content)
#             count += 1
#         except EOFError:
#             break


# json
# 如果你是要跨平台沟通，那么推荐使用json
# key只能是字符串
# 不能多次load和dump
# 支持的数据类型有限

# pickle
# 如果你是只在python程序之间传递消息，并且要传递的消息是比较特殊的数据类型
# 处理文件的时候 rb/wb
# 支持多次dump/load