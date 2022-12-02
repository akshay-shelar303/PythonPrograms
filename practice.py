class A:
    def setParameters(self,no,name):
        self.no=no
        self.name=name

    def getParameters(self) :
        return self.no,self.name
a=A()
a.setParameters(12,'xyz')
print(a.getParameters())


    
