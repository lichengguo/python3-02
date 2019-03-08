#!/usr/bin/env python3
# author:Alnk(李成果)
import os
from shopping_car.core.basic import Basic
from shopping_car.conf import settings


class Register(Basic):  # 注册

    def register(self):  # 注册
        user_name = input('输入注册账号>>>').strip()
        user_pwd = input('输入密码>>>').strip()
        # 用户信息字典
        user_info_dict = {
            "user_name": user_name,
            "user_pwd": user_pwd,
            "shopping_car": {},
        }
        user_info_path_file = os.path.join(settings.user_info_path, '%s.json' % user_name)
        if os.path.isfile(user_info_path_file):
            print('该账号已经注册，请直接登录!\n')
        else:
            self.write_info(user_info_dict, user_info_path_file)  # 写入信息
            print('\n账号[%s]注册成功\n' % user_name)
