#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql as mysql
import sys
import getopt


def usage():
    print('help:')
    print('--host db server,default localhost')
    print('--port db port,default 3306')
    print('--user db username,default root')
    print('--password db password,default blank')
    print('--database db name')
    print('--output markdown output file,default current path')


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h",
                                   ["help", "host=", "port=", "database=", "user=", "password=", "output="])
    except getopt.GetoptError:
        sys.exit()
    if 'help' in args:
        usage()
        sys.exit()
        print(opts)
    host = "localhost"
    user = input("数据库帐号：")
    password = input("数据库密码：")
    database = input("要导出数据库名：")
    port = 3306
    mdfile = input("请输入生成的路径和文件名，如果不填则默认当前目录下(./markdown.md)：")
    output = mdfile if mdfile else "./markdown.md"

    for op, value in opts:
        if op == '--host':
            host = value
        elif op == '--port':
            port = value
        elif op == '--database':
            database = value
        elif op == '--user':
            user = value
        elif op == '--password':
            password = value
        elif op == '--output':
            output = value
        elif op == '-h':
            usage()
            sys.exit()
        if database == '':
            usage()
            #    sys.exit()
    conn = mysql.connect(host=host, port=port, user=user, password=password, database='information_schema')
    cursor = conn.cursor()
    cursor.execute(
        "select table_name,table_comment from information_schema.tables where table_schema='%s' and table_type='base table'" % database)
    tables = cursor.fetchall()

    markdown_table_header = """

### %s 
#### %s 
字段名 | 字段类型 | 默认值 | 注释
---- | ---- | ---- | ---- 
"""
    markdown_table_row = """%s | %s | %s | %s
"""
    f = open(output, 'w')
    for table in tables:
        cursor.execute(
            "select COLUMN_NAME,COLUMN_TYPE,COLUMN_DEFAULT,COLUMN_COMMENT from information_schema.COLUMNS where table_schema='%s' and table_name='%s'" % (
            database, table[0]))
        tmp_table = cursor.fetchall()
        p = markdown_table_header % table
        for col in tmp_table:
            p += markdown_table_row % col
        f.writelines(p)
        f.writelines('\r\n')
    f.close()
    print('数据字典制作完成！')