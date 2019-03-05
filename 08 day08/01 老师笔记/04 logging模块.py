


import  logging

############################# 函数式用法

# logging.basicConfig(level=logging.DEBUG,
#                     format='----> %(asctime)s [line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='test.log',
#                     filemode='a')
#
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')

############################# logger对象用法

def get_logger():
    import logging
    # 1 创建logger对象
    logger = logging.getLogger()

    # 创建流对象：文件流fh，屏幕流ch
    # 创建一个handler，用于写入日志文件
    fh = logging.FileHandler('test.log')
    # 再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    # # 设置级别
    from logging import WARNING, DEBUG, INFO, ERROR
    logger.setLevel(DEBUG)
    ch.setLevel(ERROR)
    # 3 创建格式对象
    formatter = logging.Formatter('%(asctime)s --- %(message)s')
    formatter2 = logging.Formatter('%(asctime)s --%(levelname)s- %(message)s')

    # 4 流对象添加格式对象
    fh.setFormatter(formatter)
    ch.setFormatter(formatter2)

    # 5 logger对象添加流对象
    logger.addHandler(fh)  # logger对象可以添加多个fh和ch对象
    logger.addHandler(ch)

    return logger

# 6 使用logger对象进行日志打印
logger=get_logger()
logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')