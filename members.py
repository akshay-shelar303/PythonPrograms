class Members:
    def __init__(self,memno,name,dob,postaddress,contactno,email):
        self.memno=memno
        self.name=name
        self.dob=dob
        self.postaddress=postaddress
        self.contactno=contactno
        self.email=email

    def __str__(self):
            return "Memno:-{}\nName:-{}\nDateofbirth:-{}\nPostaddress:-{}\nContactno:-{}\nEmail:-{}".format(self.memno,self.name,self.dob,self.postaddress,self.contactno,self.email)
memno=int(input("Enter Membership number:-"))
name=input("Enter Full Name:-")
dob=input("Enter date of Birth:-")
postaddress=input("Enter postal address:-")
contactno=int(input("Enter contact number:-"))
email=input("Enter email:-")

m1=Members(memno,name,dob,postaddress,contactno,email)
print(m1)

m2=Members(memno,name,dob,postaddress,contactno,email)
print(m2)

m3=Members(memno,name,dob,postaddress,contactno,email)
print(m3)
