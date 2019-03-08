#!/usr/bin/env python3
# author:Alnk(李成果)
import json
import os


class Basic:  # 基础类

    def __init__(self, name=None, pwd=None):
        pass

    def read_info(self, file_path):  # 读取信息
        if os.path.isfile(file_path):
            with open(file_path, encoding='utf-8', mode='r') as f:
                user_info_dict = json.load(f)
                return user_info_dict
        else:
            return False

    def write_info(self, msg, file_path):  # 写入信息
        if os.path.isdir(os.path.dirname(file_path)):
            with open(file_path, encoding='utf-8', mode='w') as f:
                json.dump(msg, f)
                return True
        else:
            return False
