import pymysql

# 创建和数据库服务器的连接　　connection
conn = pymysql.connect(host='localhost',port=3306,user='root',password='123456',
                db='students',charset='utf8')

# 创建游标对象
cursor = conn.cursor()

# 中间可以使用游标完成对数据库的操作
sql = "select * from student where sex=1"

# 执行ｓｑｌ语句的函数　　返回值是该ＳＱＬ语句影响的行数
count = cursor.execute(sql)

# print("数据的总数 或者 操作影响的行数%d" % count)

# print(cursor.fetchone())   # 返回值类型是元祖，表示一条记录

# print(cursor.fetchall())    # 返回值类型是元组，元组里面的每一个成员就是一条数据记录，也是一个元组

# 获取本次操作的所有数据
for line in cursor.fetchall():
    print("数据是%s" % str(line))

# 关闭资源　先关游标
cursor.close()
# 再关连接
conn.close()