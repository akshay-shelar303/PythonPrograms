class Student:
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
    def __str__(self):
        return "Roll No:- {} and Name:- {}".format(self.rollno,self.name)
mca1=set()
s1=Student(1,'abs')
s2=Student(2,'xyz')

mca1.add(s1)
mca1.add(s2)

mca2=set()
s3=Student(3,'pqr')
s4=Student(4,'lmn')

mca2.add(s3)
mca2.add(s4)

fmca1=frozenset(mca1)
fmca2=frozenset(mca2)

mca={fmca1,fmca2}
for st in mca:
    for stu in st:
        print(stu)
