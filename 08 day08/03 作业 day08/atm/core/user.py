#!/usr/bin/env python3
# author:Alnk(李成果)
import os
from atm.core.basic import Basic
from atm.conf import settings
from atm.core.decorator import outer
from atm.core.log import get_logger


class User(Basic):  # 用户类
    option_lis = [('查看账户信息', 'check_user_info'),
                  ('取现', 'with_draw'),
                  ('还款', 'pay_back'),
                  ('转账', 'transfer'),
                  ('退出', 'login_out')]

    def __init__(self, name):
        self.name = name
        self.file_path = os.path.join(settings.user_info_path, '%s.json' % self.name)  # 初始化用户信息文件路径
        self.user_dict = self.read_dict(self.file_path)  # 获取用户详细信息
        self.log_file = os.path.join(settings.log_path, '%s.log' % self.name)  # 日志文件路径

    def check_user_info(self):  # 查看账户信息
        super().check_user_info(self.name)

    def with_draw(self):  # 提现
        print('你可提现额度为[%s]' % (float(self.user_dict['available_quota']) * (1 - settings.service_charge)))  # 要手续费
        quota = float(input('输入你想提现的金额 手续费为5%>>>'))
        if quota <= float(self.user_dict['available_quota']) * (1 - settings.service_charge):  # 提现不能超过可用额度
            self.user_dict['available_quota'] -= quota * (1 + settings.service_charge)  # 可用额度减去提现额度和手续费
            self.write_dict(self.user_dict, self.file_path)
            print('提现成功\n')
            log_msg = '用户[%s]提现[%s]元 手续费[%s]' % (self.name, quota, quota * settings.service_charge)
            get_logger(self.log_file, log_msg)  # 写入到日志
        else:
            print('请输入合理的提现金额')

    def pay_back(self):  # 还款
        pay_back_quota = self.user_dict['total_quota'] - self.user_dict['available_quota']  # 还款额度
        print('你需要还款的总额为[%s]' % pay_back_quota)
        if pay_back_quota == 0:
            print('不需要还款\n')
            return False
        input_quota = float(input('输入还款金额>>>'))
        if 0 < input_quota <= pay_back_quota:
            self.user_dict['available_quota'] += input_quota
            self.write_dict(self.user_dict, self.file_path)
            print('还款成功，可用额度为[%s]\n' % self.user_dict['available_quota'])
            log_msg = '用户[%s]还款[%s]元' % (self.name, input_quota)
            get_logger(self.log_file, log_msg)

    def transfer(self):  # 转账
        friend_card = input('输入对方卡号>>>')
        money = float(input('转账金额>>>'))
        if not os.path.isfile(os.path.join(settings.user_info_path, '%s.json' % friend_card)):
            print('账号[%s]不存在\n' % friend_card)
            return False
        if self.user_dict['available_quota'] >= money:
            self.user_dict['available_quota'] -= money  # 转账，自己账号减少额度
            self.write_dict(self.user_dict, self.file_path)  # 写入自己的文件
            file_path = os.path.join(settings.user_info_path, '%s.json' % friend_card)  # 对方文件路径
            friend_dict = self.read_dict(file_path)  # 对方相信信息
            friend_dict['available_quota'] += money  # 对方账号增加额度
            self.write_dict(friend_dict, file_path)  # 对方详细信息写入文件
            print('转账成功')
            log_msg = '用户[%s]向账号[%s]转账[%s]元' % (self.name, friend_card, money)
            get_logger(self.log_file, log_msg)
        else:
            print('可用余额不足\n')

    def run(self):
        while 1:
            print('\n--- 欢迎用户[%s] ---' % self.name)
            for num, value in enumerate(self.option_lis, 1):
                print(num, value[0])
            action = int(input('\n输入编号>>>'))
            if hasattr(self, self.option_lis[action - 1][1]):
                getattr(self, self.option_lis[action - 1][1])()
            else:
                print('\n编号有误，请重新输入\n')
