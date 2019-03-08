#!/usr/bin/env python3
# author:Alnk(李成果)
import os
from shopping_car.conf import settings
from shopping_car.core.basic import Basic


login_flag = False  # 标志位，购物之前要先登录
user_name = None  # 购物车使用

class Login(Basic):  # 登录类

    def login(self):  # 登录
        self.user_name = input('输入登录账号>>>')
        self.user_pwd = input('输入登录密码>>>')
        user_info_path_file = os.path.join(settings.user_info_path, '%s.json' % self.user_name)
        user_info_dict = self.read_info(user_info_path_file)
        if user_info_dict == False:
            print('\n账号或密码有问题\n')
            return False
        if user_info_dict['user_pwd'] == self.user_pwd:
            print('登录成功\n')
            global login_flag,user_name
            login_flag = True
            user_name = self.user_name
        else:
            print('\n账号或密码错误\n')
