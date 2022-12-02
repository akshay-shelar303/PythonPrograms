'''
t=(1,2,3,4,5,6,7,8)
l=list(t)           # type casting
l.sort(reverse=True)
t=tuple(l)
print(t)
'''

t=(1,2,3,4,2,1,7,7,1,2)
l=list(t)
l.extend([9,10])
l.sort()
t=tuple(l)
print(t)
print(t.count(2))
print(t.index(2))
