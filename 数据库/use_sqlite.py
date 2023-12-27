import sqlite3

# 创建一个连接到数据库文件test.db的连接
conn = sqlite3.connect('test.db')
# 创建一个cursor
cursor = conn.cursor()
# 执行sql语句
cursor.execute('create table user (id int primary key,name varchar(30))')
cursor.execute('insert into user(id,name) values (1,\'xnp\')')
cursor.execute('select * from user where id=?', ('1',))
# fetchall获取结果集，结果集是一个list
values = cursor.fetchall()
print(type(values))
# rowcount获得插入的行数
cursor.rowcount
# 提交事务
conn.commit()
# 关闭cursor
cursor.close()
# 关闭连接
conn.close()
