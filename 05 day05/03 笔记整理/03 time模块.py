#!/usr/bin/env python3
#author:Alnk(李成果)

# 和时间打交道的模块
import time

# 1.时间戳时间 time.time()
# print(time.time())
# 1548645816.011941 时间戳格式
# float 小数
# 为什么时间要用这种格式(1548558746.5218766)表示？
    # 是给计算机看的
# '2019/1/27 11:13'
# 1970 1 1 0:0:0 英国伦敦的时间 0时区
# 1970 1 1 8:0:0 北京的时间 东8区


# 2.格式化时间 time.strftime('%Y-%m-%d %H:%M:%S')
# t1 = time.strftime('%Y-%m-%d %H:%M:%S')
# t1 = time.strftime('%Y+%m+%d %H:%M:%S %a')
# t1 = time.strftime('%Y+%m+%d %H:%M:%S %A %b %B')
# t1 = time.strftime('%y+%m+%d %H:%M:%S %A %b %B')
# t1 = time.strftime('%c')
# print(t1)


# 3.结构化时间（时间元组） time.localtime()
# print(time.localtime())
# tm_year=2019 --- 年
# tm_mon=1   ---月
# tm_mday=28,   ---日
# tm_hour=11,  ---时
# tm_min=33,  ---分
# tm_sec=1,   ---秒
# tm_wday=0,  --- 一周的第几天，星期一为0
# tm_yday=28,  ---  一年的第几天
# tm_isdst=0  --- 是否是夏令时，默认不是


# 转换只能通过结构化时间进行转换 ：时间戳格式 <---> 结构化时间 <---> 格式化时间
# 1548558746.5218766                        '2019/1/27 11:13'
#   计算机能看懂的    (为了进行数据转换)    人能看懂的
#   时间戳时间         结构化时间           格式化时间
#   time.time()       time.localtime()      time.strftime('%Y-%m-%d %H:%M:%S')


# 举例1
# 格式化时间 2018-8-8  ---> 时间戳时间
# 先把格式化时间 转化成 元组时间
# str_time = '2018-8-8'
# struct_time = time.strptime(str_time, '%Y-%m-%d')
# print(struct_time)
# # 在转化成时间戳
# stamp_time = time.mktime(struct_time)
# print(stamp_time)

# 举例2
# 2000000000 转化为格式化时间
# stamp_t = 2000000000
# # 先把时间戳时间转化为元组时间
# struct_t = time.localtime(stamp_t)
# print(struct_t)
# # 再把元组时间转为格式化时间
# strftime_t = time.strftime('%Y-%m-%d %H:%M:%S', struct_t)
# print(strftime_t)

# 小练习1
# 拿到本月时间1号的时间戳时间
# strftime_t = time.strftime('%Y-%m')
# print(strftime_t)
# struct_t = time.strptime(strftime_t, '%Y-%m')
# print(struct_t)
# stamp_t = time.mktime(struct_t)
# print(stamp_t)

# 小练习2
# '2017-09-11 08:30:00' '2017-09-12 11:00:00' 计算这两个时间段的时间差
# 先把格式化时间--->元组时间
t1 = time.mktime(time.strptime('2017-09-11 08:30:00', '%Y-%m-%d %H:%M:%S'))
t2 = time.mktime(time.strptime('2017-09-12 11:00:00', '%Y-%m-%d %H:%M:%S'))
ret = t2 - t1
struct_t = time.gmtime(ret)
print(struct_t)
print('过去了%d年%d月%d天%d小时%d分钟%d秒'%(struct_t.tm_year-1970,struct_t.tm_mon-1,
                                 struct_t.tm_mday-1,struct_t.tm_hour,
                                 struct_t.tm_min,struct_t.tm_sec))
