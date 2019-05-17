import pymysql

# 创建和数据库服务器的连接　　connection
conn = pymysql.connect(host='localhost',port=3306,user='root',password='123456',
                db='students',charset='utf8')

# 创建游标对象
cursor = conn.cursor()

# 中间可以使用游标完成对数据库的操作
sql = "update student set age=18,description='我再炸!' where name='周润发'"

result = cursor.execute(sql)

# 默认情况下，pymysql里面的游标会把多个数据库的操作语句[添加/修改/删除]设置成一个事物，表示一个整体，
# 所以我们如果不手动提交事物，则默认会进行事物回滚操作 conn.rollback()
conn.commit()

print( result )

# 关闭资源　先关游标
cursor.close()
# 再关连接
conn.close()