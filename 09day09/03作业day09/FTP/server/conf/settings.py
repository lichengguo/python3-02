#!/usr/bin/env python3
#author:Alnk(李成果)
import os

# IP,PORT
IP = '127.0.0.1'
PORT = 8100

# db目录
base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_base = os.path.join(base, 'db')

# db/info/user_info.json目录
user_info_base = os.path.join(db_base, 'user_info')
user_info_file = os.path.join(user_info_base, 'user_info.json')

