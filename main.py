from sqlalchemy import create_engine
engine=create_engine("mysql://docker:docker@192.168.1.124:3306/test_database")

from sqlalchemy.ext.declarative import declarative_base
Base=declarative_base()

from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, DateTime
import datetime
class Memo(Base):
    __tablename__="user" #テーブル名を指定
    id=Column(Integer, primary_key=True)
    title=Column(String(255))
    body=Column(String(255))
    datetime = Column(DateTime())

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
SessionClass=sessionmaker(engine) #セッションを作るクラスを作成
session=SessionClass()

#データクリア
for r in session.query(Memo).all():
    session.delete(r)
session.commit()

for i in range(1000):
    session.add(Memo(title="test{}".format(i),body="tttttttttest",datetime=datetime.datetime.now()))
    print(i)

session.commit()

for r in session.query(Memo).all():
    print(r.id,end=",")
    print(r.title,end=",")
    print(r.body,end=",")
    print(r.datetime)

#データクリア
for r in session.query(Memo).all():
    session.delete(r)
session.commit()

for r in session.query(Memo).all():
    print(r.id,end=",")
    print(r.title,end=",")
    print(r.body,end=",")
    print(r.datetime)