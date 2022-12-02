class Student:
    def setRollno(self,rollno):
        self.rollno=rollno

    def setName(self,name):
        self.name=name

    def getRollno(self):
        return self.rollno

    def getName(self):
        return self.name


s1=Student()
s1.setRollno(101)
s1.setName('Akshay')

s2=Student()
s2.setRollno(202)
s2.setName('Shelar')

print(s1.getRollno())
print(s1.getName())
print(s2.getRollno())
print(s2.getName())
