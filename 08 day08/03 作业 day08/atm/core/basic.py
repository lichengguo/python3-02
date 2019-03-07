#!/usr/bin/env python3
# author:Alnk(李成果)
import json
import os
from atm.conf import settings


class Basic:  # 基础类

    def write_dict(self, user_dict, file_name):
        """
        写入数据
        :param user_dict: 用户信息字典
        :param file_name: 文件名称
        :return: True
        """
        with open(file_name, encoding='utf-8', mode='w') as f:
            json.dump(user_dict, f)
            f.flush()
        return True

    def read_dict(self, file_name):
        """
        读取数据
        :param file_name: 文件名称
        :return: user_dict
        """
        with open(file_name, encoding='utf-8', mode='r') as f:
            user_dict = json.load(f)
        return user_dict

    def check_user_info(self, name):  # 查看用户详细信息
        file_path = os.path.join(settings.user_info_path, '%s.json' % name)  # 文件路径
        user_dict = self.read_dict(file_path)
        msg = '''\n------ 账号[%s]的详细信息 ------
        账号: %s
        总额度: %s
        可用额度: %s
        状态: %s\n\n
        ''' % (user_dict['name'], user_dict['name'],
               user_dict['total_quota'],
               user_dict['available_quota'],
               '激活' if user_dict['state'] == 1 else '冻结',
               )
        print(msg)

    def login_out(self):
        exit('退出')
