class A:
    def __init__(self,x):
        self.x=x

    def __add__(self,other):
        return self.x+other.x

    def __mul__(self,other):
        return self.x*other.x

a=A(100)
a1=A(200)
print(a+a1)

a2=A(300)
print(A(a+a1)+a2)

a4=A('Akshay')
a5=A('Shelar')
print(a4+a5)

print(a*a1)
