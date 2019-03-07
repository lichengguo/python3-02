#!/usr/bin/env python3
# author:Alnk(李成果)
import os

# 程序目录
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 用户数据库目录与文件
db_path = os.path.join(base_path, 'db')  # 数据库目录
user_info_path = os.path.join(db_path, 'user_info')  # 用户信息目录

# 日志目录
log_path = os.path.join(base_path, 'log')
admin_log_path = os.path.join(log_path, 'admin.log')  # admin管理员日志文件

# 提现手续费
service_charge = 0.05
