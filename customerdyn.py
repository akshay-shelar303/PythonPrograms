class Customer:
    def __init__(self,cusno,firstname,lastname,mobno,country):
        self.cusno=cusno
        self.firstname=firstname
        self.lastname=lastname
        self.mobno=mobno
        self.country=country

    def __str__(self):
        return"Customerno:-{}\nFirstname:-{}\nLastname:-{}\nMobileno:-{}\nCountry:-{}".format(self.cusno,self.firstname,self.lastname,self.mobno,self.country)

cusno=int(input("Enter customer no:-"))
firstname=input("Enter first name:-")
lastname=input("Enter last name:-")
mobno=int(input("Enter customer mob no:-"))
country=input("Enter customer country")

c1=Customer(cusno,firstname,lastname,mobno,country)
print(c1)
