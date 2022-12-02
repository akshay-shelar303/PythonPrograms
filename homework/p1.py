'''
def practice(r,r1):
    print(dict.fromkeys(r,r1))
practice((range(1,4)),'a')

class Akshay:
    def func1(self,r,r1):
        print(dict.fromkeys(r,r1))
a=Akshay()
a.func1((range(1,5)),'b')
'''

def show(a,b):
    if a>b:
        print('a is grater')
    else:
        print('b is grater')
show(20,30)

class Akshay:
    def show(self,x,y):
        if x>y:
            print('x is grater')
        else:
            print('y is grater')
a=Akshay()
a.show(30,20)
