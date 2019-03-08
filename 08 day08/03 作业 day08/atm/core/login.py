#!/usr/bin/env python3
# author:Alnk(李成果)
import os
from atm.conf.settings import user_info_path, log_path
from atm.core.basic import Basic
from atm.core.log import get_logger

class Login(Basic):  # 认证类

    def login(self, name=None, pwd=None):
        if name==None and pwd==None:
            name = input('卡号用户名>>>')
            pwd = input('密码>>>')
        file_path = os.path.join(user_info_path, '%s.json' % name)
        if os.path.isfile(file_path):
            user_dict = self.read_dict(file_path)
        else:
            print('账号或者密码错误！')
            return False
        if name == user_dict['name'] and pwd == user_dict['pwd'] and user_dict['state'] == 1:
            user_log_path = os.path.join(log_path, '%s.log' % name)
            log_msg = '卡号[%s]登录成功！' % name
            get_logger(user_log_path, log_msg)  # 写入日志
            print('登录成功!\n')
            return user_dict
        else:
            print('登录失败，联系管理员')
            return False
