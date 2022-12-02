'''
#arithmatic operators
a=10
b=20
print('additiob',a+b)
print('subtraction',a-b)
print(a/b)
print(a*b)
print(a//b)
print(a%b)

'''
'''
class Student:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def __str__(self):
        return "First Name:-{}\nLast Name:-{}".format(self.fname,self.lname)

s=Student('Akshay','Shelar')
print(s)


'''

#sinfle level inheritance
'''
class College:
    def name(self):
        print('name of collge')

    def m1(self):
        print('m1---College')
        
class Student(College):
    def name(self):
        print('Name of Student')
    def branch(self):
        print('Branch name')

s=Student()
s.name()
s.m1()
s.branch()
'''


#multi-level inheritance
'''
class Car:
    def name(self):
        print('Car name is Fortuner')

    def price(self):
        print('HIgh price')

class Driver(Car):
    def name(self):
        print('Name of the driver')

class Brand(Driver):
    def name(self):
        print('name of the company')
        super().name()

b=Brand()
b.name()
b.price()
        
'''

#Multiple Inheritance
'''
class Country:
    def name(self):
        print('name Of Country Is India')
        super().name()

    def language(self):
        print('natinal langauage Hindi')

class State:
    def name(self):
        print('Maharastra')

    def language(self):
        print('Marathi')

class City:
    def name(self):
        print('Nashik')

class Village(Country,State,City):
    def name(self):
        print('Yesgaon')
        super().name()

v=Village()
v.name()
v.language()
'''
    


#Hierarchical Inheritance
'''
class Animal:
    def walk(self):
        print('Can walk')

    def type(self):
        print('tyoe of animal')

class Dog(Animal):
    def walk(self):
        print('dog can walk')

class Parrots(Animal):
    def walk(self):
        print('walk and fly')


p=Parrots()
p.walk()
p.type()
'''


#hybrid Inheritance
'''
class Cricket:
    def name(self):
        print('Cricket is most loved game')

    def role(self):
        print('Role of players')

class Batsman(Cricket):
    def name(self):
        print('name of the batsman')

    def role(self):
        print('batting')

class Bowler(Cricket):
    def role(self):
        print('bowler')

class Team(Batsman,Bowler):
    def name(self):
        print('India')

t=Team()
t.name()
t.role()
    
'''

#Polymorphism
#overloading
#operator Overloading
'''

class Cal:
    def __init__(self,x):
        self.x=x

    def __add__(self,other):
        return self.x+other.x

    def __lt__(self,other):
        return self.x<other.x

c1=Cal(10)
c2=Cal(5)
print(c1+c2)
print(c1<c2)
'''

#Method Overloading
'''
class A:
    def add(self,*x):
        add=0
        for i in x:
            add=add+i

        print(add)

a=A()
a.add()
a.add(1)
a.add(1,2)
a.add(1,2,3)
'''

#method overriding:
'''
class Parent:
    def m1(self):
        print('m1 plementaion')

class Child(Parent):
    def m1(self):
        print('Special m1 implementaion')

c=Child()
c.m1()
'''


#Duck Typing
'''
class A:
    def add(self):
        print(10+20)
    def sub(self):
        print(20-10)

class B:
    def add(self):
        print(100+200)
    def sub(self):
        print(200-100)

def interface(obj):
    obj.add()
    obj.sub()

interface(A())
interface(B())

'''

#Encapsulation
'''
class A:
    x=10
    _y=20
    __z=30

    def m1(self):
        print('PuBlic Method')

    def __m2(self):
        print('Private method')

a=A()
print(a.x)
print(a._y)
a.m1()
#a.__m2()    #error
'''


#Name Mangling
'''
class A:
    x=10
    _y=20
    __z=30

    def m1(self):
        print('PuBlic Method')

    def __m2(self):
        print('Private method')

a=A()
print(a.x)
print(a._y)
print(a._A__z)
a._A__m2()

'''


