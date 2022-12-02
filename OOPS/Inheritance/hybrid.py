'''
#Multiple+Hirarchical
class A:
    def m1(self):
        print("m1---A")
        super().m1()

class B:
    def m1(self):
        print("m1---B")
    def m2(self):
        print("m2---B")

class C(A,B):
    def m1(self):
        print("m1---C")
        super().m1()
        
    def m3(self):
        print("m3---C")
        
class D(C):
    def m3(self):
        print("m3---D")

class E(C):
    def m1(self):
        print("m1---E")
        super().m1()
        D.m3(self)

e=E()
e.m1()
print(E.mro())
    
'''
'''

#hirarchical+multilevel

class Calculator:
    def m1(self):
        print("Calculator")

class Add(Calculator):
    def add(Self,a,b):
        print("Add-",a+b)
        
class Sub(Calculator):
    def sub(self,a,b):
        print("Sub-",a-b)

class Div(Sub):
    def div(self,a,b):
        print("Div-",a/b)

class Mul(Div):
    def mul(self,a,b):
        print("Mul-",a*b)
        super().div(a,b)

m=Mul()
m.mul(20,30)

'''


'''
#Multiple+Multilevel
class College:
    def name(self):
        print("College Name")

class Dept:
    def name(self):
        print("Departnament name")
    def deptid(self):
        print("Mech-1234")
        
class Student(College,Dept):
    def name(self):
        print("Akshay")
    def dept(self):
        print("Mechanical")

class District(Student):
    def name(self):
        print("Nashik")
        super().name()
        super().dept()

class City(District):
    def name(self):
        print("Malegaon")
        super().name()

c=City()
c.name()
    

'''

'''
#Multilevel+Multiple
class Company:
    def name(self):
        print("Hundai")
        
class Car(Company):
    def carname(self):
        print("Creta")
        
class Type(Car):
    def name(self):
        print("Suv")
        
class Owner:
    def name(self):
        print("Akshay")

class Info(Type,Owner):
    def info(self):
        print("Owner info")
        super().name()


i=Info()
i.info()


'''



#multilevel+hierarchical+multiple
class Add:
    def add(self,a,b):
        print("Addition-",a+b)
        
class Sub(Add):
    def sub(self,a,b):
        print("Subtraction-",a-b)
        super().add(a,b)

class Mul(Sub):
    def mul(Self,a,b):
        print("Multiplication-",a*b)
        super().sub(a,b)

class Div(Mul):
    def div(self,a,b):
        print("Division-",a/b)
        super().mod(a,b)

class Mod(Mul):
    def mod(self,a,b):
        print("Modulus-",a%b)
        super().mul(a,b)
        
class Calculator(Div,Mod):
    def cal(self,a,b):
        print("calculaor")
        super().div(a,b)

c=Calculator()
c.cal(10,20)
print(Calculator.mro())










































































































