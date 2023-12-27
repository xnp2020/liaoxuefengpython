# 导入MySQL驱动:
import mysql.connector


# 注意把password设为你的root口令:
conn = mysql.connector.connect(
    user='root', password='1qw2!QW@', database='testdb', host='10.1.1.235')
cursor = conn.cursor()
# 创建user表:
cursor.execute(
    'create table user2 (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user2 (id, name) values (%s, %s)',
               ['1', 'Michael'])
cursor.rowcount
# 结果：1
# 提交事务:
conn.commit()
cursor.close()
# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
values
# 结果：[('1', 'Michael')]
# 关闭Cursor和Connection:
cursor.close()
conn.close()
