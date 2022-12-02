class Student:
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
    def __str__(self):
        return "Roll No:- {} and Name:- {}".format(self.rollno,self.name)

s=set()
s1=Student(1,'abs')
s2=Student(2,'xyz')

s.add(s1)
s.add(s2)
for stu in s:
    print(stu)
