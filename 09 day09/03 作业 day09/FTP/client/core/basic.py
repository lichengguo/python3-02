#!/usr/bin/env python3
#author:Alnk(李成果)
import struct
import json
import hashlib
import sys


class Basic:  # 基类

    def send_dict_info(self, info_dict):  # 拼接发给服务端的基础信息
        info_dict_bites = json.dumps(info_dict).encode()  # 转换成字节格式
        info_dict_bites_length = len(info_dict_bites)  # 统计长度
        info_park = struct.pack('i', info_dict_bites_length)  # 打包
        last_info = info_park + info_dict_bites  # 拼接
        return last_info

    def get_md5(self,line):  # 获取md5
        md5 = hashlib.md5()
        md5.update(line)
        file_md5 = md5.hexdigest()
        return file_md5

    def view_bar(self, total_size, already_size):  # 进度条
        num = int((already_size / total_size) * 100)
        r = '\r%s%s%%' % ('>'*num, num)
        sys.stdout.write(r)
        sys.stdout.flush
