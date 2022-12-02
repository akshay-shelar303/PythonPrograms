
class A:
    def m1(self,a=0,b=0,c=0):
        s=0
        if a!=0 and b!=0 and c!=0:
            s=a+b+c
            print(s)
        elif a!=0 and b!=0:
            s=a+b
            print(s)
        elif a!=0:
            print(a)
        else:
            print("No parameter value")

a=A()
a.m1()
a.m1(2)
a.m1(2,3)
a.m1(2,3,4)
a.m1('a','b','c')




#by using 'None'
class A:
    def m1(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
            print(s)
        elif a!=None and b!=None:
            s=a+b
            print(s)
        elif a!=None:
            print(a)
        else:
            print("No Parameter Value")


a=A()
a.m1()
a.m1(4)
a.m1(4,5)
a.m1(4,5,6)




















            
    
