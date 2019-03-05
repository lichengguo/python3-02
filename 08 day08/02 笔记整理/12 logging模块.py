#!/usr/bin/env python3
# author:Alnk(李成果)

# 一 函数式用法（不常用，太过于简单）
# import logging
# logging.basicConfig(level=logging.DEBUG,  # 日志默认打印级别
#                     format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',  # 日志格式信息
#                     datefmt = '%a, %d %b %Y %H:%M:%S',  # 时间格式
#                     filename = 'test1.log',  # 日志文件，写入到文件就不在屏幕打印了
#                     filemode='a'  # 写入方式 ，日志一般要追加格式。
#                     )
#
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')


# 二 对象式用法
# 大鱼吃小鱼，小鱼吃虾米
# import logging
#
# # 1.创建logger函数对象
# logger = logging.getLogger('alnk')  # 这个参数是用户名字
#
# # 2.创建流对象：文件流fh，屏幕流ch
# fh = logging.FileHandler('test2.log')  # 写入日志文件
# ch = logging.StreamHandler()  # 输出到屏幕
#
# # 3.创建日志格式:这里可以创建多个日志格式
# formatter = logging.Formatter('%(asctime)s -- %(message)s')
#
# # 4.流对象添加格式对象
# fh.setFormatter(formatter)  # 文件流添加日志格式
# ch.setFormatter(formatter)  # 屏幕流添加日志格式
#
# # 5.logger对象添加流对象
# logger.addHandler(fh)
# logger.addHandler(ch)
#
# # 6.使用logger 对象进行日志打印
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warning message')
# logger.error('error message')
# logger.critical('critical message')


# 需求：流对象设置日志打印等级
# import logging
# from logging import DEBUG,INFO,WARN,ERROR,CRITICAL
#
# # 1.创建logger函数对象
# logger = logging.getLogger('alnk')  # 这个参数是用户名字
#
# # 2.创建流对象：文件流fh，屏幕流ch
# fh = logging.FileHandler('test2.log')  # 写入日志文件
# ch = logging.StreamHandler()  # 输出到屏幕
#
# # 3.创建日志格式:这里可以创建多个日志格式
# formatter = logging.Formatter('%(asctime)s -- %(message)s')
#
# # 4.流对象添加格式对象
# fh.setFormatter(formatter)  # 文件流添加日志格式
# ch.setFormatter(formatter)  # 屏幕流添加日志格式
#
# # 5.logger对象添加流对象
# logger.addHandler(fh)
# logger.addHandler(ch)
#
# # 6.设置日志打印级别
# logger.setLevel(DEBUG)  # 全局设置，同时设置文件流和屏幕流
# fh.setLevel(ERROR)  # 单独设置文件流日志打印级别
# # ch.setLevel(INFO)  # 单独设置屏幕流日志打印级别
#
# # 7.使用logger 对象进行日志打印
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warning message')
# logger.error('error message')
# logger.critical('critical message')


# 常用的方式：封装成函数，单独放置到一个模块，如日志模块，然后调用就可以
import logging
from logging import DEBUG, INFO, WARN, ERROR, CRITICAL  # 日志的5个级别


def get_logger():
    # 1.创建logger函数对象
    logger = logging.getLogger('alnk')  # 这个参数是用户名字

    # 2.创建流对象：文件流fh，屏幕流ch
    fh = logging.FileHandler('test2.log')  # 写入日志文件
    ch = logging.StreamHandler()  # 输出到屏幕

    # 3.创建日志格式:这里可以创建多个日志格式
    # formatter = logging.Formatter('%(asctime)s -- %(message)s')
    formatter = logging.Formatter('xxx -- %(message)s')

    # 4.流对象添加格式对象
    fh.setFormatter(formatter)  # 文件流添加日志格式
    ch.setFormatter(formatter)  # 屏幕流添加日志格式

    # 5.logger对象添加流对象
    logger.addHandler(fh)
    logger.addHandler(ch)

    # 6.设置日志打印级别
    logger.setLevel(DEBUG)  # 全局设置，同时设置文件流和屏幕流
    fh.setLevel(ERROR)  # 单独设置文件流日志打印级别
    # ch.setLevel(INFO)  # 单独设置屏幕流日志打印级别

    return logger


# 调用get_logger()函数进行日志打印
logger = get_logger()

logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')
