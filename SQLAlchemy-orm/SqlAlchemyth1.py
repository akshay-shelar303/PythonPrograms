
from sqlalchemy import create_engine,MetaData,Table,Column,Integer,String,Float
from sqlalchemy.orm import mapper,sessionmaker

DB_URL='mysql://root:root@localhost:3306/mydb'

ENGINE=create_engine(DB_URL)
print(ENGINE,type(ENGINE))


class Student:
    def __init__(self,r,n,m):
        self.rn=r
        self.name=n
        self.marks=m

    def __str__(self):
        return f"{self.rn},{self.name},{self.marks}"

md=MetaData()

st=Table('Stud',md,Column('rn',Integer,primary_key=True),
         Column('name',String(20)),
         Column('marks',Float))

mapper(Student,st)
print('Mapped')

md.create_all(ENGINE)
print('TAble created')

Session=sessionmaker(bind=ENGINE)
sess=Session()
print(sess,type(sess))

s1=Student(1,'Akshay',95)
s2=Student(2,'Prashant',70)
s3=Student(3,'Advik',80)

#INSERTION
sess.add(s1)
##sess.add_all([s2,s3])

#DATA RETEIVE
data=sess.query(Student)
for rows in data:
    print(rows)

var=sess.query(Student).filter(Student.rn==2)
for i in var:
    print(i)

#UPDATION
#sess.query(Student).filter(Student.rn==3).update({Student.marks:60})

#DELETE
##sess.query(Student).filter(Student.rn==2).delete()

sess.commit()
sess.close()



'''
from sqlalchemy import create_engine,MetaData,Table,Column,Integer,String,Float
from sqlalchemy.orm import mapper,sessionmaker

DB_URL='mysql://root:root@localhost:3306/shelar_db'

ENGINE=create_engine(DB_URL)

class Student:
    def __init__(self,r,n,m):
        self.rn=r
        self.name=n
        self.marks=m

    def __str__(self):
        return f"{self.rn},{self.name},{self.marks}"

md=MetaData()

st=Table('Stud',md,Column('rn',Integer,primary_key=True),
         Column('name',String(20),nullable=False),
         Column('marks',Float))

mapper(Student,st)

md.create_all(ENGINE)

Session=sessionmaker(bind=ENGINE)
sess=Session()



print('---Select Choice----\
       \n1.Insert Data\n2.Retrive Data\n3.Updata\n4.Delete')

ch=int(input('Enter your choice-'))

if ch==1:
    r=int(input('Enter roll no-'))
    n=input('Enter Student name-')
    m=float(input('Enter marks-'))
    s=Student(r,n,m)
    sess.add(s)

elif ch==2:
    var=sess.query(Student)
    for rows in var:
        print(rows)

elif ch==3:

    sess.query(Student).filter(Student.rn=={val}).update({Student.marks:{}})

elif ch==4:
    
    sess.query(Student).filter(Student.rn==1).delete()

sess.commit()
sess.close()
    
      
'''

'''
from sqlalchemy import create_engine,MetaData,Table,Column,Integer,String,Float
from sqlalchemy.orm import mapper,sessionmaker

DB_URL='mysql://root:root@localhost:3306/shelar_db'

ENGINE=create_engine(DB_URL)

class Student:
    def __init__(self,r,n,c):
        self.rn=r
        self.name=n
        self.city=c

    def __str__(self):
        return f"{self.rn},{self.name},{self.city}"

md=MetaData()

st=Table('Info',md,Column('rn',Integer,primary_key=True),
         Column('name',String(20),nullable=False),
         Column('city',String(20)))

mapper(Student,st)

md.create_all(ENGINE)

Session=sessionmaker(bind=ENGINE)
sess=Session()

s1=Student(1,'','Nashik')
sess.add(s1)

sess.commit()
sess.close()
'''
'''
from sqlalchemy import create_engine,MetaData,Table,Column,Integer,String,Float,ForeignKey
from sqlalchemy.orm import mapper,sessionmaker

DB_URL='mysql://root:root@localhost:3306/shelar_db'

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
           Column('cid',Integer,ForeignKey("cust.cid")),
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
                r=int(input('Enter cid which name is tobe updated-'))
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







































