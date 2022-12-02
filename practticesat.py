
def add(x,y,z):
    print("Addition=",x+y+z)
add(10,20,30)

class A:
    def m1(self,a,b,c):
        print("Addition=",a+b+c)
a=A()
a.m1(20,30,40)


def mul(a,b,c):
    print("Multiplication=",a*b*c)
mul(1,2,3)


class Akshay:
    def m3(self,x,y,z):
        if x==0 or y==0 or z==0:
            print("invalid input")
        else:
            print("Multiplication=",x*y*z)
x=int(input('Enter first no:-'))
y=int(input('Enter second no:-'))
z=int(input('Enter third no:-'))
a=Akshay()
a.m3(x,y,z)


def m4(p,q):
    print("Floor division=",p//q)
m4(50,20)

class D:
    def floor(self,p,q):
        print("Floor division=",p//q)
d=D()
d.floor(70,30)
