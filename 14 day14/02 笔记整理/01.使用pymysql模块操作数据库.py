#!/usr/bin/env python3
# author:Alnk
# 一般需要安装pymysql模块
# pip install pymysql

import pymysql

# 1.创建和数据库服务的链接
conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', charset='utf8', db='test')

# 2.创建游标对象
cursor = conn.cursor()

# 3.中间可以使用游标完成对数据库的操作
sql = "select * from student;"

# 4.执行sql语句函数，返回值是sql语句的影响行数
count = cursor.execute(sql)
print('被影响的行数', count)
# print(cursor.fetchone())  # 获取一行数据，类型为元组
# print(cursor.fetchmany(3))  # 获取多行数据
# print(cursor.fetchall())  # 获取全部数据

# 5.格式化输出本次操作的所有数据
for line in cursor.fetchall():
    print(line)

# 6.关闭资源，先关闭游标，在关闭连接
cursor.close()
conn.close()

# 注意，如果是修改，插入数据，需要提交语句，只是查询则不需要
# conn.commit()
