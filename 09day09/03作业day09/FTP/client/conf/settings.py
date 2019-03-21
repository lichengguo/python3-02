#!/usr/bin/env python3
#author:Alnk(李成果)
import os

# IP,PORT
IP = '127.0.0.1'
PORT = 8100

# client目录
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# db 目录
db_path = os.path.join(base_path, 'db')
