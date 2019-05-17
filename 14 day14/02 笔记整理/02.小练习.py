#!/usr/bin/env python3
#author:Alnk
# 在python中操作pymysql，获取 301班所有女生的信息[id,name,sex,age]

import pymysql

# 1.创建连接
conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='test', charset='utf8')

# 2.创建游标
cursor = conn.cursor()

# 3.编写sql语句
sql = "select id,name,sex,age from student where sex = 2 "

# 4.执行sql语句
cursor.execute(sql)

# 5.格式化输出
for line in cursor.fetchall():
    print(line)

# 6.结束关闭
cursor.close()
conn.close()

