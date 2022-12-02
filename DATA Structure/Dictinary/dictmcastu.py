class Student:
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
    def __str__(self):
        return "Roll No:- {} and Name:- {}".format(self.rollno,self.name)
s1=Student(1,'xyz')
s2=Student(2,'pqr')
mca1=[s1,s2]

s3=Student(3,'aaa')
s4=Student(4,'bbb')
mca2=[s3,s4]

mca={'MCA-1':mca1,'MCA-2':mca2}
for k,v in mca.items():
    print(k)
    for stu in v:
        print(stu)
