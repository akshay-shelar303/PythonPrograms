class Payment:
    def __init__(self,paymentid,firstname,lastname,amount,dop,location,receiptno):
        self.paymentid=paymentid
        self.firstname=firstname
        self.lastname=lastname
        self.amount=amount
        self.dop=dop
        self.location=location
        self.receiptno=receiptno
    def __str__(self):
        return"Paymentid:-{}\nFirstname:-{}\nLastname:-{}\nAmount\ndop:-{}\nLocation:-{}\nReceiptno:-{}".format(self.paymentid,self.firstname,self.lastname,self.amount,self.dop,self.location,self.receiptno)

paymentid=int(input("Enter paymentid:-"))
firstname=input("Enter first name:-")
lastname=input("Enter last name:-")
amount=input("Enter payment amount:-")
dop=input("Enter date of payment:-")
location=input("Enter payment location:-")
receiptno=int(input("Enter receipt no:-"))

p1=Payment(paymentid,firstname,lastname,amount,dop,location,receiptno)
print(p1)

