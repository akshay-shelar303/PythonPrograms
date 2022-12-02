class Calculator:
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)
    def mul(self,a,b):
        print(a*b)
    def div(self,a,b):
        print(a/b)

a=int(input("Enter first value="))
b=int(input("Enter second value="))
c=Calculator()
c.add(a,b)
c.sub(a,b)
c.mul(a,b)
c.div(a,b)
