class Account:
    def setAccno(self,accno):
        self.accno=accno
    def getAccno(self) :
        return self.accno

    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name

    def setOpeningdate(self,date):
        self.date=date
    def getOpeningdate(self):
        return self.date

    def setAmount(self,amount):
        self.amount=amount
    def getAmount(self) :
        return self.amount

    def setBranchname(self,branchname):
        self.branchname=branchname
    def getBranchname(self):
        return self.branchname

    def setCity(self,city):
        self.city=city
    def getCity(self):
        return self.city

accno=int(input("Enter Account number:-"))
name=input("Enter Account holder name:-")
openingdate=input("Enter Account opening number:-")
amount=input("Enter Amount:-")
branchname=input("Enter Branch name:-")
city=input("Enter City:-")

a=Account()
a.setAccno(accno)
a.setName(name)
a.setOpeningdate(openingdate)
a.setAmount(amount)
a.setBranchname(branchname)
a.setCity(city)

print(a.getAccno())
print(a.getName())
print(a.getOpeningdate())
print(a.getAmount())
print(a.getBranchname())
print(a.getCity())

 
