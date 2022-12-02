class Product:
    def __init__(self,proid,proname):
        self.proid=proid
        self.proname=proname
    def __str__(self):
        return "Productid:-{}\nProductname:-{}".format(self.proid,self.proname)

class Company:
    def __init__(self,compid,compname,compref):
        self.compid=compid
        self.compname=compname
        self.compref=compref
    def __str__(self):
        return "Companyid:-{}\nCompanyname:-{}\nProduct:-{}".format(self.compid,self.compname,self.compref)

p=Product(123,'xyz')
c=Company(123456,'abc',p)
print(c)
