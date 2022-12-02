from sqlalchemy import create_engine,MetaData,Integer,String,Table,Column
from sqlalchemy.orm import mapper,sessionmaker

url="mysql://root:root@localhost:3306/new"

Engine=create_engine(url)

class Student:
    def __init__(self,r,n,c):
        self.rn=r
        self.name=n
        self.city=c

    def __str__(self):
        return f"{self.rn},{self.name},{self.city}"

md=MetaData()
st=Table('info',md,
         Column('rn',Integer,primary_key=True),
         Column('name',String(20),unique=True),
         Column('city',String(20),nullable=False))

mapper(Student,st)
md.create_all(Engine)
Session=sessionmaker(bind=Engine)
sess=Session()
      
