class Student:
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
    def __str__(self):
        return "Roll No:- {} and Name:- {}".format (self.rollno,self.name)
def rollno_sort(obj):
    return obj.rollno
def name_sort(obj):
    return obj.name

s1=Student(3,'aaa')
s2=Student(1,'ccc')
s3=Student(2,'bbb')
l=[s1,s2,s3]
for stu in l:
    print(stu)

print("Roll no wise sort")
l.sort(key=rollno_sort)
for stu in l:
    print(stu)

print("Name wise sort")
l.sort(key=name_sort)
for stu in l:
    print(stu)

