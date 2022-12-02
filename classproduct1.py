class Product:
    def display(self):
        print(self.productid)
        print(self.productname)
        print(self.expdate)
        print(self.weight)
        
print("product Details")
productid=int(input("Enter product id="))
productname=input("Enter product name=")
expdate=int(input("enter expiry date="))
weight=int(input("Enter product weight="))

p1=Product()
p1.productid
p1.productname
p1.expdate
p1.weight
p1.display()
   
