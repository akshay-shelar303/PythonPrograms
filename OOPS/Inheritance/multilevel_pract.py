'''
class Add:
    def m1(self,a,b):
        print("ADD---Add-",a+b)
        

class Sub:
    def m1(self,a,b):
        print("ADD----Sub-",a+b)
    
class Child(Add,Sub):
    def m1(self):
        a=int(input("Enter First value-"))
        b=int(input("Enter Second Value-"))
        ch=int(input("Enter your choice-"))
        if ch==1:
            Add.m1(self,a,b)
        elif ch==2:
            Sub.m1(self,a,b)
        else:
             print("Child---Add",a+b)
        

c=Child()

c.m1()
'''

class Addition:
    def add(self,a,b):
        print("Add-",a+b)

class Subtraction(Addition):
    def sub(self,a,b):
        print("Sub-",a-b)
        
class Multiplication(Subtraction):
    def mul(self,a,b):
        print("Mul-",a*b)
       

class Division(Multiplication):
    def div(self,a,b):
        print("Div-",a*b)
       
        
class Choice(Division):
    def ch(self):
        a=int(input("Enter First value-"))
        b=int(input("Enter second value-"))
        ch=int(input("Enter choice-"))
        if ch==1:
            c.add(a,b)
        elif ch==2:
            c.sub(a,b)
        elif ch==3:
            c.mul(a,b)
        elif ch==4:
            c.div(a,b)
        else:
            print("ibvalid choice")
        
c=Choice()
c.ch()






































