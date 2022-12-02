'''
class A:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        return self.x+other.x,self.y+other.y

       # return "Addition1:- {} \n Addition2:- {}".format(self.x+other.x,self.y+other.y)

            
a=A(10,20)
a1=A(30,40)
print(a+a1)

'''

'''
class A:
    def __init__(self,x):
        self.x=x
       

    def __mul__(self,other):
        return self.x*other.x

a=A(1)
b=A(2)
var1=a*b

      
c=A(3)
d=A(4)
var2=c*d

print(A(var1)*A(var2))



'''


class A:
    def __init__(self,x):
        self.x=x

    def __truediv__(self,other):       #division
        return self.x/other.x

    def __floordiv__(self,other):      #floor division
        return self.x//other.x

    def __mod__(self,other):           #Modulus
        return self.x%other.x
    
    def __pow__(self,other):        #Exponentiation
        return self.x**other.x

    def __gt__(self,other):          #Greaterthan
        return self.x>other.x

    def __lt__(self,other):         #lessthan
        return self.x<other.x

    def __et__(self,other):         #equalto
        return self.x==other.x

    def __le__(self,other):         #lessthan or equalto
        return self.x<=other.x

    def __ge__(self,other):         #graterthan or equalto
        return self.x>=other.x

    def __ne__(self,other):         #notequalto
        return self.x!=other.x

    def __lshift__(self,other):     #leftshift
        return self.x<<other.x

    def __rshift__(self,other):     #rightshift
        return self.x>>other.x

    def __and__(self,other):        #AND
        return self.x&other.x

    def __xor__(self,other):        #XOR
        return self.x^other.x

    def __or__(self,other):         #OR
        return self.x|other.x

a1=A(20)
a2=A(10)
print(a1/a2)
print(a1//a2)
print(a1%a2)
print(a1**a2)
print(a1>a2)
print(a1<a2)
print(a1==a2)
print(a1<=a2)
print(a1>=a2)
print(a1!=a2)
print(a1<<a2)
print(a1>>a2)
print(a1%a2)
print(a1^a2)
print(a1|a2)
































































