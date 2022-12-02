'''
class A:
    rn=0
    _name=''
    __marks=0

    def m1(self):
        print('__marks',self.__marks)

a=A()
print('rn variable-->',a.rn)
print('_name variable-->',a._name)

a.m1()


'''
'''
class A:
    def m1(self):
        print('m1---public')

    def _m2(self):
        print('_m2----protected')
        self.__m3()

    def __m3(self):
        print('__m3---private')

a=A()
a.m1()
a._m2()
'''
'''
class A:
    __rn=0                 #_A__rn      # _class__rn

    def __m1(self):
        print("m1----private")

a=A()
print(a._A__rn)         #Name Mangling
a._A__m1()
print(dir(A))


'''
'''
class A:
    __var=20
    __x='Akshay'
    __y=25

    def add(self):
        print('Addition-',10+20)
        print(self.__var)
        print(self.__x)
        print(self.__y)

    def _sub(self):
        print('Subtraction-',20-10)
        self.__mul()

    def __mul(self):
        print('Multiplication-',10*20)
        self.__div()
        
    def __div(self):
        print('Division_',10/2)
        

a=A()
a.add()
a._sub()
'''
'''
class A:
    __var=20
    __x='Akshay'
    __y=25

    def add(self):
        print('Addition-',10+20)
       
    def _sub(self):
        print('Subtraction-',20-10)
        
    def __mul(self):
        print('Multiplication-',10*20)
            
    def __div(self):
        print('Division_',10/2)
        

a=A()
print(a._A__var)
print(a._A__x)
print(a._A__y)

a.add()
a._sub()
a._A__mul()
a._A__div()

'''
'''
class A:
    __rn=1

    def setRN(self,n):
        self.__rn=n

    def getRN(self):
        return self.__rn

a=A()
a.setRN(500)
var=a.getRN()
print(var)
'''
'''
class Employee:
    __eid=0
    __fnmae=''
    __lname=''
    __city=''
    __pin=0

    def setEmpid(self,eid):
        self.__eid=eid
    def setFirstname(self,fn):
        self.__fname=fn
    def setLastname(self,ln):
        self.__lname=ln
    def setCity(self,c):
        self.__city=c
    def setPin(self,p):
        self.__pin=p

    def getEmpid(self):
        return self.__eid
    def getFirstname(self):
        return self.__fname
    def getLastname(self):
        return self.__lname
    def getCity(self):
        return self.__city
    def getPin(self):
        return self.__pin

e=Employee()
e.setEmpid(12)
e.setFirstname('Akshay')
e.setLastname('Shelar')
e.setCity('Nashik')
e.setPin(121345)

print(e.getEmpid())
print(e.getFirstname())
print(e.getLastname())
print(e.getCity())
print(e.getPin())
'''


class Student:
    __rn=0
    __fnmae=''
    __lname=''
    __subject=''
    __city=''

    def setRN(self,r):
        self.__rn=r
    def setFirstname(self,fn):
        self.__fname=fn
    def setLastname(self,ln):
        self.__lname=ln
    def setSubject(self,s):
        self.__subject=s
    def setCity(self,c):
        self.__city=c

    def getRN(self):
        return self.__rn
    def getFirstname(self):
        return self.__fname
    def getLastname(self):
        return self.__lname
    def getSubject(self):
        return self.__subject
    def getCity(self):
        return self.__city

s=Student()
ch=int(input('enter your choice-'))
if ch==1:
    rn=int(input("enter roll no-"))
    s.setRN(rn)
    print(s.getRN())
    
elif ch==2:
    fn=input("Enter first name-")
    s.setFirstname(fn)
    print(s.getFirstname())
    
elif ch==3:
    ln=input("Enter last name-")
    s.setLastname(ln)
    print(s.getLastname())
    
elif ch==4:
    s=input("Enter sunject -")
    s.setSubject(s)
    print(s.getSubject())
    
elif ch==5:
    c=input("Enter city name-")
    s.setCity(c)
    print(s.getCity())
    
else:
    print('Invalid inpur')




























































































