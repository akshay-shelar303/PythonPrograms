class Payment:
    def __init__(self,paymentid,firstname,lastname,dop,location,receiptno):
        self.paymentid=paymentid
        self.firstname=firstname
        self.lastname=lastname
        self.dop=dop
        self.location=location
        self.receiptno=receiptno
    def __str__(self):
        return"Paymentid:-{}\nFirstname:-{}\nLastname:-{}\ndop:-{}\nLocation:-{}\nReceiptno:-{}".format(self.paymentid,self.firstname,self.lastname,self.dop,self.location,self.receiptno)

p1=Payment(1234546,'Akshay','Shelar','7jan21','nashik',12345)
print(p1)

p2=Payment(1234,'Prashant','Shelar','20apr21','Malegaon',12345)
print(p2)

p3=Payment(1234546,'Akshay','Shelar','7jan21','nashik',12345)
print(p3)
