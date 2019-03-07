#!/usr/bin/env python3
# author:Alnk(李成果)
import os
from atm.core.basic import Basic
from atm.conf import settings
from atm.core.log import get_logger


class Admin(Basic):  # 管理类
    option_lis = [('添加账户', 'create_user'),
                  ('调整用户额度', 'modify_quota'),
                  ('冻结/激活账户', 'frozen_user'),
                  ('查看用户信息', 'check_user_info'),
                  ('退出', 'login_out'), ]


    def __init__(self, name):
        self.name = name

    def create_user(self):
        """
        创建用户
        :return:
        """
        name = input('\n输入卡号>>>')
        pwd = input('输入密码>>>')
        total_quota = 15000  # 额度
        role = 'user'  # 角色
        user_dict = {
            'name': name,  # 账号
            'pwd': pwd,  # 密码
            'role': role,  # 角色 管理员:admin, 用户:user
            'total_quota': total_quota,  # 总额度
            'available_quota': total_quota,  # 可用额度
            'state': 1,  # 状态 1：可用，0：冻结
        }
        file_path = os.path.join(settings.user_info_path, '%s.json' % name)  # 用户文件路径
        self.write_dict(user_dict, file_path)
        log_msg = '用户[%s]创建成功!' % name
        get_logger(settings.admin_log_path, log_msg)

    def modify_quota(self):
        """
        调整用户额度
        :return:
        """
        name = input('调整的卡号>>>')
        quota = int(input('调整的额度>>>'))
        file_path = os.path.join(settings.user_info_path, '%s.json' % name)  # 用户文件路径
        user_dict = self.read_dict(file_path)
        user_dict['total_quota'] = user_dict['total_quota'] + quota  # 调整总额度
        user_dict['available_quota'] = user_dict['available_quota'] + quota  # 调整实际额度
        self.write_dict(user_dict, file_path)
        log_msg = '账户[%s]额度调整成功，调整后的额度为[%s]' % (name, user_dict['total_quota'])
        get_logger(settings.admin_log_path, log_msg)

    def frozen_user(self):
        """
        冻结/解冻 账户
        :return: Ture
        """
        name = input('需要冻结/激活的卡号>>>')
        state = int(input('1:激活/0:冻结 >>>'))
        file_path = os.path.join(settings.user_info_path, '%s.json' % name)  # 文件路径
        user_dict = self.read_dict(file_path)
        user_dict['state'] = state
        self.write_dict(user_dict, file_path)
        print('账号[%s]被[%s]' % (name, '激活' if user_dict['state'] == 1 else '冻结'))
        log_msg = '账号[%s]被[%s]' % (name, '激活' if user_dict['state'] == 1 else '冻结')
        get_logger(settings.admin_log_path, log_msg)  # 日志

    def check_user_info(self):
        name = input('需要查看的账号>>>')
        super().check_user_info(name)

    def run(self):
        while 1:
            print('\n--- 欢迎管理员[%s] ---' % self.name)
            for num, value in enumerate(self.option_lis, 1):
                print(num, value[0])
            action = int(input('\n输入编号>>>'))
            if hasattr(self, self.option_lis[action - 1][1]):
                getattr(self, self.option_lis[action - 1][1])()
            else:
                print('\n编号有误，请重新输入\n')
