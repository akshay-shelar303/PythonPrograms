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

if ch==1:
    alculator().add(a,b)
elif ch==2:
    Calculator.sub(a,b)
elif ch==3:
    Calculator.mul(a,b)
elif ch==4:
    Calculator.div(a,b)

else:
    print("wrong choice")
