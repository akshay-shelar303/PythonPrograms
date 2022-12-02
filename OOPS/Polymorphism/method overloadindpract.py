'''
class A:
    def mul(self,x=0,y=0,z=0):
        MUL=x*y*z
        if x!=0 and y!=0 and z!=0:
            MUL=x*y*z
            print("Multiplication is:-",MUL)
        elif x!=0 and y!=0:
            MUL=x*y
            print("Multiplication is:-",MUL)
        elif x!=0:
            MUL=x
            print("Multiplication is:-",MUL)
        else:
            
            print("Multiplication is:-",MUL)
            
a=A()
a.mul()
a.mul(2)
a.mul(10,2)
a.mul(10,2,3)
a.mul(1,1,1)
'''

'''
class A:
    def mul(self,*n):
        mul=1
        
        for i in n:
            mul*=i
        print("Multiplication is:-",mul)
            

a=A()
a.mul()
a.mul(2)
a.mul(10,2)
a.mul(10,2,3)

'''

'''
class A:
    def div(self,a=0,b=0):
        if a==0 and b==0:
            print("Invalid inputs")
            
        elif b==0:
            print("Cannot divide by zero")
        else:
            div=a/b
            print(div)
a=A()
a.div()
a.div(2,0)
a.div(4,2)
a.div(0,2)

'''
'''

class A:
    def sub(self,a=0,b=0,c=0):
        sub=a-b-c
        if a==0 and b==0 and c==0:
            print("You have not entered any inputs")
        else:
            print(sub)

           

a=A()
a.sub()
a.sub(2,3)
a.sub(10,5,2)
'''


class A:
    def sub(self,*n):
        sub=0
        for i in n:
            sub=sub-(i)
            if sub<0:
                sub=-sub
            else:
                sub=sub
        print(sub)

a=A()
a.sub()
a.sub(5,2)
a.sub(5,2,1)
a.sub(0,10,3,2,5)










































