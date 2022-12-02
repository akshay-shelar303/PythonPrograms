'''
class PuneUniversity:
    def __init__(self,colid,colname):
        self.colid=colid
        self.colname=colname
    def __str__(self):
        return "College id:- {} , College name:- {}".format(self.colid,self.colname)

l=[]
c=[]
for x in range(1,6):
    colid=int(input("Enter college id:-"))
    colname=input("Enter college name:-")
    l.append(colid)
    c.append(colname)
d=dict(zip(l,c))
print(d) 
for k,v in d.items():
    p=PuneUniversity(k,v)
    print(p)

l=[]
l1=[]
for x in range(1,5):
    x=int(input('Enter first Value:-'))
    l.append(x)
print(l)
for y in range(1,5):
    y=input('Enter Second value:-')
    l1.append(y)

print(l1)
'''

'''
class CJC:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return "Name:-{}".format(self.name)
    
l=[]
for i in range(1,4):
    name=input("Enter name:-")
    l.append(name)
t=tuple(l)
for x in t:
    c=CJC(x)
    print(c)



'''

class Calculator:
    def add(self,a,b):
        add=a+b
        return(add)
    def sub(self,a,b):
        sub=a-b
        return sub
    def mul(self,a,b):
        mul=a*b
        return mul
    def div(self,a,b):
        div=a/b
        return div
c=Calculator()
a=int(input("Enter First value:-"))
b=int(input("Enter second Value:-"))
ch=int(input("Enter your choice:-"))
if ch==1:
    print(c.add(a,b))
elif ch==2:
    print(c.sub(a,b))
elif ch==3:
    print(c.mul(a,b))
elif ch==4:
    print(c.div(a,b))
else:
    print("Invalid Choice")
































































