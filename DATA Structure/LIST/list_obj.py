class Student:
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
s1=Student(1,'abc')
s2=Student(2,'xyz')
s3=Student(3,'pqr')

l=[s1,s2,s3]
for stu in l:
    print(stu.rollno)
    print(stu.name)
