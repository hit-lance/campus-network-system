import MySQLdb

# 打开数据库连接
db = MySQLdb.connect('localhost', 'root', '123456', 'cns')
# db = pymysql.connect(host="localhost", user="root", password="admin", db="epoch", port=3306)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用 executor()方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用fetchone()获取一条数据库
data = cursor.fetchone()

# 关闭数据库连接
db.close()