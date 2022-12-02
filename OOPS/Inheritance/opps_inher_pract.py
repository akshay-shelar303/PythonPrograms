class A:
    def add(self,a,b):
        return a+b
class B(A):
    def m1(self):
        x=int(input('enter first value-'))
        y=int(input('Enter second value-'))
        self.add(x,y)
    def add(self,x,y):
        print(A.add(self,x,y))
    
        
b=B()
b.m1()
             
        
        
        
