#!/usr/bin/env python3
# author:Alnk(李成果)
from atm.core.admin import Admin
from atm.core.login import Login
from atm.core.user import User


def view():  # 功能分发
    l = Login()
    ret = l.login()
    if ret:
        if ret['role'] == 'admin':
            a = Admin(ret['name'])
            a.run()
        elif ret['role'] == 'user':
            u = User(ret['name'])
            u.run()
