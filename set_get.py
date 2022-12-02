class A:
    def setCount(self,count):
        self.count=count
        
    def getCount(self):
        return self.count

a1=A()
a1.setCount(200)

a2=A()
a2.setCount(300)

print(a1.getCount())
print(a2.getCount())
