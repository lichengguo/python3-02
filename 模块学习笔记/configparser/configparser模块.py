#!/usr/bin/env python3
# author:Alnk
"""
ConfigParser 是用来读取配置文件的包。
配置文件的格式如下：中括号“[ ]”内包含的为section。section 下面为类似于key-value 的配置内容。
"""
import configparser
# 1 实例化一个对象
config = configparser.ConfigParser()
# 2 读取配置文件
config.read('conf.ini', encoding='utf-8')

# 打印所有section
print(config.sections())  # ['db', 'concurrent']

# 获取指定section下指定的opiton的值
db_host = config.get('db', 'db_host')
print(db_host)

# 获取指定section下的所有配置信息
items = config.items('db')
print(items)  # [('db_host', '127.0.0.1'), ('db_port', '69'), ('db_user', 'root')]

# 修改某个option的值，如果不存在则会创建
config.set('db', 'db_port', '3306')
config.write(open('conf.ini', 'w'))
#
config.set('db', 'password', 'abc123')
config.write(open('conf.ini', 'w'))

# 检查section或option是否存在，bool值
res1 = config.has_section('db')
print(res1)
res2 = config.has_option('db', 'host')
print(res2)

# 添加section 和 option
if not config.has_section('mysql'):
    config.add_section('mysql')
#
if not config.has_option('mysql', 'host'):
    config.set('mysql', 'host', '127.0.0.1')
# 写入文件
config.write(open('conf.ini', 'w'))

# 删除section 和 option
config.remove_section('mysql')  # 整个section下的所有内容都将删除
config.write(open('conf.ini', 'w'))
