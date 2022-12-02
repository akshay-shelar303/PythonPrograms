def add(a,b):
    print(a+b)

def sub(a,b,c):
    print(a-b-c)

def mul(a,b,c,d):
    print(a*b*c*d)

def div(a,b,c,d,e):
    print(a/b/c/d/e)

print("   Select choice   \n""1.Addition\n""2.Subtraction\n""3.Multiplication\n""4.Division")

ch=int(input("Enter your choice="))


if ch==1:
    a=int(input("Enter first value="))
    b=int(input("Enter second value="))
    add(a,b)

elif ch==2:
    a=int(input("Enter first value="))
    b=int(input("Enter second value="))
    c=int(input("Enter third value="))
    sub(a,b,c)

elif ch==3:
    a=int(input("Enter first value="))
    b=int(input("Enter second value="))
    c=int(input("Enter third value="))
    d=int(input("enter forth value="))

    mul(a,b,c,d)
    
elif ch==4:
    a=int(input("Enter first value="))
    b=int(input("Enter second value="))
    c=int(input("Enter third value="))
    d=int(input("enter forth value="))
    e=int(input("Enter fifth value="))
    div(a,b,c,d,e)

else:
    print("Wrong choice")
