#!/usr/bin/env python3
# author:Alnk(李成果)
import sys
import os

# 设置环境属性
base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, base_path)

from shopping_car.core.main import view

if __name__ == '__main__':
    view()
