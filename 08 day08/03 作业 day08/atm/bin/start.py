#!/usr/bin/env python3
# author:Alnk(李成果)
import os
import sys

base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # 项目目录
print(base_path)
sys.path.insert(0, base_path)  # 添加项目目录到python环境
from atm.core.main import view

# 程序入口，就是这么简单
if __name__ == '__main__':
    view()
