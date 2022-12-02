'''
from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        print("m2---A")

    def m4(self):
        print("m4----A")

class B(A):
    def m3(self):
        print("m3---B")

    def m1(self):
        print("m1---B")

    def m2(self):
        print("m2---B")

b=B()
b.m1()
b.m2()
b.m3()
b.m4()
'''
'''
from abc import ABC,abstractmethod

class Mobile(ABC):
    @abstractmethod
    def camera(self):
        pass

    @abstractmethod
    def crome(self):
        pass

class User(Mobile):
    def camera(self):
        print("Used to capture moments")

    def crome(self):
        print("used to browse")
u=User()
u.camera()
u.crome()

'''
'''   
from abc import ABC,abstractmethod

class A(ABC):                        
    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def sub(self):
        pass

    @abstractmethod
    def m1(self):
        pass

class B(A):                        
    def add(self):
        print("Addition-",2+3)

    def m1(self):
      print("m1---D")
      


class C(B):                       
    def sub(self):
        print("Subtraction-",10-5)
        super().add()
  
c=C()
c.sub()
'''
'''
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def name(self):
        pass

    

class Dog(ABC):
   @abstractmethod
   def move(self):
        pass
        
class Bird(Animal,Dog):
    def name(self):
        print("Bird name")

    def move(self):
        print("all can move")


b=Bird()
b.name()
b.move()
#d=Dog()
#d.name
'''    



'''
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def name(self):
        print("Dog name")

    def move(self):
        print("Dog can move")
        
class Bird(Animal):
    def name(self):
        print("Bird name")
    def move(self):
        print("Bird fly")

b=Bird()
b.name()
b.move()
#d=Dog()
#d.name
    
'''
'''
from abc import ABC,abstractmethod
class Country(ABC):
    @abstractmethod
    def name():
        pass
    
    @abstractmethod
    def code(self):
        pass
 
class State(Country):
    def name(self):
        print("Maharastra")

class City(State):
    def code(self):
        print("123")

class Info(City,State):
    def name(self):
        print("Information")
        super().code()

i=Info()
i.name()


'''

'''
from abc import ABC,abstractmethod
class Country(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def area(self):
        pass
class State(ABC):
    @abstractmethod
    def code(self):
        pass
    @abstractmethod
    def lang(self):
        pass   
class City(Country,State):
    def name(self):
        print("India")

    def area(self):
        print("Large area")
        
    
    def code(self):
        print("12")
       
class Town(City):
    def lang(self):
        print("Marathi")
        super().name()
class Village(City):
     def code(self):
        print("Marathi")
        super().name()
     def lang(self):
        print("Hindi")

v=Village()
v.code()

'''
'''
#Hierarchical+multiple
from abc import ABC,abstractmethod
class Calculator(ABC):
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def sub(self):
        pass
    
class Addition(Calculator):
##    def add(self):
##        print("Addition-",10+20)
##        super().add()
    def sub(self):
        print("Subtraction-",20-10)
        
class Subtraction(Calculator):
##    def add(self):
##        print("Adddition-",50+10)
    def sub(self):
        print("Subtraction-",40-20)
        
class Calculation(Addition,Subtraction):
    def add(self):
        print("addition")
        

c=Calculation()
c.add()
    
'''
'''
#Hierarchical+multilevel
from abc import ABC,abstractmethod
class Polygon(ABC):
    @abstractmethod
    def side(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Pentagon(Polygon):
    def side(self):
        print("5 sides")
    def area(self):
        print("Area of Pentagon")

class Square(Polygon):
    def side(self):
        print("4 sides")
    
class Triangle(Square):
    def area(self):
        print("Area of trangle")

class Final(Triangle):
    def area(self):
        print("Successfully implemented")
        super().side()
f=Final()
f.area()

'''

'''
#hierarchical+multiple+multilevel
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def name(self):
        pass
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def legs(self):
        pass
    
class Pet(Animal):
    def name(self):
        print("Pet animal name")
    def move(self):
        print("they can move")

class Wild(Animal):
    def legs(self):
        print("four legs")
    
class Dog(Pet,Wild):
    def legs(self):
        print("two legs")

class Pug(Dog):
    def name(self):
        print("Pub type dog")

class Bulldog(Pug):
    def move(self):
        print("walk ")

    def legs(self):
        print("four legs")
        
b=Bulldog()
b.move()
b.legs()
    
'''
'''
#MULTIPLE+MULTILEVEL+HIERARCHICAL
from abc import ABC,abstractmethod
class Bank(ABC):
    @abstractmethod
    def irate(self):
        pass
    @abstractmethod
    def minbal(self):
        pass

class Sbi(ABC):
    @abstractmethod
    def withlimit(self):
        pass
        
class Boi(Bank,Sbi):
    def withlimit(self):
        print("Withdraw limit 50000")
    def irate(self):
         print("5%")

class Bob(Boi):
    def minbal(self):
        
        print("20000")
class Gbank(Bob):
    def name(self):
        print("Graminbank")
        super().minbal()
        
class Bom(Gbank):
    def irate(self):
        print("rate is 10%")
class RBI(Gbank):
    
    def name(self):
        print("AKshay")
        super().name()

r=RBI()
r.name()
print(RBI.mro())

'''
#MULTILEVEL+HIERARCHICAL+MULTIPLE
from abc import ABC,abstractmethod
class University(ABC):
    @abstractmethod
    def name(self):
        pass
    @abstractmethod
    def coltype(self):
        pass
    @abstractmethod
    def exam(self):
        pass
class Pcollege(University):
    def name(self):
        print("SCOE")
    def coltype(self):
        print("Private engg college")
class Gcollege(Pcollege):
    def exam(self):
        print("Online exam")
        super().name()
        
class Depart(Gcollege):
    def name(self):
        print("Mechanical")
        super().exam()
        
class Grade(Gcollege):
    def type(self):
        print("Percentage sysytem")
        
class Section(Depart,Grade):
    def sec(self):
        print("Engineering Section")
        super().name()

s=Section()
s.sec()
print(Section.mro())





































