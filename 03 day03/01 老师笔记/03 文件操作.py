# -*- coding: utf-8 -*-
# @Time    : 2019/1/13 10:37
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 03 文件操作.py
# @Software: PyCharm
# f1 = open(r'd:\美女护士空姐联系方式.txt', encoding='utf-8', mode='r')
# content = f1.read()
# print(content)
# f1.close()
"""
f1 f f_h file_handler 变量,文件句柄。
open 内置函数 底层调用的操作系统的操作文件功能的接口。
windows: 默认编码gbk，linux utf-8  ios: utf-8. 
操作文件总共3步；
1，打开文件，产生文件句柄。
2，对文件句柄进行操作。
3，关闭文件句柄。
"""
# 错误示范：
# 1，UnicodeDecodeError: 'gbk' codec can't decode... 编解码错误。
# 2,路径错误。路径分隔符 与后面的字符产生特殊的意义。 解决方式 r 或者 \

# 绝对路径：从根目录开始。
# 相对路径：同一个工作目录（文件夹）下。
# f1 = open('log', encoding='utf-8', mode='r')
# content = f1.read()
# print(content)
# f1.close()

# 第一 读（r rb r+ r+b）
# r模式
# 默认就是r模式
# 1.1 read()
# f1 = open('log', encoding='utf-8',)
# content = f1.read()
# print(content,type(content))
# 1.2 read(n)
# r模式下,n代表字符。
# f1 = open('log', encoding='utf-8',)
# content = f1.read(3)
# print(content)
# 1.3 readline() 按行读取
# f1 = open('log', encoding='utf-8',)
# print(f1.readline().strip())
# print(f1.readline().strip())
# f1.close()
# 1.4 readlines()  返回一个列表,列表里面的元素是原文件每一行
# f1 = open('log', encoding='utf-8',)
# content = f1.readlines()
# print(content)
# f1.close()
# 1.5 for循环
# f1 = open('log', encoding='utf-8',)
# for line in f1:  # ['老男孩教育是最好的培训学校\n', '太白金星是最好的司机，老师\n', '深圳分校\n', '上海分校\n', '北京校区']
#     print(line.strip())
# f1.close()

# rb模式
# f1 = open('log', mode='rb')
# content = f1.read()
# print(content.decode('utf-8'))
# f1.close()

# f1 = open('log', mode='rb')
# content = f1.read()
# print(content)
# f1.close()

# r+ 读写
# f = open('log',encoding='utf-8',mode='r+')
# print(f.read())
# f.write('666')
# f.close()

# 先读后写会出问题
# f = open('log',encoding='utf-8',mode='r+')
# f.write('松岛岛')
# print(f.read())
# f.close()



# 第二写模式
# w
# 没有文件创建文件写入内容，有文件，先清空内容后写入。
# f = open('log1',encoding='utf-8',mode='w')
# # f.write('林志玲 fjdsklafjsd;flj太白金星')
# f.write('深圳校区 ~~~')
# f.write('深圳校区 ~~~')
# f.write('深圳校区 ~~~')
# f.write('深圳校区 ~~~')
# f.write('深圳校区 ~~~')
# f.close()




# wb
# f1 = open('timg.jpg', mode='rb')
# content = f1.read()
# # print(content)
#
#
# f2 = open('time1.jpg',mode='wb')
# f2.write(content)
# f2.close()


# w+ 写读
# f = open('log1',encoding='utf-8',mode='w+')
# f.write('老男孩教育...')
# f.seek(0)
# print(f.read())
# f.close()





# a 追加
# 没有文件创建文件追加内容，有文件，在文件最后追加内容。
# f = open('log3',encoding='utf-8',mode='a')
# f.write('老男孩')
# f.close()

# 其他操作方法：
# readable() writable()  ***
# seek 调整光标位置 按照字节   ***
# seek(0)  将光标移动到开始
# seek(0，2)  将光标移动到最后。
# tell 获取光标位置 按照字节。  ***
# flush 刷新 保存  ***
# truncate
# f = open('log3',encoding='utf-8')
# f.seek(1)
# print(f.read())
# print(f.tell())
# f.seek(0) # 将光标移动到开始
# f.seek(0,2)  # 将光标移动到最后。

# print(f.read())
# print(f.writable())
# if f.writable():
#     f.write('111')
# f.close()

# f = open('log3',encoding='utf-8',mode='w')
# f.write('fjdsklafjdfjksa')
# f.flush()
# f.close()

# f = open('log3',encoding='utf-8',mode='r+')
# f.truncate(3)
# f.close()
#文件的改
'''
1,以读的模式打开原文件。
2，以写的模式打开新文件。
3，读取原文件对源文件内容进行修改形成新内容写入新文件。
4，将原文件删除。
5，将新文件重命名成原文件。
'''

# with open('log1',encoding='utf-8') as f1:
#     print(f1.read())

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

# 方法二：
import os

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

#
# s1 = '太白'
# print(s1.replace('alex','sb'))