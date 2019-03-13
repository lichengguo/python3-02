#!/usr/bin/env python3
# author:Alnk(李成果)
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.main import FTPClient
from conf.settings import IP, PORT

# 程序入口
if __name__ == "__main__":
    name = input('输入账号>>>')
    pwd = input('输入密码>>>')
    fc = FTPClient(IP, PORT, name, pwd)
    fc.run()

