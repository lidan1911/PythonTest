import pymysql

# 打开数据库连接
db = pymysql.connect(host='192.168.100.55',
                     port=3306,
                     user='root',
                     passwd='root',
                     db='db_school')

# 使用cursor()方法创建一个游标对象cur
cur = db.cursor()

# ====查询

# 使用execute()方法执行sql查询
cur.execute('select * from student')
# 使用fetchall()方法获取查询结果
data = cur.fetchall()
print(data)
# 关闭数据库连接
db.close()

# # ====增删改
# try:
#     cur.execute("增删改sql")
#     # 提交
#     db.commit()
# except Exception as e:
#     print("错误信息：%s" % str(e))
#     # 错误回滚
#     db.rollback()
# finally:
#     db.close()


