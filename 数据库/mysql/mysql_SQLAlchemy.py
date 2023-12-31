# 导入
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()

# 定义User对象


class User(Base):
    # 表的名字
    __tablename__ = 'user'

    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


# 初始化数据库连接
engine = create_engine(
    'mysql+mysqlconnector://root:1qw2!QW@@10.1.1.235:3306/testdb')
# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

# 创建session对象
session = DBSession()
# 创建新的User对象
new_user = User(id='5', name='Bob')
# 添加到session
session.add(new_user)
# 提交即保存到数据库
session.commit()
# 关闭session
session.close()


# 查询
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行
user = session.query(User).filter(User.id == '5').one()
# 打印类型和对象的name属性
print('type:', type(user))
print('name:', user.name)
# 关闭session
session.close()


# class User(Base):
#     __tablename__ = 'user'
#     id = Column(String(20),primary_key=True)
#     name = Column(String(20))
#     一对多
#     books = relationship('Book')

# class Book(Base):
#     __tablename__ = 'book'

#     id = Column(String(20),primary_key = True)
#     name = Column(String(20))
#     user_id = Column(String(20),ForeignKey('user.id'))
