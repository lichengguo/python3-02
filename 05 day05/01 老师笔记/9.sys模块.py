# -*- coding: utf-8 -*-
# @Time    : 2019/1/27 15:16
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 9.sys模块.py
# @Software: PyCharm

# sys模块是和 python解释器打交道的
import sys
# sys.exit()
# print(123)
# print(sys.version)
# print(sys.platform)  # 平台 操作系统

# print(sys.path)  # 模块搜索路径
# 包含的内容
# 1.内置的python安装的时候就规定好的一些内置模块所在的路径
    # 内置模块
    # 扩展模块
# 2.当前被执行的文件所在的路径
    # 自定义的模块

# python py文件的目录 参数1 参数2
# print(sys.argv)   # []
# if sys.argv[1] == 'alex' and sys.argv[2] == 'alexsb':
#     print('登陆成功')
# else:
#     print('登陆失败')
#     sys.exit()
# print('登陆成功后的所有代码')