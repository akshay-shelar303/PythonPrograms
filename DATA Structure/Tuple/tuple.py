t=(1,2,3,4,5)
print(t,type(t))

a=1,2,3,4,5
print(a,type(a))

t1=(1,)
print(t1)

t3=(10,20,30,40,50,60,70,70,80,90)
print(t3.index(40))
print(t3.count(70))
print(max(t3))
print(min(t3))
print(len(t3))
print(sum(t3))

t4=(10,20,30,40,50)
l=list(t4)
print(l)
l.append(60)
print(l)
t4=tuple(l)
print(t4)
