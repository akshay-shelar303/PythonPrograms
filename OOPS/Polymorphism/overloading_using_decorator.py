'''
from multipledispatch import dispatch
@dispatch(int,int)
def add(a,b):
    return a+b

@dispatch(int,int,int)
def add(a,b,c):
    return a+b+c

print(add(2,3))
print(add(2,3,4))

'''
'''

from multipledispatch import dispatch
class A:
    
    @dispatch(int,int)
    def add(a,b):
        return a+b

    @dispatch(int,int,int)
    def add(a,b,c):
            return a+b+c


a=A()
print(a.add(2,3))
print(a.add(2,3,4))
'''

from multipledispatch import dispatch
class A:
    @dispatch(str)
    def name(a):
        print(a)
        
    @dispatch(int,str,str)
    def name(a,b,c):
        print(a,b,c)

a=A()
a.name('Akshay')
a.name(30,'Akshay','Shelar')



































