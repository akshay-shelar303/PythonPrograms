'''
from sqlalchemy import *
from sqlalchemy.orm import *

url="mysql://root:root@localhost:3306/new"
Engine=create_engine(url)
class Customer:
    def __init__(self,cid,n):
        self.cid=cid
        self.name=n

    def __str__(self):
        return f"{self.cid},{self.name}"

class Orders:
    def __init__(self,oid,n,cid):
        self.oid=oid
        self.name=name

    def __str__(self):
        return f"{self.cid},{self.name}"

md=MetaData()

st=Table('Custo',md,
         Column('cid',Integer,primary_key=True),
         Column('name',String(20),nullable=False))

mapper(Customer,st)

md.create_all(Engine)

Session=sessionmaker(bind=Engine)
sess=Session()

c=Customer(1,'Akshay')
sess.add(c)

sess.commit()
sess.close()
'''

'''

from sqlalchemy import *
from sqlalchemy.orm import *

DB_URL='mysql://root:root@localhost:3306/new'

ENGINE=create_engine(DB_URL)

class Customer:
    def __init__(self,cid,name,amount):
        self.cid=cid
        self.name=name
        self.amount=amount

    def __str__(self):
        return f'{self.cid},{self.name},{self.amount}'

class Details:
    def __init__(self,oid,name,cid):
        self.oid=oid
        self.name=name
        self.cid=cid

    def __str__(self):
        return f'{self.oid},{self.name},{self.cid}'
    

md=MetaData()

st1=Table('cust',md,Column('cid',Integer,primary_key=True),
          Column('name',String(20)),
          Column('amount',Integer))

st2=Table('orders',md,Column('oid',Integer,primary_key=True),
           Column('name',String(20)),
           Column('cid',Integer,ForeignKey("cust.cid",onupdate='CASCADE',ondelete='CASCADE')),
           )

mapper(Customer,st1)
mapper(Details,st2)

md.create_all(ENGINE)

Session=sessionmaker(bind=ENGINE)
sess=Session()

while True :

    print('---Select Operation--- \n1.INSERTION\n2.DATA RETRIVE\
             \n3.UPDATION\n4.DELETION\n5.ExitLoop')
    ch=int(input('Enter your choice-'))

    if ch==1:
        print('Select table\n1.Cust\n2.orders')
        ch=int(input('Enter your choice-'))
        if ch==1:
            cid=int(input('Enter customer id-'))
            name=input('enter customer name-')
            amount=int(input('Enter amount-'))
            c=Customer(cid,name,amount)
            sess.add(c)
            
        elif ch==2:
            oid=int(input('Enter order id-'))
            name=input('Enter order name-')
            cid=int(input('Enter customer id-'))
            d=Details(oid,name,cid)
            sess.add(d)
            
    elif ch==2:
        print('Select table \n1.Cust\n2.orders')
        ch=int(input('Enter your choice-'))
        if ch==1:
            val1=sess.query(Customer)
            for i in val1:
                print(i)
        elif ch==2:
            val2=sess.query(Details)
            for j in val2:
                print(j)


    elif ch==3:
        print('Select table to update \n1.cust\n2.orders')
        ch=int(input('Enter your choice-'))
        if ch==1:
            print('Select column tobe updated\n1.name\n2.amount\n3.cid')
            ch=int(input('Enter your choice-'))
            if ch==1:
                new_name=input('Enter updated name-')
                r=int(input('Enter cid which name is tobe updated-'))
                sess.query(Customer).filter(Customer.cid==r).update({Customer.name:new_name})
                
            elif ch==2:
                new_amount=int(input('Enter new amount-'))
                r=int(input('Enter cid which name is tobe updated-'))
                sess.query(Customer).filter(Customer.cid==r).update({Customer.amount:new_amount})
                
            elif ch==3:
                new_cid=int(input('Enter new cid-'))
                r=int(input('Enter cid which cid is tobe updated-'))
                sess.query(Customer).filter(Customer.cid==r).update({Customer.cid:new_cid})


        elif ch==2:
            print('Select column tobe updated\n1.oid\n2.name\n3.cid')
            ch=int(input('Enter your choice-'))
            if ch==1:
                new_oid=int(input('Enter updated oid-'))
                r=int(input('Enter cid which name is tobe updated-'))
                sess.query(Details).filter(Deatils.cid==r).update({Details.oid:new_oid})
                
            elif ch==2:
                new_name=input('Enter new name-')
                r=int(input('Enter cid which name is tobe updated-'))
                sess.query(Details).filter(Details.cid==r).update({Details.name:new_name})
                
            elif ch==3:
                new_cid=int(input('Enter new cid-'))
                r=int(input('Enter cid which name is tobe updated-'))
                sess.query(Details).filter(Details.cid==r).update({Details.cid:new_cid})

    elif ch==4:
        print('Select table to update \n1.Cust\n2.orders')
        ch=int(input('Enter your choice-'))
        if ch==1:
            print('Select column whose row is to delete\n1.name\n2.amount\n3.cid')
            ch=int(input('Enter your choice-'))
            if ch==1:
                n=input('Enter name-')
                sess.query(Customer).filter(Customer.name==n).delete()

            elif ch==2:
                a=int(input('Enter amount-'))
                sess.query(Customer).filter(Customer.amount==a).delete()

            elif ch==3:
                n=input('Enter cid-')
                sess.query(Customer).filter(Customer.cid==c).delete()

        elif ch==2:
            print('Select column whose row is to delete\n1.oid\n2.name\n3.cid')
            ch=int(input('Enter your choice-'))
            if ch==1:
                o=int(input('Enter name-'))
                sess.query(Details).filter(Details.oid==o).delete()

            elif ch==2:
                n=input('Enter amount-')
                sess.query(Details).filter(Details.name==n).delete()

            elif ch==3:
                n=input('Enter cid-')
                sess.query(Details).filter(Details.cid==c).delete()
                
    elif ch==5:
        break
       
    sess.commit()
sess.close()


'''
'''
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

url="mysql://root:root@localhost:3306/practice"
ENGINE=create_engine(url)
Base=declarative_base()

class Info(Base):
    __tablename__='student'
    uid=Column(Integer,primary_key=True)
    name=Column(String(30),primary_key=True)
    age=Column(Integer)

    def __str__(self):
        return f"{self.uid},{self.name},{self.age}"

class Details(Base):
    __tablename__='detail'
    pid=Column(Integer,primary_key=True)
    name=Column(String(30))
    uid=Column(Integer),ForeignKeyConstraint(['name','uid'],['student.name','student.uid'])
    

    def __str__(self):
        return f"{self.pid},{self.name},{self.uid}"

Base.metadata.create_all(ENGINE)

'''
'''
from sqlalchemy import *
from sqlalchemy.orm import *
url="mysql://root:root@localhost:3306/practice"
ENGINE=create_engine(url)
class Info:
    def __init__(self,uid,name,age):
        self.uid=uid
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.uid},{self.name},{self.age}"

class Details:
    def __init__(self,pid,name,uid):
        self.pid=pid
        self.name=name
        self.uid=uid

    def __str__(self):
        return f"{self.pid},{self.name},{self.uid}"
md=MetaData()

st1=Table('tbl1',md,
          Column('uid',Integer,primary_key=True),
          Column('name',String(30),primary_key=True),
          Column('age',Integer,nullable=False))

st2=Table('tbl2',md,
          Column('pid',Integer,primary_key=True),
          Column('p_name',String(30),nullable=False),
          Column('p_uid',Integer,nullable=False),
          ForeignKeyConstraint(['p_name','p_uid'],['tbl1.name','tbl1.uid'])
                 )      


mapper(Info,st1)
mapper(Details,st2)
md.create_all(ENGINE)


'''
'''

for i in range(1,6):
    for j in range(1,16):
        if j>=i:
            print('*',end='')
        else:
            print(' ',end='')
    print()
    
for i in range(1,6):
    for j in range(i,6):
        print('*',end=' ')
    print()


'''
'''
def outerfun():
    print("Akshay Shelar")

    def innerfun():
        print("Python Batch")

    return innerfun()

outerfun()
'''


##for i in range(5):
##    print(i)
##
##l1=[1,3,2]
##l2 = [4,6,5]
##l1.append(4)
##print(l1)
##print(l1.sort())



##li = ['Akshay','Shelar']
##mystr = ' '.join(li)
##print(type(mystr),mystr)
##
##print(mystr[::-2])
##
##


num = 1

while num <= 5:
    print(num)
    num += 1



























    








