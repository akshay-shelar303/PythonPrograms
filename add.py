def add(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

def mul(a,b):
    print(a*b)

def div(a,b):
    print(a/b)
    
print("___Select choice___\n""1.add\n""2.sub\n""3.mul\n""4.div")

ch=int(input("enter your choice"))

a=float(input("Enter first number "))
b=float(input("Enter second number "))

if ch==1:
      add(a,b)

elif ch==2:
      sub(a,b)

elif ch==3:               
      mul(a,b)

elif ch==4:
    div(a,b)

else:
      print("Wrong chice ")
   
