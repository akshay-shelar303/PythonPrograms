'''
#Single Inheritance
class Parent:
    def add(self):
        print("Addition-",20+30)
    def m1(self):
        print("m1----Parent")
        
class Child(Parent):
    def add(self):
        print("Addition-",30+40)

c=Child()
c.add()
c.m1


#2 Multilevel Inheritance

class College:
    def name(self):
        print("Collge Name -SCOE")

    def type(self):
        print("College type-Engineering")
        
class Department(College):
    def name(self):
        print("Mechanical Department")
        super().name()

class Student(Department):
    def name(self):
        print("Akshay Shelar")

    def type(self):
        print("Full time Student")
        super().name()
s= Student()
s.name()
s.type()


#Multiple Inheritance
class RBI:
    def rrate(self):
        print("RBI Interest rate is 7%")

    def amount(self):
        print("No minimum amount")

class SBI:
    def srate(self):
        print("SBI Interest rate is 10%")

class Bank(RBI,SBI):
    def rate(self):
        rate=int(input("Enter rate-"))
        if rate>=7:
            super().rrate()
        else:
            super().srate()

b=Bank()
b.rate()
b.amount()


#Hierarchical Inheritance

class CJC:
    def course(self):
        print("CJC privide multiple courses")
        

    def place(self):
        print("PUNE")

class Python(CJC):
    def course(self):
        print("Python corse by CJC")
    def made(self):
        print("Online Learning")

class Java(CJC):
    def course(self):
        print("JAve couse by CJC")
        super().course()

j=Java()
j.course()


#Hybrid Inheritance

class PC:
    def fun1(self):
        print('This is PC class')

class Laptop(PC):
    def fun2(self):
        print("This is Laptop class inheriting PC class")
        
class Mouse(Laptop):
    def fun3(self):
        print("This is Mouse class inheriting Laptop class")

class Student(Mouse, Laptop):
        def fun4(self):
            print("This Student class Inheriting Mouse and Laptop")
s=Student()
s.fun4()

'''
'''
#Polymorphism
#1 operator overloading
class A:
    def __init__(self,x):
        self.x=x

    def __add__(self,other):
        return self.x+other.x

    def __lt__(self,other):
        return self.x<other.x

a1=A(50)
a2=A(20)
print(a1+a2)
print(a1<a2)

print('----------------')

#2 Method Overloading
class A:
    def add(self,a=0,b=0,c=0):
        sum=a+b+c
        if a!=0 and b!=0 and c!=0:
            print(a+b+c)
        elif a!=0 and b!=0:
            print(a+b)
        elif a!=0:
            print(a)

        else:
            print("No inputs ")

a=A()
a.add()
a.add(10)
a.add(10,20)
a.add(10,20,30)

print('----------')

class B:
    def sub(self,*a):
        sub=0
        for i in a:
            
            sub=sub-i
            if sub>0:
                sub=sub
            else:
                sub=-sub
    
        print(sub)

b=B()
b.sub(5,2)
b.sub()
b.sub(5,2,1)
        
'''  
'''
#method Overriding
print('----method Overriding-----')

class Parent:
    def price(self):
        print('Before discount')

    
class Child(Parent):
    def price(self):
        print("Price after discount")
c=Child()
c.price()



#duck Typing
print("-----DUCK TYPING---")
class CAL1:
    def add(self):
        print("Addition of cal1-",10+20)

    def sub(self):
        print("Subtraction of cal1-",20-10)

class CAL2:
    def add(self):
        print("Addition of cal2-",100+200)

    def sub(self):
        print("Subtraction of cal2-",200-100)

def interface(obj):
    obj.add()
    obj.sub()

interface(CAL1())
interface(CAL2())
'''
'''
#Encapsulation

class Ecap:
    a=100
    __b='Akshay'

    def m1(self):
        print("m1--Public method")
        print(self.__b)
        self.__m2()

    def __m2(self):
        print("m2---private method")

e=Ecap()
e.m1()
print(e.a)



#Name Mangling
print("---Name Mangling---")
class Ecap:
    a=100
    __b='Akshay'

    def m1(self):
        print("m1--Public method")
        

    def __m2(self):
        print("m2---private method")

e=Ecap()
e.m1()
print(e.a)
print(e._Ecap__b)
e._Ecap__m2()



#setters and getters
print('----setters and getters----')
class Shop:
    __price=0
    __brand=''
    def setPrice(self,p):
        self.__price=p
        
    def setBrand(self,b):
        self.__brand=b

    def getPrice(self):
        return self.__price

    def getBrand(self):
        return self.__brand

s=Shop()
s.setPrice(1200)
s.setBrand('XYZ')

print(s.getPrice())
print(s.getBrand())

'''
'''
#ABSTRACTION
from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def age(self):
        pass

    def m1(self):
        print("m1---A")

class B(A):
    def name(self):
        print("Name of Student")

    def age(self):
        print("Age of Student")
b=B()
b.name()
b.age()
b.m1()





#by indirect subclass
class A(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def age(self):
        pass

    def m1(self):
        print("m1---A")

class B:
    def name(self):
        print("Name of Student")
        
A.register(B)
    
b=B()
b.name()
'''

#Comprehensions

#List Comprehension
l=[1,2,3,4,5,6]

li=[i*i*i for i in l if i%2==0]    #cube of even numbers
print(li)


#Set comprehensions
s={'absd','Akshay','Shelar','Pune'}

s_comp={i for i in s if len(i)>4}
print(s_comp)


#dict Comprehension
di={1:'a',2:'b',3:'d',4:'e',5:'f'}

d_comp={i:ord(v) for i,v in di.items()}
print(d_comp)









































