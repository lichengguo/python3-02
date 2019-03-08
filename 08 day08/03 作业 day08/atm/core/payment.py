#!/usr/bin/env python3
# author:Alnk(李成果)
import os
from atm.conf import settings
from atm.core.decorator import outer
from atm.core.basic import Basic
from atm.core.log import get_logger
from atm.core.login import Login


class PayMent(Login):  # 支付功能

    def payment(self, cash):
        ret = self.login()  # 获取登录返回值
        if ret == False:
            return 0  # 账号或密码错误
        else:
            self.name = ret['name']
        file_path = os.path.join(settings.user_info_path, '%s.json' % self.name)  # 用户文件路径
        user_dict = self.read_dict(file_path)  # 获取用户详细信息
        if cash <= user_dict['available_quota']:
            user_dict['available_quota'] -= cash
            self.write_dict(user_dict, file_path)  # 写入文件
            log_file = os.path.join(settings.log_path, '%s.log' % self.name)
            log_msg = '通过第三方支付[%s]元' % cash
            get_logger(log_file, log_msg)
            return 2 # 支付成功
        else:
            return 1 # 额度不够
