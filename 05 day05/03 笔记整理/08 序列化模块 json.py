#!/usr/bin/env python3
#author:Alnk(李成果)

# 序列化模块
# 序列化
# 序列 ： list str tuple bytes
# 可迭代的都是序列？ 字典？集合？无序的，散列。不是序列
# 狭义的序列 ：str / bytes
# 序列化？把。。。变得有序，把。。。变成str或者是bytes
# 反序列化？把str/bytes 还原回原来的 。。。

# 为什么要有序列化？
# 1.存储在文件中 长久保存到硬盘
# 2.在网络上传递，只能用字节

# 序列化模块
import json
# 能够支持所有的计算机高级语言
# 对数据类型的要求非常严格
# dic = {"key":"value"}
# ret = json.dumps(dic)   # 序列化方法
# print(dic,type(dic))
# print(ret,type(ret))
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
#
# dump load
# dic = {"key":"value"}
# with open('json_file2','w') as f:
#     json.dump(dic,f)
#
# with open('json_file2') as f:
#     ret = json.load(f)
# print(ret['key'])


# json不可以dump多次
# dic = {"key":"value"}
# with open('json_file2','w') as f:
#     json.dump(dic,f)
#     json.dump(dic,f)
#
# with open('json_file2', 'r') as f:
#     ret = json.load(f)


# 如果需要dump多次，按照下面的方法
# str_dic = {"name": "alex","sex":None}
# ret = json.dumps(str_dic)
# with open('json_file2','w') as f:
#     f.write(ret+'\n')
#     f.write(ret+'\n')
#
# with open('json_file2', 'r') as f:
#     for line in f:
#         print(json.loads(line), type(json.loads(line)))

