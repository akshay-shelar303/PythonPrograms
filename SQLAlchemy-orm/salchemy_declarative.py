'''
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL="mysql://root:root@localhost:3306/new"

ENGINE=create_engine(URL)

Base=declarative_base()

class Student(Base):
    __tablename__='stud'
    rn=Column(Integer,primary_key=True)
    name=Column(String(20),nullable=False)
    marks=Column(Integer)

    def __str__(self):
        return f"{self.rn},{self.name},{self.marks}"

Base.metadata.create_all(ENGINE)

Session=sessionmaker(bind=ENGINE)
sess=Session()

s1=Student(rn=1,name='Akshay',marks=90)
s2=Student(rn=2,name='Prashant',marks=80)
s3=Student(rn=3,name='Advik',marks=70)

#sess.add_all([s1,s2,s3])

#sess.query(Student).filter(Student.rn==1).update({Student.marks:95})

data=sess.query(Student)
for rows in data:
    print(rows)
    
sess.commit()
sess.close()
'''
'''
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL="mysql://root:root@localhost:3306/new"

ENGINE=create_engine(URL)
Base=declarative_base()

class Student(Base):
    __tablename__='details'
    rn=Column(Integer,primary_key=True)
    name=Column(String(20))
    marks=Column(Integer)

    def __str__(self):
        return f"{self.rn},{self.name},{self.marks}"

Base.metadata.create_all(ENGINE)

Session=sessionmaker(bind=ENGINE)
sess=Session()

while True:
    print("Select Operation--\n1.INSERTION\n2.UPDATION\n3.DELETION\n4.DATA RETRIVE\n5.EXITLOOP")
    ch=int(input('Enter your choice-'))
    if ch==1:
        r=int(input("Enter roll no-"))
        n=input('Enter name-')
        m=int(input('Enter marks-'))

        s=Student(rn=r,name=n,marks=m)
        sess.add(s)

    elif ch==2:
        print("select column to update\n1.rn\n2.name\n3.marks")
        ch=int(input('ENter your choice-'))
        if ch==1:
            new_value=int(input('Enter new rn value-'))
            r=int(input('Enter rn -'))
            sess.query(Student).filter(Student.rn==r).update({Student.rn:new_value})

        elif ch==2:
            new_value=input('Enter new name value-')
            r=int(input('Enter rn  -'))
            sess.query(Student).filter(Student.rn==r).update({Student.name:new_value})

        if ch==3:
            new_value=int(input('Enter new marks value-'))
            r=int(input('Enter rn -'))
            sess.query(Student).filter(Student.rn==r).update({Student.marks:new_value})
            
    elif ch==3:
        print("select---\n1.delete all\n2.delete by columns")
        ch=int(input('ENter your choice-'))
        if ch==1:
            sess.query(Student).delete()

        elif ch==2:
            print("select column \n1.rn\n2.name\n3.marks")
            ch=int(input('ENter your choice-'))
            if ch==1:
                r=int(input('Enter roll no-'))
                sess.query(Student).filter(Student.rn==r).delete()

            elif ch==2:
                n=input('Enter name-')
                sess.query(Student).filter(Student.name==n).delete()

            elif ch==3:
                marks=int(input('Enter marks-'))
                sess.query(Student).filter(Student.name==n).delete()
                
    elif ch==4:
        var=sess.query(Student)
        i=None
        for i in var:
            print(i)
        if i is None:
            print("no records founs")
      
            
    elif ch==5:
        break

            
    sess.commit()
sess.close()

'''

