# -*- coding: utf-8 -*-
# @Time    : 2019/1/27 12:09
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 7.os模块.py
# @Software: PyCharm

# os和操作系统打交道的
import os
# os.mkdir(r'D:\太白金星\周末班\day05视频与课上笔记\day05\new')
# os.makedirs(r'D:\太白金星\周末班\day05视频与课上笔记\day05\dir1\dir2')
# os.makedirs(r'dir1\dir2\dir3\dir4')
# os.removedirs(r'dir1\dir2\dir3\dir4')
# lst = os.listdir(r'D:\太白金星\周末班')
# print(lst)
# st = os.stat(r'D:\太白金星\周末班\tmp')
# print(st)

# os.system('dir')
# ret = os.popen('dir')
# s = ret.read()

# print('--->',os.getcwd())  # 获取当前工作目录
# D:\太白金星\周末班\day05视频与课上笔记\day05
# 所谓工作目录 文件在哪个目录下运行 工作目录就是哪里
# 和这个文件本身所在的路径没有关系
# open('tmp_new','w').close()  # 这个相对目录是相对工作目录而言的

# os.chdir(r'D:\太白金星\周末班\day05视频与课上笔记\day05')
# open('tmp_new2','w').close()

# 1.工作目录与文件所在位置无关
# 2.工作目录和所有程序中用到的相对目录都相关

# print(__file__)
# ret = os.path.dirname(__file__)
# ret2 = os.path.basename(__file__)
# ret3 = os.path.basename('D:/太白金星/周末班/day05视频与课上笔记')
# ret4 = os.path.split('D:/太白金星/周末班/day05视频与课上笔记')
# print(ret,ret2)
# print(ret3)
# print(ret4)
# print(os.path.abspath('tmp_new3'))
# a = 'day05'
# ret = os.path.join('D:\太白金星\周末班\day05视频与课上笔记',a,'123')
# print(ret)

# size = os.path.getsize(r'D:\太白金星\周末班\day05视频与课上笔记\day05\7.os模块.py')
# size2 = os.path.getsize(r'D:\太白金星\周末班\day05视频与课上笔记\day05\5.time模块.py')
# print(size)
# print(size2)
# dir_size1 = os.path.getsize('D:\太白金星\周末班\day05视频与课上笔记\day05')
# print(dir_size1)

# 使用python代码 计算文件夹的大小
# 这个文件夹里可能还有文件夹


# 两个时间之间差了多久
# 时间戳相减 ：30天为一个月
# 时分秒
# 年月日