class A:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        return self.x+other.x,self.y+other.y

a1=A(1,2)
a2=A(3,4)
a3=A(5,6)
a4=A(7,8)
a5=A(9,10)
a6=A(11,12)


p=a1+a2
q=a3+a4
r=a5+a6
var1=p+q
var2=var1+r

t=var2
t1=(t[0]+t[2]+t[4]),(t[1]+t[3]+t[5])

addition=tuple(t1)
print("Addition",addition)
    





