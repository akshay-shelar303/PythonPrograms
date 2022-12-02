class Student:
    def __init__(self,rollno,name,adr):
        self.rollno=rollno
        self.name=name
        self.adr=adr
class Address:
    def __init__(self,cityname,areaname):
        self.cityname=cityname
        self.areaname=areaname

addr=Address('Nashik','Camp')
stu=Student(123,'Akshay',addr)
print(stu.rollno)
print(stu.name)
print(stu.adr.cityname)
print(stu.adr.areaname)
