#!/usr/bin/env python3
# author:Alnk(李成果)
import os
import sys
from shopping_car.core.login import Login
from shopping_car.core.register import Register
from shopping_car.core.buy import Buy


def view():
    msg = """\n\n---- 欢迎来到老男孩购物商城 ----
        1 注册
        2 登录
        3 购物
        4 退出
    """
    dic = {
        '1': Register().register,
        '2': Login().login,
        '3': Buy().buy,
        '4': quit,
    }
    while 1:
        print(msg)
        keys = input('请输入你要选择的操作序号>>>:')
        if dic.get(keys):
                dic[keys]()
        else:
            print('编号有误')
