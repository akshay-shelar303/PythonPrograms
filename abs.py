class Calculator:
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)
    def mul(self,a,b):
        print(a*b)
    def div(self,a,b):
        print(a/b)
print("   Select choice   \n1.Additiob\n2.Subtraction\n3.Multiplication\n4.Division")
ch=int(input("enter your choice="))
a=float(input("Enter first value="))
b=float(input("Enter second value="))
c=Calculator()
if ch==1:
    c.add(a,b)
elif ch==2:
    c.sub(a,b)
elif ch==3:
    c.mul(a,b)
elif ch==4:
    c.div(a,b)

else:
    print("wrong choice")
