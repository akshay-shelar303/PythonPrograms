class Employee:
    def __init__(self,empid,empname,empsal,city):
        self.empid=empid
        self.empname=empname
        self.empsal=empsal
        self.city=city
    def __str__(self):
        return "Empid:-{} Name:-{} Salary:-{} City:-{}".format(self.empid,self.empname,self.empsal,self.city)
e1=Employee(1,'xyz',50000,'pune')
e2=Employee(2,'abc',20000,'nashik')
e3=Employee(3,'pqr',21000,'aaa')
e4=Employee(4,'qwe',21452,'bbbb')
e5=Employee(5,'ab',12345,'cccc')
l=[e1,e2,e3,e4,e5]

for emp in l:
    print(emp)
    
print("after sort")
l.sort(key=lambda x:x.empid)
for emp in l:
    print(emp)
