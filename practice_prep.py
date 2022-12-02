##import MySQLdb as m
##
##conn = m.connect('localhost','root','root','mydb')
##curs = conn.cursor()
##c = "create table student(rn int,name varchar(30))"
##
####curs.execute(c)
##
##i = "insert student values(1,'Akshay')"
##
##print(curs.execute(i))
##
##conn.commit()
##conn.close()

##
##import pickle
##
##class Student:
##    def __init__(self,rn,n):
##        self.rn = rn
##        self.n = n
##
##    def __str__(self):
##        return f"{self.rn} and {self.n}"
##
##s = Student(1,'Akshay')
##fh = open("C:/Users/DELL/Desktop/Templates/newfile.txt",'rb')
##
##obj = pickle.load(fh)
##print(obj)
##fh.close()




##import pickle
##list = [1,2,3,4,5,6,7,8,9]
##fh = open("C:/Users/DELL/Desktop/Templates/newfile.txt",'wb')
##pickle.dump(list,fh)
##fh.close()


##fh = open("C:/Users/DELL/Desktop/Templates/newfile.txt",'rb')
##l = pickle.load(fh)
##print(l)
##fh.close()

'''

from sqlalchemy import *
from sqlalchemy.orm import *

url = "mysql://root:root@localhost:3306/mydb"

engine = create_engine(url)

class Product:
    def __init__(self,pid,pname):
        self.pid = pid
        self.pname = pname

    def __str__(self):
        return f"{self.pid},{self.pname}"

md = MetaData()
st = Table("prod",md,Column('pid',Integer,primary_key=True),
           Column('pname',String(30)))

mapper(Product,st)
md.create_all(engine)
session = sessionmaker(engine)
sess = session()

p = Product(1,'Laptop')

p1 = Product(2,'Mobile')
p2 = Product(3,'Mouse')
sess.add_all([p1,p2])
##sess.add(p)

var = sess.query(Product)
for i in var:
    print(i)
sess.commit()
sess.close()

'''

'''
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import *

url = "mysql://root:root@localhost:3306/mydb"

engine = create_engine(url)
BASE = declarative_base()

class Info(BASE):
    __tablename__ = 'info'
    name = Column(String(30),primary_key=True)
    marks = Column(Float)

    def __str__(self):
        return f"{self.name} {self.marks}"


BASE.metadata.create_all(engine)
session = sessionmaker(bind=engine)
sess = session()


obj = Info(name='Akshay',marks=80)
sess.add(obj)
print('data added')
sess.commit()
sess.close()
'''


##
##import copy
##
##li = [10,20,30,[40,60]]
##cli = copy.copy(li)
##print('li-->',id(li[0]))
##print('cli-->',id(cli[0]))
##
##cli[3][0] = 200
##cli[0] = 100
##print('li-->',li)
##print('cli-->',cli)



##
##def mydecorator(fun):
##    def innerfun(a):
##        var = fun(a)
##        fullname = 'Akshay'+var
##        print('hi',fullname)
##        return fullname
##    return innerfun
##
##
##@mydecorator
##def myname(a):
##    return a
##
##myname('Shelar')
##
##    
##



##class Student:
##    __name = 'Akshay'
##    _r = 10
##
##s = Student()
##print(dir(Student))
##print(s._Student__name)


##from abc import ABC , abstractmethod
##class A(ABC):
##    @abstractmethod
##    def m1(self):
##        pass
##
##    @abstractmethod
##    def m2(seld):
##        pass
##
##class B(A):
##    def m1(self):
##        print('m1---B')
##
##class C(B):
##    def m2(self):
##        print('m2---C')
####        B.m1(self)
##        super().m1()
##
##
##c = C()
##c.m2()



##class InvalidPriceError(Exception):
##    def __init__(self,msg):
##        self.msg = msg
##
##def m1(p):
##    if p < 0:
##        raise InvalidPriceError("price must be grater than zero")
##    print(p)
##
##try:
##    m1(-1000)
##
##except InvalidPriceError as msg:
##    print(msg)
##    




##num = 2031
##rnum = 0
##while num > 0:
##    remainder = num % 10
##    rnum = (rnum*10)+remainder
##    num = num // 10
##if (len(str(num)) == len(str(rnum))):
##    print(rnum)
##else:
##    print('0'+str(rnum))



##s = "akshay"
##news = ''
##for i in s:
##    news = i+news
##
##print(news.upper())

##x = 20
##y = 30
##
##total = x+y
##x = total-x
##y = total-x
##print(x,y)

##class A:
##    def m1(self):
##        print('m1---A')
##    def m2(self):
##        print('m2---A')
##class B:
##    def m1(self):
##        print('m1---B')
##    def m2(self):
##        print('m2---B')
##
##def interface(obj):
##    obj.m1()
##    obj.m2()
##
##a = A()
##b = B()
##interface(a)
##interface(b)



