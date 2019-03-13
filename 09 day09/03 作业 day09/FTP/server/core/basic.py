#!/usr/bin/env python3
#author:Alnk(李成果)
import json
import os
import hashlib


class Basic:  # 基础读写数据类

    def read_info(self, filename):  # 读取信息
        if os.path.isfile(filename):
            with open(filename, 'r') as f:
                user_dict = json.load(f)
            return user_dict
        else:
            print('找不到文件')
            return None

    def write_info(self, filename, info_dict):  # 写入信息
        with open(filename, 'w') as f:
            json.dump(info_dict, f)
            f.flush()

    def get_md5(self,line):  # 获取md5
        md5 = hashlib.md5()
        md5.update(line)
        file_md5 = md5.hexdigest()
        return file_md5