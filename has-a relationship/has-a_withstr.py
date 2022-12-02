class Student:
    def __init__(self,rollno,name,adr):
        self.rollno=rollno
        self.name=name
        self.adr=adr
    def __str__(self):
        return "Roll no:-{}\nName:-{}\nAddress:-{}".format(self.rollno,self.name,self.adr)
    
class Address:
    def __init__(self,cityname,areaname):
        self.cityname=cityname
        self.areaname=areaname
    def __str__(self):
        return "Cityname:-{}\nAreaname:-{}".format(self.cityname,self.areaname)

addr=Address('Nashik','Camp')
stu=Student(123,'Akshay',addr)
print(stu)
