s={1,2,3,'abc',True}
print(s)

#add()
s.add(50)
print(s)

#remove
s.remove('abc')
print(s)

#discard()
s.discard(50)
print(s)

#pop()
s.pop()
print(s)

s1={1,2,3,4,8,'abs','aa'}
s1.update([10,20,30])
print(s1)

t=100,200
s1.add(t)
print(s1)

s1.remove(t)
print(s1)

s2=s1.copy()
print(s)