'''
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL="mysql://root:root@localhost:3306/new"

ENGINE=create_engine(URL)
Base=declarative_base()

class Details(Base):
    __tablename__='person'
    pid=Column(Integer,primary_key=True)
    name=Column(String(20))
    city=Column(String(20))

    def __str__(self):
        return f"{self.pid},{self.name},{self.city}"

class License(Base):
    __tablename__='license_info'
    lid=Column(Integer,primary_key=True)
    li_no=Column(String(20))
    pid=Column(Integer,ForeignKey('person.pid',onupdate='CASCADE',ondelete='CASCADE'))

    def __str__(self):
        return f"{self.lid},{self.li_no},{self.pid}"

Base.metadata.create_all(ENGINE)
Session=sessionmaker(bind=ENGINE)
sess=Session()

while True:
    print("Select Operation--\n1.INSERTION\n2.UPDATION\n3.DELETION\n4.DATA RETRIVE\n5.EXITLOOP")
    ch=int(input('Enter your choice-'))
    if ch==1:
        print('Selct table\n1.person\n2.license_info')
        ch=int(input('Enter your choice-'))
        if ch==1:
            pid=int(input('Enter pid-'))
            name=input('Enter name-')
            city=input('Enter city-')
            p=Details(pid=pid,name=name,city=city)
            
            sess.add(p)
        elif ch==2:
            lid=int(input('Enter lid-'))
            li_no=input('Enter pid-')
            pid=int(input('Enter pid-'))
            l=License(lid=lid,li_no=li_no,pid=pid)

            sess.add(l)

    elif ch==2:
         print('Selct table\n1.person\n2.license_info')
         ch=int(input('Enter your choice-'))
         if ch==1:
             new_pid=int(input('Enter pid-'))
             sess.query(Details).filter(Details.name=='Akshay').update({Details.pid:new_pid})

    elif ch==3:
        sess.query(Details).filter(Details.pid==2).delete()

    elif ch==4:
        print('Selct table\n1.person\n2.license_info')
        ch=int(input('Enter your choice-'))
        if ch==1:
            var1=sess.query(Details)
            for i in var1:
                print(i)

        elif ch==2:
            var2=sess.query(License)
            for i in var2:
                print(i)
        
        
    elif ch==5:
        break
    sess.commit()
sess.close()



'''
'''
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL="mysql://root:root@localhost:3306/new12"

ENGINE=create_engine(URL)
Base=declarative_base()

class Details(Base):
    __tablename__='person'
    pid=Column(Integer,primary_key=True)
    fname=Column(String(20))
    lname=Column(String(20))

    def __str__(self):
        return f"{self.pid},{self.fname},{self.lname}"

class License(Base):
    __tablename__='license_info'
    lid=Column(Integer,primary_key=True)
    li_no=Column(String(20))
    pid=Column(Integer,ForeignKey('person.pid',onupdate='CASCADE',ondelete='CASCADE'))

    def __str__(self):
        return f"{self.lid},{self.li_no},{self.pid}"

class Location(Base):
    __tablename__='mycity'
    cid=Column(Integer,primary_key=True)
    c_name=Column(String(30))
    pid=Column(Integer,ForeignKey('person.pid',onupdate='CASCADE',ondelete='CASCAde'))

    def __str__(self):
        return f"{self.cid},{self.c_name},{self.pid}"

Base.metadata.create_all(ENGINE)

Base.metadata.create_all(ENGINE)
Session=sessionmaker(bind=ENGINE)
sess=Session()

while True:
    print("Select Operation--\n1.INSERTION\n2.UPDATION\n3.DELETION\n4.DATA RETRIVE\n5.EXITLOOP")
    ch=int(input('Enter your choice-'))
    if ch==1:
        print('Selct table\n1.person\n2.license_info\n3.mycity')
        ch=int(input('Enter your choice-'))
        if ch==1:
            pid=int(input('Enter pid-'))
            fname=input('Enter fname-')
            lname=input('Enter lname-')
            p=Details(pid=pid,fname=fname,lname=lname)
            sess.add(p)
        elif ch==2:
            lid=int(input('Enter lid-'))
            li_no=input('Enter li_no-')
            pid=int(input('Enter pid-'))
            l=License(lid=lid,li_no=li_no,pid=pid)
            sess.add(l)
        elif ch==3:
            cid=int(input('Enter cid-'))
            c_name=input('Enter city name-')
            pid=int(input('Enter pid-'))
            m=Location(cid=cid,c_name=c_name,pid=pid)
            sess.add(m)

    elif ch==2:
         print('Selct table\n1.person\n2.license_info\n3.mycity')
         ch=int(input('Enter your choice-'))
         if ch==1:
             new_pid=int(input('Enter new pid-'))
             n=input('Enter fname whose pid is to updata')
             sess.query(Details).filter(Details.fname==n).update({Details.pid:new_pid})

    elif ch==3:
        p=int(input('Enter pid to delete-'))
        sess.query(Details).filter(Details.pid==p).delete()

    elif ch==4:
        print('Selct table\n1.person\n2.license_info\n3.mycity')
        ch=int(input('Enter your choice-'))
        if ch==1:
            var1=sess.query(Details)
            for i in var1:
                print(i)

        elif ch==2:
            var2=sess.query(License)
            for i in var2:
                print(i)
                
        elif ch==3:
            var3=sess.query(Location)
            for i in var3:
                print(i)
        
        
    elif ch==5:
        break
    sess.commit()
sess.close()

'''
'''
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import MySQLdb

URL="mysql://root:root@localhost:3306/new12"

ENGINE=create_engine(URL)
Base=declarative_base()

class Student(Base):
    __tablename__='stud'
    rn=Column(Integer,primary_key=True)
    fname=Column(String(20))
    lname=Column(String(20))

    def __str__(self):
        return f"{self.rn},{self.fname},{self.lname}"
    
class College(Base):
    __tablename__='colg'
    cid=Column(Integer,primary_key=True)
    c_name=Column(String(20))
    rn=Column(Integer,ForeignKey('stud.rn',onupdate='CASCADE',ondelete='CASCADE'))

    def __str__(self):
        return f"{self.cid},{self.c_name},{self.rn}"
    
class University(Base):
    __tablename__='univ'
    uid=Column(Integer,primary_key=True)
    u_name=Column(String(20))
    cid=Column(Integer,ForeignKey('colg.cid',onupdate='CASCADE',ondelete='CASCADE'))

    def __str__(self):
        return f"{self.uid},{self.u_name},{self.cid}"

Base.metadata.create_all(ENGINE)

Session=sessionmaker(bind=ENGINE)
sess=Session()

while True:
    print("Select Operation--\n1.INSERTION\n2.UPDATION\n3.DELETION\n4.DATA RETRIVE\n5.EXITLOOP")
    ch=int(input('Enter your choice-'))
    if ch==1:
        print('Selct table\n1.stud\n2.colg\n3.univ')
        ch=int(input('Enter your choice-'))
        if ch==1:
            rn=int(input('Enter roll no-'))
            fname=input('Enter fname-')
            lname=input('Enter lname-')
            s=Student(rn=rn,fname=fname,lname=lname)
            sess.add(s)

        elif ch==2:
            cid=int(input('Enter cid-'))
            c_name=input('Enter  college name-')
            rn=int(input('Enter rn-'))
            c=College(cid=cid,c_name=c_name,rn=rn)
            sess.add(c)

        elif ch==3:
            uid=int(input('Enter uid-'))
            u_name=input('Enter  University name-')
            cid=int(input('Enter cid-'))
            u=University(uid=uid,u_name=u_name,cid=cid)
            sess.add(u)

    elif ch==2:
        print('Selct table\n1.stud\n2.colg\n3.univ')
        ch=int(input('Enter your choice-'))
        if ch==1:
            sess.query(Student).filter(Student.rn==2).update({Student.rn:22})

    elif ch==3:
        print('Selct table\n1.stud\n2.colg\n3.univ')
        ch=int(input('Enter your choice-'))
        if ch==1:
            sess.query(Student).filter(Student.rn==2).delete()

    elif ch==4:
        print('Selct table\n1.stud\n2.colg\n3.univ')
        ch=int(input('Enter your choice-'))
        if ch==1:
            var=sess.query(Student)
            for i in var:
                print(i)

        elif ch==2:
            var=sess.query(College)
            for i in var:
                print(i)

        elif ch==3:
            var=sess.querry(University)
            for i in var:
                print(i)

    elif ch==4:
        break
    sess.commit()


    print(e)
sess.close()
    
'''