##l = [1,2,3,1,4,5,2]
##li = []
##for i in l:
##    if i not in li:
##        li.append(i)
##
##print(li)
##


##l = [1,2,3,1,4,5,2]
##li = list(set(l))
##print(li)



##try:
##    div = 10/a
##except Exception as e:
##    print("cannot divide by zero",e)
##except ZeroDivisionError as e:
##    print("not divide by zero",e)


    

##class Singleton:
##   __instance = None
##   @staticmethod 
##   def getInstance():
##      """ Static access method. """
##      if Singleton.__instance == None:
##         Singleton()
##      return Singleton.__instance
##   def __init__(self):
##      """ Virtually private constructor. """
##      if Singleton.__instance != None:
##         raise Exception("This class is a singleton!")
##      else:
##         Singleton.__instance = self
##s = Singleton()
##print(s)
##
##s2 = Singleton.getInstance()
##print(s2)
##
##s3 = Singleton.getInstance()
##s3.data = 20
##print(s.data)
##
##print("s",id(s),"\ns2",id(s2))

##x = lambda a,b : a % b
##print(type(x))
##x(10,2)




##st = "0abc"
##x = st[0]
##if x.isdigit():
##    print(x,"is a number")
##else:
##    print(x,"is a character")




##st = "6abc"
##x = st[0]
##if x >= '0' and x <= '9':
##    print("number")
##else:
##    print("character")


##s = "akshay is my first name"
##w = s.split(' ')
##print(w)
##print('No of word in string is ',len(w))


##def myrange(n):
##    i = 1
##    while i < n:
##        if i % 2 == 0:
##            yield i
##        i += 1
##
##x = myrange(11)
##print(next(x))
##print(next(x))
##print(next(x))
##print(next(x))
##print(next(x))
##print(next(x))

##
##a1 = [1,3,4,7,9]
##a2 = [2,5,20,50]
##a3 = a1+a2
##print(a3)
##
##for i in range(len(a3)):
##    for j in range(len(a3)-1):
##        if a3[j] > a3[j+1]:      #ascending
##            temp = a3[j]
##            a3[j] = a3[j+1]
##            a3[j+1] = temp
##print("After sort",a3)




##import json
##di = {'name':'Alkshay','age':27}
##d = {'name':'Advik','age':1}
##print(type(d),d)
####json_obj = json.dumps(di)
####print(json_obj)



##def func(a):
##    num = [x for x in range(1,a+1)]
##    new = []
##    for _ in range(a-1):
##        for i in range(len(num)-1):
##            new.append(num[i]+num[i+1])
##        num = new.copy()
##        new =[]
##    return num[0]
##print(func(100))
##
##test_case = int(input("Number of cases: "))
##numbers = []
##for _ in range(test_case):
##    numbers.append(int(input("numbers: ")))
##
##

#Prine Number

##num = int(input("Enter number:-"))
##if num > 1:
##    for i in range(2,num):
##        if num % i == 0:
##            print(num,"is not prime number")
##            break
##    else:
##        print(num,"is prime number")
##       
##
##else:
##    print(num,"is not prime number")

##l = [1,5,40,20,6,8,9,100]
##for i in range(len(l)):
##    for j in range(len(l)-1):
##        if l[j] > l[j+1]:
##            temp = l[j]
##            l[j] = l[j+1]
##            l[j+1] = temp
##print(l)


##def sortFunction(l):
##    for i in range(len(l)):
##        for j in range(len(l)-1):
##            if l[j] > l[j+1]:
##                temp = l[j]
##                l[j] = l[j+1]
##                l[j+1] = temp
##    print(l)
##
##
##sortFunction([1,5,0,7,3,9,50])


##def myfun(num):
##    fact = 1
##    for i in range(1,num+1):
##        fact = fact * i
##    print(fact)
##
##myfun(50)




##
##names=['Deepak','Reema','John','Deepak','Munna','Reema','Deepak','Amit','John','Reema']
##d={}
##for i in range(len(names)-1):
##    x=names[i]
##    c=0
##    for j in range(i,len(names)):
##        if names[j]==names[i]:
##            c=c+1
##    count=dict({x:c})
##    if x not in d.keys():
##        d.update(count)
##print (d)
##


'''
new_string = ""
string = "aabbbccad"
count = 1
for i in range(len(string)-1):
    if string[i] == string[i+1]:
        count = count + 1
    else:         
        new_string =  new_string + string[i] + str(count)
        count = 1
new_string = new_string + string[i+1] + str(count)
print(new_string)
        

'''











