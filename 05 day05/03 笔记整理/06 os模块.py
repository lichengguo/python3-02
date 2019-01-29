#!/usr/bin/env python3
#author:Alnk(李成果)
# import os
# os和操作系统打交道的

# 和文件、文件夹相关的
# os.makedirs('dirname1/dirname2')    # 可生成多层递归目录
# os.removedirs('dirname1/dirname2')    # 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
# os.mkdir('dirname')    # 生成单级目录；相当于shell中mkdir dirname
# os.rmdir('dirname')    # 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
# ret = os.listdir(r'E:\python3周末班2期笔记\05 day05\03 笔记整理')
#  列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
# print(ret)
# os.remove('test.py')  # 删除一个文件
# os.rename("test.py","test2.py")  # 重命名文件/目录
# ret = os.stat(r'E:\python3周末班2期笔记\05 day05\03 笔记整理')  # 获取文件/目录信息
# print(ret)


# 和执行系统命令相关
# os.system("dir")  # 运行shell命令，直接显示
# ret = os.popen('dir').read()  # 运行shell命令，获取执行结果
# print(ret)
# ret = os.getcwd() # 获取当前工作目录，即当前python脚本工作的目录路径
# print(ret)
# os.chdir(r"E:\python3周末班2期笔记")  # 改变当前脚本工作目录；相当于shell下cd
# ret = os.getcwd()
# print(ret)
# 所谓工作目录 文件在哪个目录下运行 工作目录就是哪里
# 和这个文件本身所在的路径没有关系
# 1.工作目录与文件所在位置无关
# 2.工作目录和所有程序中用到的相对目录都相关

# 和路径相关的
# os.path
# ret = os.path.abspath(__file__) # 返回path规范化的绝对路径
# print(ret)
# ret = os.path.split(__file__) # 将path分割成目录和文件名二元组返回
# print(ret)
# os.path.dirname(path) # 返回path的目录。其实就是os.path.split(path)的第一个元素
# os.path.basename(path) # 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
# ret = os.path.exists(r'E:\python')  # 如果path存在，返回True；如果path不存在，返回False
# print(ret)
# ret = os.path.isabs('E:\python3周末班2期笔记\05 day05\03 笔记整理')  # 如果path是绝对路径，返回True
# print(ret)
# ret = os.path.isfile('E:\python3周末班2期笔记\05 day05\03 笔记整理')  # 如果path是一个存在的文件，返回True。否则返回False
# print(ret)
# ret = os.path.isdir('E:\python3周末班2期笔记')  # 如果path是一个存在的目录，则返回True。否则返回False
# print(ret)
# ret = os.path.join('E:\python3周末班2期笔记', 'abc', 'def')  # 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
# print(ret)
# os.path.getatime(path)  返回path所指向的文件或者目录的最后访问时间
# os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间
# ret = os.path.getsize(r'E:\python3周末班2期笔记\05 day05\03 笔记整理\00 今日课程大纲.py')
#  返回path的大小,文件夹的大小不准确
# print(ret)


# 练习题
# 使用python代码 计算文件夹的大小
# 这个文件夹里可能还有文件夹
# import os
# total_size=0
# def file_size(path):
#     global total_size
#     path=os.path.abspath(path)
#     print('path',path)
#     file_list=os.listdir(path)
#     print('list',file_list)
#     for i in file_list:
#         i_path = os.path.join(path, i)
#         if os.path.isfile(i_path):
#             total_size += os.path.getsize(i_path)
#         else:
#             try:
#                 file_size(i_path)
#             except RecursionError:
#                 print('递归操作时超出最大界限')
#     return total_size
#
# print(file_size(r'E:\02'))