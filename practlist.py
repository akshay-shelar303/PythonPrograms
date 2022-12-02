''' li=[4,2,3,1,9,8,7,6,5]
li.sort(reverse=True)
print(li)
'''

'''
li=[4,2,3,1,9,8,7,6,5]
print(li)
x=sorted(li)
print(x)


l=[1,2,3,4,5]
l2=['abc','xyz']
l.append(l2)
print(l)
'''
'''
li=[1,2,3,'abs']
x=li.copy()
print(x)
print(id(li))
print(id(x))
'''

li=[4,4,3,2,1,9,7,6,4,3,2,5,5]
print(li)
li1=[]
for i in li:
    if i not in li1:
        li1.append(i)
print(li1)
li1.sort(reverse=True)
print(li1)

