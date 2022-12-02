class Customer:
    def __init__(self,cusid,name,amount,product):
        self.cusid=cusid
        self.name=name
        self.amount=amount
        self.product=product
    def __str__(self):
        return "Customer id:-{} Name:-{} Amount:-{} Product:-{}".format(self.cusid,self.name,self.amount,self.product)

def amount_sort(obj):
    return obj.amount

c1=Customer(1,'xy',1000,'abc')
c2=Customer(2,'aa',1500,'xyz')
c3=Customer(3,'bb',1200,'pqr')
c4=Customer(4,'cc',4000,'lmn')
c5=Customer(5,'xy',5000,'azy')
c=[c1,c2,c3,c4,c5]
for x in c:
    print(x)

print("after sort")
c.sort(key=amount_sort)
for x in c:
    print(x)
