#!/usr/bin/env python3
# author:Alnk(李成果)
import os
from atm.conf import settings
from atm.core.decorator import outer
from atm.core.basic import Basic
from atm.core.log import get_logger


class PayMent(Basic):  # 支付功能
    name = input('输入银行卡号>>>')
    pwd = input('输入密码密码>>>')

    def __init__(self):
        pass

    @outer(name, pwd)
    def payment(self, cash):
        file_path = os.path.join(settings.user_info_path, '%s.json' % self.name)  # 用户文件路径
        user_dict = self.read_dict(file_path)  # 获取用户详细信息
        if cash <= user_dict['available_quota']:
            user_dict['available_quota'] -= cash
            self.write_dict(user_dict, file_path)  # 写入文件
            log_file = os.path.join(settings.log_path, '%s.log' % self.name)
            log_msg = '通过第三方支付[%s]元' % cash
            get_logger(log_file, log_msg)
            return True
        else:
            return '余额不够,支付失败！'
