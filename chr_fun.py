'''
print(chr(65))
print(chr(66))
print(chr(70))
print(ord('a'))
'''
'''
x=65
while x<=69:
    print(chr(x),end='')
    x+=1
'''
'''

for i in range(65,70):
    for j in range (65,70):
        print(chr(j),end='')
    print()
'''
'''
for i in range(65,71):
    for j in range (65,71):
        print(chr(i),end='')
    print()
'''
'''
for i in range(1,7):
    for j in range (97,103):
        print(chr(j),end='')
    print()

'''
'''
l1=[1,2,3,4,5]
l2=['a','b','c','d']
l3=[l1,l2]
for i in l3:
    for x in i:
        print(x)
        
'''

t=(1,2,3,4,5)
l=list(t)
l.extend([1,2,8,9,5,5])
l.sort(reverse=True)
print(l)
#code for count of each element
for x in l:
    if x<=len(l):
        var=l.count(x)
    print("count of",x,"=",var)
    
#code for removing duplicate elements    
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)
t=tuple(l1)
print(t)





























