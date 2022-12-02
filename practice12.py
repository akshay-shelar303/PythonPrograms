def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)

print("Enter choice\n1.Addition\n21.Suntraction\n3.multiplication\n4.Division")
ch=int(input("Enter your choice="))

a=int(input("Enter first value="))
b=int(input("Enter second value="))
if ch==1:
    add(a,b)
elif ch==2:
    sub(a,b)
elif ch==3:
    mul(a,b)
elif ch==4:
    div(a,b)
else:
    print("invalid input")
