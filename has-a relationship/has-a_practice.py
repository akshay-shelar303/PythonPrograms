'''
class Department:
    def __init__(self,deptid,deptname):
        self.deptid=deptid
        self.deptname=deptname
    def __str__(self):
        return "Department id:-{}\nDepartment Name:-{}".format(self.deptid,self.deptname)

class Employee:
    def __init__(self,empid,empname,empref):
        self.empid=empid
        self.empname=empname
        self.empref=empref
    def __str__(self):
        return "Employeeid:-{}\nEmployeename:-{}\nDepartment:-{}".format(self.empid,self.empname,self.empref)

d1=Department(1234,'Mechanical')
e1=Employee(12345,'Akshay',d1)
print(e1)
'''
    
class Department:
    def setDeptid(self,deptid):
        self.deptid=deptid
    def getDeptid(self):
        return self.deptid
    def setDeptname(self,deptname):
        self.deptname=deptname
    def getDeptname(self):
        return self.deptname

class Salary:
    def setSalamt(self,salamt):
        self.salamt=salamt
    def getSalamt(self):
        return self.salamt


class Employee:
    def setEmpid(self,empid):
        self.empid=empid
    def getEmpid(self):
        return self.empid
    def setEmpname(self,empname):
        self.empname=empname
    def getEmpname(self):
        return self.empname
    def setEmpref(self,empref):
        self.empref=empref
    def getEmpref(self):
        return self.empref
    def setSalref(self,salref):
        self.salref=salref
    def getSalref(self):
        return self.salref


d1=Department()
d1.setDeptid(1123)
d1.setDeptname('Mechanical')
s1=Salary()
s1.setSalamt('Rs.50000')

e1=Employee()
e1.setEmpid(12345)
e1.setEmpname('Akshay')
e1.setEmpref(d1)
e1.setSalref(s1)
print(e1.getEmpid())
print(e1.getEmpname())
print(e1.empref.getDeptid())
print(e1.empref.getDeptname())
print(e1.salref.getSalamt())
