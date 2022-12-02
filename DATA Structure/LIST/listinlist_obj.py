class Student:
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
    def __str__(self):
        return 'Roll NO:- {} and Name:- {}'.format(self.rollno,self.name)

s1=Student(1,'xyz')
s2=Student(2,'abc')
mca1=[s1,s2]

s3=Student(3,'aaa')
s4=Student(4,'bbb')
mca2=[s3,s4]

mca=[mca1,mca2]

for stulist in mca:
    for stu in stulist:
        print(stu)
