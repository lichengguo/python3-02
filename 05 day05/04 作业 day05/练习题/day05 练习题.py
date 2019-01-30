#!/usr/bin/env python3
#author:Alnk(李成果)

# 1、计算两个格式化时间之间差了多少年月日时分秒
# 例如 '1997-10-1 08:00:00' 和 '1997-10-2 09:00:00'
# import time
# def diff_time(t1, t2):
#     t1_struct = time.strptime(t1,'%Y-%m-%d %H:%M:%S')
#     t1_stamp = time.mktime(t1_struct)
#     t2_struct = time.strptime(t2,'%Y-%m-%d %H:%M:%S')
#     t2_stamp = time.mktime(t2_struct)
#     if t1_stamp > t2_stamp:
#         diff_t = t1_stamp - t2_stamp
#     else:
#         diff_t = t2_stamp - t1_stamp
#     diff_t_struct = time.gmtime(diff_t)
#     print('两个时间相差了 [%s]年 [%s]月 [%s]日 [%s]时 [%s]分 [%s]秒'
#           % (diff_t_struct.tm_year-1970, diff_t_struct.tm_mon-1,
#              diff_t_struct.tm_mday-1, diff_t_struct.tm_hour,
#              diff_t_struct.tm_min, diff_t_struct.tm_sec))
#
#
# t1 = '1997-10-1 08:00:00'
# t2 = '1997-10-2 09:00:00'
# diff_time(t1, t2)



# 2、计算当前时间所在月1号的时间戳
# import time
# def get_time():
#     now_t = time.strftime('%Y-%m')
#     uct_t = time.strptime(now_t, '%Y-%m')
#     stamp_t = time.mktime(uct_t)
#     return stamp_t
#
# ret = get_time()
# print(ret)



# 3、生成一个6位随机验证码(包含数字和大小写字母)
# import random
# def get_code(n=6, flag=True):
#     code = ''
#     for i in range(n):
#         selectd = random.randint(0,9)
#         if flag:
#             alp = random.randint(65,90)
#             selectd = random.choice([selectd, chr(alp)])
#         code += str(selectd)
#     return code
#
#
# ret = get_code()
# print(ret)



# 4、发红包、制定金额和个数，随机分配红包金额
# import random
# def get_hb(num, cash):
#     # 存储随机分配的红包
#     lst = []
#     # 乘以100是为了方便随机取值，添加到列表的时候会除以100
#     cash = cash * 100
#     for i in range(num-1):
#         # 随机获取红包金额
#         ret = random.randint(1, cash-1*(num-1-i)) # 这里是为了不让出现0元红包，红包最小为0.01元
#         lst.append(ret/100)
#         cash -= ret
#     else:
#         lst.append(cash/100)
#     return lst
#
#
# ret = get_hb(5, 0.06)
# print(ret)



# 5、分别列出给定目录下所有的文件和文件夹
# import os
#
# def lis_file_path(path):
#     dir_list = []
#     file_list = []
#     # 拼接路径
#     ret_list = os.listdir(r'%s' % path)
#     for i in ret_list:
#         ret = os.path.join(path + '/%s' % i)
#         if os.path.isfile(ret):
#             file_list.append(i)
#         elif os.path.isdir(ret):
#             dir_list.append(i)
#     return dir_list,file_list
#
#
# ret = lis_file_path(r'E:\python3周末班2期笔记\05 day05\04 作业 day05\练习题')
# print('目录:', ret[0])
# print('文件:', ret[1])



# 6、获取当前文件所在目录
# import os
# ret = os.path.abspath(__file__)
# print(os.path.dirname(ret))



# 7、在当前目录下创建一个文件夹、在这个文件夹下创建一个文件
# import os
# def mk():
#     # 获取被运行的PY文件绝对目录
#     now_abs_dir = os.path.dirname(os.path.abspath(__file__))
#     # 拼接路径
#     ret_dir = os.path.join(now_abs_dir + '/new_dir')
#     # 创建一个文件夹
#     os.mkdir(ret_dir)
#     # 拼接路径
#     ret_file = os.path.join(ret_dir + '/test.txt')
#     # 创建一个文件
#     with open(r'%s' % ret_file, encoding='utf-8', mode='w') as f:
#         f.write(ret_file + '\n')
#
#
# mk()



# 8、计算某路径下所有文件和文件夹的总大小
# import os
# # 文件总大小
# total_size = 0
#
# def lis_file_path(path):
#     global total_size
#     # 获取指定目录下的文件和子目录，返回一个列表
#     ret_list = os.listdir(r'%s' % path)
#     for i in ret_list:
#         # 拼接路径
#         ret = os.path.join(path + '/%s' % i)
#         # 如果是文件夹继续递归
#         if os.path.isdir(ret):
#             lis_file_path(ret)
#          # 如果是文件就直接计算大小，算入总值
#         elif os.path.isfile(ret):
#             size = os.path.getsize(ret)
#             total_size += size
#     return total_size
#
#
# ret = lis_file_path(r'E:\python3周末班2期笔记')
# print(ret)