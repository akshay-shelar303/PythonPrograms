class Members:
    def __init__(self,memno,name,dob,postaddress,contactno,email):
        self.memno=memno
        self.name=name
        self.dob=dob
        self.postaddress=postaddress
        self.contactno=contactno
        self.email=email

    def __str__(self):
            return "Memno:-{} \n Name:-{} \n Dateofbirth:-{} \n Postaddress:-{} \n Contactno:-{} \n Email:-{}".format(self.memno,self.name,self.dob,self.postaddress,self.contactno,self.email)

m1=Members(1234,'Akshay Shelar','27 jan','malegaon',7768939268,'xyz@gmail.com')
print(m1)
m2=Members(213,'xyz','27april','abc',4579862545,'abc@gamil.com')
print(m2)
m3=Members(213,'xyz','27april','abc',4579862545,'abc@gamil.com')
print(m3)
