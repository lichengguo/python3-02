# -*- coding: utf-8 -*-
# @Time    : 2019/1/27 11:11
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 5.time模块.py
# @Software: PyCharm

# 和时间打交道的模块
import time

# print(time.time())
# 1548558746.5218766  时间戳格式
# float 小数
# 为什么时间要用这种格式(1548558746.5218766)表示？
    # 是给计算机看的
# '2019/1/27 11:13'
# 1970 1 1 0:0:0 英国伦敦的时间 0时区
# 1970 1 1 8:0:0 北京的时间 东8区

# 1548558746.5218766     '2019/1/27 11:13'
#   计算机能看懂的        人能看懂的
#   时间戳时间            格式化时间
#   time.time()           time.strftime('%Y-%m-%d %H:%M:%S')

# t1 = time.strftime('%Y-%m-%d %H:%M:%S')
# t1 = time.strftime('%Y+%m+%d %H:%M:%S %a')
# t1 = time.strftime('%Y+%m+%d %H:%M:%S %A %b %B')
# t1 = time.strftime('%y+%m+%d %H:%M:%S %A %b %B')
# t1 = time.strftime('%c')
# print(t1)

# t1 = time.strftime('%Y-%m-%d %H:%M:%S')
# '%s,%s'%(1,2)

# 1548558746.5218766                        '2019/1/27 11:13'
#   计算机能看懂的    (为了进行数据转换)    人能看懂的
#   时间戳时间         结构化时间           格式化时间
#   time.time()       time.localtime()      time.strftime('%Y-%m-%d %H:%M:%S')

# print(time.localtime())


# 2018-8-8  --> 时间戳时间
# str_time = '2018-8-8'
# struct_time = time.strptime(str_time,'%Y-%m-%d')
# print(struct_time)
# stamp_time = time.mktime(struct_time)
# print(stamp_time)

# print(time.time())
# 2000000000
# struct_time = time.localtime(3000000000)
# print(struct_time)
# str_t = time.strftime('%y-%m-%d %H:%M:%S',struct_time)
# print(str_t)

# 拿到本月时间1号的时间戳时间
# now_str = time.strftime('%Y-%m')
# print(now_str)
# struct_time = time.strptime(now_str+'-01 老师笔记','%Y-%m-%d')
# print(struct_time)
# 时间戳时间
# stamp_t = time.mktime(struct_time)
# print(stamp_t)