'''
class Student:
    __stuid=0
    __name=''

    def setStuid(self,stuid):
        self.__stuid=stuid

    def setName(self,n):
        self.__name=n

    def getStuid(self):
        return self.__stuid

    def getName(self):
        return self.__name

s=Student()
s.setStuid(123)
s.setName('Akshay')
print(s.getStuid())
print(s.getName())
'''
#Abstraction
'''
from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass
    
class Child(A):
    def m1(self):
        print('m1----child')

    def m2(self):
        print('m2---child')


c=Child()
c.m1()
c.m2()

'''

#by indirect subclass of abstract class
'''
from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass
    
class Child:
    def m1(self):
        print('m1----child')

A.register(Child)
c=Child()
c.m1()

'''

#iterator
'''
class A:
    def __init__(self,n):
        self.n=n
        self.i=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.n:
            x=self.i
            self.i+=1
            return x*x
        else:
            raise StopIteration

a=A(11)
for i in a:
    print(i)




#Generator

def m1():
    x=0
    while x<11:
        yield x**3
        x+=1

y=m1()
for i in y:
    print(i)
'''

'''
try:
    def m1():
        a=int(input('Enter first value-'))
        b=int(input('Enter second value-'))
        div=a/b
        print('division-',div)
        add=x+b
        print(add)

    m1()
except ZeroDivisionError as e:
    print('cannot divide by zero',e)

except ValueError as e:
    print('invalid input',e)

except NameError as e:
    print('name is not defined',e)
    try:
        m1().x=20
    except Exception as e:
        print('Exception occur',e)

else:
    print('no exception')

finally:
    print('Finally block executed')

'''
'''
class ZeroDivisionError(Exception):
    def __init__(self,msg):
        self.msg=msg

class InvalidAgeError(Exception):
    def __init__(self,msg):
        self.msg=msg
try:
    def m1():
        a=int(input('Enter first value-'))
        b=int(input('Enter second value-'))
        if b==0:
            raise ZeroDivisionError('cannot divide by zero')
        else:
            print('Division',a/b)

        age=int(input('Enter your age-'))
        if age <= 0:
            raise InvalidAgeError('age input is wrong')
    m1()
except ZeroDivisionError as msg:
    print(msg)

except InvalidAgeError as msg:
    print(msg)


'''
'''
#list
print('\n append method')
l=[1,2,3,4]
l.append(6)
print(l)

print('\n extend method')
l1=[1,2,3,4]
l1.extend([5,6,7])
print(l1)


print('\n insert method')
l2=[1,2,3,4]
l2.insert(2,'akshay')
print(l2)

print('\n pop method')
l3=['aa','bb','cc']
l3.pop(2)
print(l3)

print('\n remove method')
l4=['a',1,2,4]
l4.remove(4)
print(l4)


print('\n index method')
l5=[1,2,3,4]
print(l5.index(3))


print('\n count method')
l6=[1,2,3,4,1,5,1,6,1,1]
print(l6.count(1))


print('\n sort method')
l7=[1,6,5,7,9,2,3,4]
l7.sort()
print(l7)
l7.sort(reverse=True)
print(l7)

print('\n sorted method')
l8=[2,5,9,7,1,3]
l9=sorted(l8)
print(l9)
'''
#list comprehension
'''
l=['a','b','c','d']
li=[i.capitalize() for i in l]
print(li)


'''
'''
for i in range(1,10):
    print(i)
    if i==3:
        break
        '''  
'''
for i in range(1,10):
    print(i)
    print('i printed')
    if i==3 or i==5:
        continue
    print('end')
    print()
'''
'''

for i in ['a','b','c','d']:
##    print(i.capitalize())
    if i=='c':
        break
    print(i.capitalize())
'''

'''
for i in ['a','b','c','d']:
    print(i)
    if i=='c' or i=='d':
        continue
    print(i.capitalize())

'''


i=0
while True:
    print('---')
    if i==10:
        i+=1
        continue
    if i==20:
        break
    print(i)
    i+=1
        






















