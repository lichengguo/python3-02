#!/usr/bin/env python3
#author:Alnk(李成果)
import os
from atm.conf import settings
from atm.core.decorator import outer
from atm.core.basic import Basic


class PayMent(Basic):
    name = input('输入银行卡号>>>')
    pwd = input('输入密码密码>>>')

    def __init__(self):
        pass

    @outer(name,pwd)
    def payment(self, cash):
        file_path = os.path.join(settings.user_info_path, '%s.json' % self.name)
        user_dict = self.read_dict(file_path)
        print('user_dict', user_dict)
        print('付款')
        print('cash',cash)
        return True
