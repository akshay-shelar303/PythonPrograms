'''
#1.Single  inheritance
class Student:
    def __init__(self,brname,colname):
        self.brname=brname
        self.colname=colname


    def __str__(self):
        return "Branch Name:-{} \nCollege Name:-{}".format(self.brname,self.colname)

class Display(Student):
    def stuinfo(self):
        print('Student Information')
        print(d)
        

d=Display('Mechanical','SCOE')

d.stuinfo()
'''





















'''

#2.Multilevel Inheritance

class University:
    def name(self):
        print("University name is SPPU")
    def location(self):
        print("Situated in Pune")
class College(University):
    def name(self):
        print("College name is SCOE")
        super().name()
    def ctype(self):
        print("Engineering college")
class Student(College):
    def name(self):
        print("Student name is Akshay")
        super().name()
    def branch(self):
        print("Mechanical")

s=Student()
s.name()
s.ctype()

'''
















'''



#3 Multiple Inheritance

class Calculation1:  
    def Summation(self,a,b):  
        return a+b;  
class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;  
class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  
d = Derived()  
print(d.Summation(10,20))  
print(d.Multiplication(10,20))  
print(d.Divide(10,20))  


'''




















'''

#4 Hierarchical Inheritance

class RBI:
    def rate(self):
        print("RBI Interest rate=7%")

class SBI:
    def rate(self):
        print("SBI Interest rate=9%")

class Bank(RBI,SBI):
    def show(self):
        Amount=int(input("Enter amount-"))
        if Amount<=200000:
            SBI.rate(self)
        else:
            super().rate()
b=Bank()
b.show()


'''


















#5.HYbrid Inheritance

class GrandPa:
    def __init__(self):
        print("Grand Pa")

class Father(GrandPa):
    def __init__(self):
        super().__init__()
        print("Father")

class Mother(GrandPa):
    def __init__(self):
        super().__init__()
        print("Mother")


class child(Father, Mother):
    def __init__(self):
        super().__init__()
        print("Child")

c = child()






























