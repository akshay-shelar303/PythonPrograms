li=[1,2,3,4,5,6,7,8,9,10]
#nornaml way
li_sqrs=[]
for i in li:
    s=i*i
    li_sqrs.append(s)
print(li_sqrs)

#using comprehension
l_sqrs=[i*i for i in li]
print(l_sqrs)


li=[1,2,3,4,5,6,7,8,9,10]

set_sqrs={i*i for i in li}
print(set_sqrs)

di_sqrs={i:i*i for i in li}
print(di_sqrs)


li_even=[i for i in li if i%2==0]
print(li_even)

li_evod=['ODD' if i%2!=0 else 'Even' for i in li]
print(li_evod)


set_evod={'ODD' if i%2!=0 else 'Even' for i in li}
print(set_evod)

di_evod={i:'ODD' if i%2!=0 else 'Even' for i in li}
print(di_evod)


l=[i**2 if i%2!=0 else i**3 for i in li]
print(l)
