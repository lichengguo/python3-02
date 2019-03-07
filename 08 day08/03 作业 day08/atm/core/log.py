#!/usr/bin/env python3
#author:Alnk(李成果)
import logging
from logging import DEBUG


def get_logger(log_file, log_msg):
    # 1.创建logger函数对象
    logger = logging.getLogger()  # 这个参数是用户名字
    # 2.创建流对象：文件流fh，屏幕流ch
    fh = logging.FileHandler(log_file)  # 写入日志文件
    # 3.创建日志格式:这里可以创建多个日志格式
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    # 4.流对象添加格式对象
    fh.setFormatter(formatter)  # 文件流添加日志格式
    # 5.logger对象添加流对象
    logger.addHandler(fh)
    # 6.设置日志打印级别
    logger.setLevel(DEBUG)  # 全局设置，同时设置文件流和屏幕流
    #
    logger.info(log_msg)  # 打印INFO日志
    # 在记录日志之后移除句柄,不然会重复打印日志
    logger.removeHandler(fh)

