class A:
    def add(self,x,y):
        return x+y
    def sub(self,x,y):
        return x-y
    def mul(self,x,y):
        return x*y
    def div(self,x,y):
        return x/y

class B(A):
    def m(self):
        x=int(input('Enter first value-'))
        y=int(input('Enter second value-'))
        self.add(x,y)
        self.sub(x,y)
        self.mul(x,y)
        self.div(x,y)
    def add(self,x,y):
        print('Addition',A.add(self,x,y))
        #print(super().add(x,y))      # by using super function
    def sub(self,x,y):
        print('Subtraction-',A.sub(self,x,y))
        
    def mul(self,x,y):
        print('Multiplication-',A.mul(self,x,y))

    def div(self,x,y):
        print('Division',A.div(self,x,y))

s=B()
s.m()







































