class Product:
    def setProductid(self,productid):
        self.productid=productid
    def getProductid(self):
        return self.productid

    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name

    def setMfgdate(self,mfgdate):
        self.mfgdate=mfgdate
    def getMfgdate(self):
        return self.mfgdate

    def setExpirydate(self,expdate):
        self.expdate=expdate
    def getExpirydate(self):
        return self.expdate
    
    def setWeight(self,weight):
        self.weight=weight
    def getWeight(self):
        return self.weight

    def setComName(self,comname):
        self.comname=comname
    def getComName(self):
        return self.comname

productid=int(input("Enter Product id:-"))
name=input("Enter Product name:-")
mfgdate=input("Enter Product manifacturing date:-")
expdate=input("Enter Product Expiry date:-")
weight=input("Enter Product weight:-")
comname=input("Enter Company name:-")

p=Product()
p.setProductid(productid)
p.setName(name)
p.setMfgdate(mfgdate)
p.setExpirydate(expdate)
p.setWeight(weight)
p.setComName(comname)

print(p.getProductid())
print(p.getName())
print(p.getMfgdate())
print(p.getExpirydate())
print(p.getWeight())
print(p.getComName())
        
