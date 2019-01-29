#!/usr/bin/env python3
#author:Alnk(李成果)
import re

# findall()
# ret = re.findall('\d+','h2b3123') # 匹配所有
# print(ret)

# search()
# ret = re.search('\d+','h2b3123')  # 只匹配从左到右的第一个
# print(ret)  # 变量
# print(ret.group())
#
# ret = re.search('\d+','aaaab123')  # 只匹配从左到右的第一个
# if ret:
#     print(ret.group())

# compile() # 节省时间
# '\d+'  --> 正则规则 --> python代码 --> 将字符串按照代码执行匹配
# re.findall('\d+','ahkfgilWIVKJBDKvjgheo')
# re.findall('\d+','ahkfgilsk0194750dfjWIVKJBDKvjgheo')
# re.findall('\d+','ahkfgilsk0vv194750dfjWIVKJBDKvjgheo')
#
# ret = re.compile('\d+')
# ret.findall('ahkfgilWIVKJBDKvjgheo')
# ret.search('ahkfgilsk0194750dfjWIVKJBDKvjgheo')
#
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
# 如何取消分组优先？  ?:


# 练习题
# 匹配标签
#
# s = '<h1>abc</h1>'
# ret = re.search('<(\w+)>', s)
# print(ret.group())
# 分组
# ret = re.search('<(\w+)>(.*?)<(/\w+)>',s)
# print(ret.group(1))
# print(ret.group(2))
# print(ret.group(3))


# s = '<h1>abc</h1>'
# ret = re.search('<(?P<tag>\w+)>(.*?)<(/\w+)>',s)
# print(ret.group('tag'))
# s = '<h1>abc</h1>'
# ret = re.search('<(?P<tag>\w+)>(.*?)</(?P=tag)>',s)
# print(ret)



# 匹配标签
# ret = re.search("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>","<h1>hello</h1>")
# #还可以在分组中利用?<name>的形式给分组起名字
# #获取的匹配结果可以直接用group('名字')拿到对应的值
# print(ret.group('tag_name'))  #结果 ：h1
# print(ret.group())  #结果 ：<h1>hello</h1>
#
# ret = re.search(r"<(\w+)>\w+</\1>","<h1>hello</h1>")
# #如果不给组起名字，也可以用\序号来找到对应的组，表示要找的内容和前面的组内容一致
# #获取的匹配结果可以直接用group(序号)拿到对应的值
# print(ret.group(1))
# print(ret.group())  #结果 ：<h1>hello</h1>
