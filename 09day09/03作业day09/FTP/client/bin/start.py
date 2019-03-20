#!/usr/bin/env python3
#author:Alnk(李成果)
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.main import FTPClient


if __name__ == '__main__':
    name = input('账号>>>')
    pwd = input('密码>>>')
    fc = FTPClient(name, pwd)
    fc.run()
