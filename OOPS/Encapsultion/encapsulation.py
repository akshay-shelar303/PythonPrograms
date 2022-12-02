'''
class Encap:
    a=10            #public
    __b=20          #private

    def m1(self):
        print("m1--method")
        print(self.__b)
        self.__m2()
    def __m2(self):
        print("m2--method")

e=Encap()
print(e.a)
#print(e.__b)       #AttributeError
e.m1()
#e.__m2()           #AttributeError
'''

'''
class Student:
    rn=0
    name=''

s1=Student()
s1.rn=1
s1.name='Ram'
print(s1.rn)
print(s1.name)

s2=Student()
s2.rn=2
s2.name='Rahim'
s2.marks=20
print(s2.rn)
print(s2.name)
print(s2.marks)



class MyClass:
    a=10
    __b=20       #private

    def display(self):
        print(self.a)
        print(self.__b)
        
obj=MyClass()
obj.__b=200     #public
print(obj.__b)
obj.display()
'''
'''
class Student:
    __rn=0
    __name=''

    def update(self,r,n):
        self.__rn=r
        self.__name=n
    def display(self):
        print(self.__rn)
        print(self.__name)

s1=Student()
s1.display()
s1.update(1,'ram')
s1.display()
'''


class Student:
    __rn=0
    __name=''

    def setRn(self,r):
        self.__rn=r
    def setName(self,n):
        self.__name=n

    def getRn(self):
        return self.__rn
    def getName(self):
        return self.__name

s1=Student()
print(s1.getRn())
print(s1.getName())

s1.setRn(1)
s1.setName('Akshay')
print(s1.getRn())
print(s1.getName())
































