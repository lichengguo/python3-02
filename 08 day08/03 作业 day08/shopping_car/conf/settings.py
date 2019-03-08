#!/usr/bin/env python3
#author:Alnk(李成果)
import os

# 项目目录
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 用户信息存放路径
user_info_path = os.path.join(base_path, 'db')

# 商品列表
goods_info_dict = {
    "1": {"name": "电脑", "price": 1999, },
    "2": {"name": "鼠标", "price": 10, },
    "3": {"name": "键盘", "price": 60, },
    "4": {"name": "手机", "price": 4000, },
    "5": {"name": "ipad", "price": 2999, },
    "n": {"name": "购物车结算", "price": '', },
    "q": {'name': "退出", "price": '',},
}
