'''
#1 update
d={1:'abc',2:'xyz',3:45}
d.update({4:(1,2),5:'aaa'})
print(d)

#2 pop
d.pop(2)
print(d)

#3 popitem
d2={1:'abc',2:'xyz',3:45}
d2.update({4:12})

d2.popitem()
print(d2)

#4 get
print(d2.get(2))

#5 clear --  empty the dict
d2.clear()
print(d2)


d4={1:'a',2:'b',3:'c',4:'d'}
print(d4)
d4.popitem()
print("after popitem",d4)


d5={1:'aa',2:'xy',3:'bb'}
d5.popitem()
print(d5)

d6=d5.copy()
print(d6)
'''
'''
d4={1:'a',2:'b',3:'c',4:'d'}

for i in d4:          
    print(i)

for i in d4.items():
    print(i)

for i,v in d4.items():
    print(i,'----',v)

for i in d4.keys():
    print(i)
 
for i in d4.values():
    print(i)

'''
'''
d={1:'a',2:'b',3:'c',4:'d'}
x=d.setdefault(3,'akki')
print(x)

y=d.setdefault(5,'akshay')
print(y)
print(d)

'''

l1=[1,2,3,4,5]
l2='a'
d=dict.fromkeys(l1,l2)
print(d)

t=1,2,3
t1='a','b'
d=dict.fromkeys(t,t1)
print(d)

r=range(1,5)
r1='ab'
d=dict.fromkeys(r,r1)
print(d)









    

