from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import MySQLdb

URL="mysql://root:root@localhost:3306/new12"

ENGINE=create_engine(URL)
Base=declarative_base()

class Student(Base):
    __tablename__='stud'
    rn=Column(Integer,primary_key=True)
    fname=Column(String(20))
    lname=Column(String(20))

    def __str__(self):
        return f"{self.rn},{self.fname},{self.lname}"
    
class College(Base):
    __tablename__='colg'
    cid=Column(Integer,primary_key=True)
    c_name=Column(String(20))
    rn=Column(Integer,ForeignKey('stud.rn'))

    def __str__(self):
        return f"{self.cid},{self.c_name},{self.rn}"
    
class University(Base):
    __tablename__='univ'
    uid=Column(Integer,primary_key=True)
    u_name=Column(String(20))
    cid=Column(Integer,ForeignKey('colg.cid'))

    def __str__(self):
        return f"{self.uid},{self.u_name},{self.cid}"

Base.metadata.create_all(ENGINE)

Session=sessionmaker(bind=ENGINE)
sess=Session()

class PrimaryKeyDuplicateError(Exception):
    def __init__(self,msg):
        self.msg=msg
        
try:
    print("Select Operation--\n1.INSERTION\n2.UPDATION\n3.DELETION\n4.DATA RETRIVE\n5.EXITLOOP")
    ch=int(input('Enter your choice-'))
    if ch==1:
        print('Selct table\n1.stud\n2.colg\n3.univ')
        ch=int(input('Enter your choice-'))
        if ch==1:
            rn=int(input('Enter roll no-'))
            fname=input('Enter fname-')
            lname=input('Enter lname-')
            s=Student(rn=rn,fname=fname,lname=lname)
            sess.add(s)
            raise PrimaryKeyDuplicateError('Cannot add duplicate entries to primary key')

        elif ch==2:
            cid=int(input('Enter cid-'))
            c_name=input('Enter  college name-')
            rn=int(input('Enter rn-'))
            c=College(cid=cid,c_name=c_name,rn=rn)
            sess.add(c)
            raise PrimaryKeyDuplicateError('Cannot add duplicate entries to primary key')

        elif ch==3:
            uid=int(input('Enter uid-'))
            u_name=input('Enter  University name-')
            cid=int(input('Enter cid-'))
            u=University(uid=uid,u_name=u_name,cid=cid)
            sess.add(u)

    elif ch==2:
        print('Selct table\n1.stud\n2.colg\n3.univ')
        ch=int(input('Enter your choice-'))
        if ch==1:
            sess.query(Student).filter(Student.rn==2).update({Student.rn:22})

    elif ch==3:
        print('Selct table\n1.stud\n2.colg\n3.univ')
        ch=int(input('Enter your choice-'))
        if ch==1:
            sess.query(Student).filter(Student.rn==2).delete()

    elif ch==4:
        print('Selct table\n1.stud\n2.colg\n3.univ')
        ch=int(input('Enter your choice-'))
        if ch==1:
            var=sess.query(Student)
            for i in var:
                print(i)

        elif ch==2:
            var=sess.query(College)
            for i in var:
                print(i)

        elif ch==3:
            var=sess.querry(University)
            for i in var:
                print(i)

    
    sess.commit()
    
except ValueError as e:
    print('Invalid Input',e)


except PrimaryKeyDuplicateError as msg:
    print(msg)
    
sess.close()
    




























