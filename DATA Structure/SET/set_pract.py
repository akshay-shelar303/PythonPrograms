'''
s={1,2,'a','b'}
s.add(99)
print(s)

s.update((10,20,30))
print(s)

li=list(s)
print(li)

li.extend(['x','y','z'])
print(li)

li.append(30)
print(li)

print(li.count(30))

t=tuple(li)
print(t)

print(t.index(30))

print(t.index('b'))

li1=list(t)
print(li1)

li1.extend([1,2,10,20,30])
print(li1)

s=set(li1)
print(s)
'''
'''
li=[1,2,3]
t=(10,20,30)
s=set()
print(type(s))

s.add(t)
print(s)

#print(s.add(li))

fli=frozenset(li)
print(type(fli))

for i in fli:
    s.add(i)
print(s)
'''
#union
s1={1,2,3,'a'}
s2={'a','b',3}
print("union:-",s1.union(s2))
print("union",s1|s2)   # | pipe operator

#Intersection
print("intersection-",s1.intersection(s2))
print('intersection:-',s1&s2)  

#difference
print('difference:-',s1.difference(s2))
print("Difference:-",s1-s2)
print(s2-s1)


#Symmetric difference
sm=s1.symmetric_difference(s2)
print("Symmetric difference:-",sm)
print(s1^s2)

#issubset
s3={1,2,3}
s4={1,2,3,4,5}
print(s3.issubset(s4))

#isdisjoint
a={1,2,3}
b={'a',5,6}
print(a.isdisjoint(b))


















