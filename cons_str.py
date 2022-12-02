class Student:
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name

    def __str__(self):
        return"Roll no:- {} and Name:- {}".format(self.rollno,self.name)

a=Student(1,'Akshay')
a1=Student(2,'Shelar')
print(a)
print(a1)
