
from multipledispatch import dispatch
@dispatch(int,int)
def add(a,b):
    return a+b

@dispatch(int,int,int)
def add(a,b,c):
    return a+b+c

print(add(2,3))
print(add(2,3,4))
