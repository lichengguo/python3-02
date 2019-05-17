#!/usr/bin/env python3
# author:Alnk
# 插入一条数据
import pymysql

# 1.创建连接
conn = pymysql.connect(host='localhost', port=3306, db='test', charset='utf8', user='root', password='123456')

# 2.创建游标
cursor = conn.cursor()

# 3.编写sql语句
sql = "insert into student (name,sex,class,age) value ('日天','2','405','38')"

# 4.执行sql语句
cursor.execute(sql)

# 5.提交
conn.commit()

# 6.结束关闭
cursor.close()
conn.close()
