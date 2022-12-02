class Student:
    pass
class Address:
    pass

addr=Address()
addr.cityname='Nashik'
addr.areaname='Camp'

stu=Student()
stu.rollno=123
stu.name='Akshay'

stu.adr=addr

print(stu.rollno)
print(stu.name)
print(stu.adr.cityname)
print(stu.adr.areaname)

