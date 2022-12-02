'''
def add():
    print("Addition-",10+20)

def sub():
    print("Subtraction-",50-20)

def mul():
    print('Multiplication-',10*50)

def div():
    print('division-',100/25)

add()
sub()
mul()
div()
'''
'''
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

print(add(10,20))
print(sub(100,50))
print(mul(20,10))
print(div(50,25))
'''
'''
def vote(age):
    if age > 18:
        print("eligible to vote")
    else:
        print("not eligible")

vote(20)
vote(10)
'''
'''
class Display:
    a = 10
    def add(self):
        print("add method")
    def __init__(self,myName):
        self.myName=myName
        print(myName)
        

d=Display("Akshay")
print(d.a)
d.add()
#Display.add(d)
d.x=10
print(d.x)

s=Display("Shelar")
s.x=200
print(s.x)
'''
'''
class Student:
    x = 10
    def m1(self):
        print("m1---Student")

s=Student()
print(dir(Student))

s.a=100
print(s.a)
print(dir(s))
'''
'''
class Animal:
    name = "Horse"
    color="white"

    def movement(self):
        print("run")

    def legs(self,x):
        self.x1=x
        print(self.x1)

    def pet(self):
        print("pet animal",self.name)

  

a=Animal()
print(a.name)
a.movement()
a.legs(4)
a.pet()
'''

'''
class Student:
    def __init__(self,f,l):
        self.fname=f
        self.lname=l

    def __str__(self):
        return f"First Name:-{self.fname} and Last Name:-{self.lname}"

s=Student("Akshay","Shelar")
print(s)
'''  

'''
class Addition:
    def __init__(self,x):
        self.x=x

    def __add__(self,other):
        return self.x+other.x

a1=Addition(10)
a2=Addition(20)
a3=Addition(30)

a4=Addition(a1+a2)
print(a4+a3)
'''

'''
class Display:
    def add(self,*a):
        mySum=0
        for i in a:
            mySum=mySum+i
        print(mySum)

d=Display()
d.add()
d.add(10)
d.add(10,20)
'''

'''
class A:
    def m1(self):
        print("m1----A")

class B(A):
    def m1(self):
        print("m1----B")

b=B()
b.m1()
'''
'''
class Display:
    def m1(self):
        print("m1----Display")

    def m2(self):
        print("m2----Display")

class Show:
    def m1(self):
        print("m1----Show")

    def m2(self):
        print("m2----Show")

def interface(obj):
    obj.m1()
    obj.m2()

    
d=Display()
s=Show()

interface(d)
interface(s)
'''
'''
class Student:
    m = 100
    _a = 200
    __name = "Akshay"

    def __m1(self):
        print("m1---prvate method")

s=Student()
print(s.m)
print(s._a)
print(s._Student__name)
s._Student__m1()

'''
'''
class Student:
    __rn = 0
    __name = ""

    def setRollno(self,r):
        self.__rn = r

    def setName(self,n):
        self.__name=n

    def getRollno(self):
        return self.__rn


    def getName(self):
        return self.__name

s=Student()
s.setRollno(1)
s.setName("Akshay")

print(s.getRollno())
print(s.getName())
'''
    

'''
from abc import ABC ,abstractmethod

class A(ABC):
    @abstractmethod
    def m1(self):
        pass

    def m2(self):
        print("m2---A")

class B(A):
    def m1(self):
        print("m1---B")

b=B()
b.m1()
b.m2()                          

'''


'''

try:
    print("try block start")
    div=10/0

except ZeroDivisionError as e:
    print("cannot divide by zero")

finally:
    print("finally block executed")
   
'''


'''
class AgeValidationError(Exception):
    def __init__(self,msg):
        self.msg = msg

def m1(age):
    if age < 0:
        raise AgeValidationError("invalid age")
    
try:
    m1(-2)

except AgeValidationError as e:
    print(e)

'''

def fun(num):
    print("The nummber is -",num)
    if num==0:
        raise ZeroDivisionError ("zero dividion")

try:
    fun(0)

except TypeError as e:
    print("give valid number of  arguments-",e)

except ZeroDivisionError as e:
    print("canot divide by zero",e)
    
except NameError as e:
    print("Name is not defined-",e)

























