class Student:
    def setRollno(self,rollno):
        self.rollno=rollno
    def getRollno(self):
        return self.rollno
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setAdr(self,adr):
        self.adr=adr
    def getAdr(self):
        return self.adr

class Address:
    def setCityName(self,cityname):
        self.cityname=cityname
    def getCityName(self):
        return self.cityname
    def setAreaName(self,areaname):
        self.areaname=areaname
    def getAreaName(self):
        return self.areaname

addr=Address()
addr.setCityName('Nashik')
addr.setAreaName('Camp')

stu=Student()
stu.setRollno(123)
stu.setName('Akshay')
stu.setAdr(addr)

print(stu.getRollno())
print(stu.getName())
print(stu.adr.getCityName())
print(stu.adr.getAreaName())



