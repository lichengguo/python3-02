#!/usr/bin/env python3
#author:Alnk(李成果)
# 第二写模式
# w 写模式
# 没有文件，创建文件写入内容
# 有文件，先清空内容后写入
# f = open('log1',encoding='utf-8',mode='w')
# # f.write('林志玲 fjdsklafjsd;flj太白金星')
# f.write('深圳校区 ~~~')
# f.write('深圳校区 ~~~')
# f.write('深圳校区 ~~~')
# f.write('深圳校区 ~~~')
# f.write('深圳校区 ~~~')
# f.close()

# wb 写模式(以bytes类型写入到文件)
#rb
# f1 = open('time1.jpg', mode='rb')
# content = f1.read()
# print(content)
# f1.close()
# #wb 写入到文件
# #把bytes类型写入到文件 --图片
# f2 = open('time2.jpg',mode='wb')
# f2.write(content)
# f2.close()

# w+ 写读模式
# f = open('log1',encoding='utf-8',mode='w+')
# f.write('老男孩教育...')
# f.seek(0)   #调整光标（指针）到最开始
# print(f.read())
# f.close()

#wb+ 写读模式(bytes)