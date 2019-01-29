#!/usr/bin/env python3
#author:Alnk(李成果)

import pickle

# 1.支持几乎所有python中的数据类型
# 2.只在python语言中通用
# 3.pickle适合bytes类型打交道的
# s = {1,2,3,4}
# ret = pickle.dumps(s)
# print(ret)
#
# ret2 = pickle.loads(ret)
# print(ret2)


# pickle：序列化时候数据是什么类型，反序列化以后数据还是原来的类型，这点和 json 有点不一样
# d = {1:2,3:4}
# ret = pickle.dumps(d)
# print(ret)
# new_d = pickle.loads(ret)
# print(new_d)
#
# s = {(1,2,3):2,3:4}
# result = pickle.dumps(s)
# print(result)
# with open('pickle_file','wb') as f:
#     f.write(result)
#
# with open('pickle_file','rb') as f:
#     content = f.read()
# ret = pickle.loads(content)
# print(ret,type(ret))


# pickle 可以支持多个对象放入文件
# pickle 可以dump多次，也可以load多次
# s1 = {1,2,3}
# s2 = {1:2,3:4}
# s3 = ['k','v',(1,2,3),4]
# with open('pickle_file2','wb') as f:
#     pickle.dump(s1,f)
#     pickle.dump(s2,f)
#     pickle.dump(s3,f)
#
# with open('pickle_file2','rb') as f:
#     count = 1
#     while count <= 3:
#         try:
#             content = pickle.load(f)
#             print(content)
#             count += 1
#         except EOFError:
#             break


# json      ---实际上使用json更多。优先选择
# 如果你是要跨平台沟通，那么推荐使用json
# key只能是字符串
# 不能多次load和dump
# 支持的数据类型有限

# pickle
# 如果你是只在python程序之间传递消息，并且要传递的消息是比较特殊的数据类型
# 处理文件的时候 rb/wb
# 支持多次dump/load