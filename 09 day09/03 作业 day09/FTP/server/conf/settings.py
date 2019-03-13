#!/usr/bin/env python3
#author:Alnk(李成果)
import os
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 服务器监听的ip和port
IP = '127.0.0.1'
PORT = 8899

# db目录
db_path = os.path.join(base_path, 'db')
# 用户信息登录文件
user_info_path = os.path.join(db_path, 'user_info.json')