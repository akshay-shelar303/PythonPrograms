'''
d5={1:'aa',2:'xy',3:'bb'}
d5.popitem()
print(d5)

l1=[1,2,3,4]
l2=('a','b','c','d')
x=zip(l1,l2)
print(dict(x))
#print(list(x))
#print(set(x))
'''


def display(d1,d2):
    x=d1.update(d2)
    return d1
d1={1:'a',2:'b',3:'c',4:'d'}
d2={5:'abc',6:'ab'}
merge=display(d1,d2)    
print(dict(merge))

