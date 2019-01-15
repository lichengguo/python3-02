#!/usr/bin/env python3
#author:Alnk(李成果)
'''
文件的修改：所有的文件编辑器都要经过下面这5步才能对文件进行修改
    1,以读的模式打开原文件
    2，以写的模式打开新文件
    3，读取原文件对源文件内容进行修改形成新内容写入新文件
    4，将原文件删除
    5，将新文件重命名成原文件
'''
# 方法一 小文件可以。
# import os
#
# # 1,以读的模式打开原文件。
# # 2，以写的模式打开新文件。
# with open('alex个人简历',encoding='utf-8') as f1,\
#         open('alex个人简历.bak',encoding='utf-8',mode='w') as f2:
#     # 3，读取原文件对源文件内容进行修改形成新内容写入新文件。
#     old_content = f1.read()
#     new_content = old_content.replace('alex','SB')
#     f2.write(new_content)
#
# # 4，将原文件删除。
# os.remove('alex个人简历')
# # 5，将新文件重命名成原文件。
# os.rename('alex个人简历.bak','alex个人简历')


# 方法二： 推荐使用这种方法
import os
#
# 1,以读的模式打开原文件。
# 2，以写的模式打开新文件。
# with open('alex个人简历',encoding='utf-8') as f1,\
#         open('alex个人简历.bak',encoding='utf-8',mode='w') as f2:
#     # 3，读取原文件对源文件内容进行修改形成新内容写入新文件。
#     for old_line in f1:
#         new_line = old_line.replace('SB','alex')
#         f2.write(new_line)
#
# # 4，将原文件删除。
# os.remove('alex个人简历')
# # 5，将新文件重命名成原文件。
# os.rename('alex个人简历.bak','alex个人简历')