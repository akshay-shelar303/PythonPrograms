'''
class Brand:
    def __init__(self,brandid,brandname):
        self.brandid=brandid
        self.brandname=brandname
    def __str__(self):
        return "Brand Id:-{}\nBrand Name:-{}".format(self.brandid,self.brandname)

class Laptop:
    def __init__(self,lapid,lapname,lapram,lapref):
        self.lapid=lapid
        self.lapname=lapname
        self.lapram=lapram
        self.lapref=lapref
    def __str__(self):
        return "Laptop id:-{}\nLaptopname:-{}\nLaptopram:-{}\nBrand:-{}".format(self.lapid,self.lapname,self.lapram,self.lapref)

b=Brand(123,'Dell')
l=Laptop(12,'DellNseries','6Gb',b)
print(l)
'''


class Brand:
    def setBrandid(self,brandid):
        self.brandid=brandid
    def getBrandid(self):
        return self.brandid
    def setBrandname(self,brandname):
        self.brandname=brandname
    def getBrandname(self):
        return self.brandname

class Laptop:
    def setLapid(self,lapid):
        self.lapid=lapid
    def getLapid(self):
        return self.lapid
    def setLapname(self,lapname):
        self.lapname=lapname
    def getLapname(self):
        return self.lapname
    def setLapram(self,lapram):
        self.lapram=lapram
    def getLapram(self):
        return self.lapram
    def setLapref(self,lapref):
        self.lapref=lapref
    def getLapref(self):
        return self.lapref
    
b=Brand()
b.setBrandid(12)
b.setBrandname('dell')

l=Laptop()
l.setLapid(123456)
l.setLapname('dellnseries')
l.setLapram('6Gb')
l.setLapref(b)

print(l.getLapid())
print(l.getLapname())
print(l.getLapram())
print(l.lapref.getBrandid())
print(l.lapref.getBrandname())
