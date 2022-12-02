def add(a,b):
    c=a+b
    print(c)

def sub(a,b):
    c=a-b
    print(c)

def mul(a,b):
    c=a/b
    print(c)

print("___select___\n""1. add\n""2. sub\n""3. mul")
      

ch=int(input("Enter your choice "))

if ch==1:
      add(100,200)

elif ch==2:
      sub(30,10)

elif ch==3:
      mul(50,30)

else:
      print("Wrong chice ")
