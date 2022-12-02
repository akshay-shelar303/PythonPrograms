class Customer:
    def __init__(self,cusno,firstname,lastname,mobno,country):
        self.cusno=cusno
        self.firstname=firstname
        self.lastname=lastname
        self.mobno=mobno
        self.country=country

    def __str__(self):
        return"Customerno:-{}\nFirstname:-{}\nLastname:-{}\nMobileno:-{}\nCountry:-{}".format(self.cusno,self.firstname,self.lastname,self.mobno,self.country)

c=Customer(12,'Akshay','Shelar',8529637895,'India')
print(c)
        
    
