#!/usr/bin/env python3
# author:Alnk(李成果)
from atm.core.login import Login


def outer(name, pwd):  # 装饰器
    def wraper(func):
        def inner(*args, **kwargs):
            login = Login()
            ret = login.login(name, pwd)
            if ret:
                ret2 = func(*args, **kwargs)
                return ret2

        return inner

    return wraper
