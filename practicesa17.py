'''
l1=[10,20,30,40]
l2=[100,200,300,400]
l2.sort(reverse=True)
l3=list(zip(l1,l2))

for i in l3:
   print(i)
 
'''
'''
l1=[10,20,30,40]
l2=[100,200,300,400]
l2.sort(reverse=True)
l3=list(zip(l1,l2))

for i in l3:
   for j in i:
       print(j)


'''


'''
for i in range(1,6):
    for j in range(6,0,-1):
        if j>i:
            print(' ',end='')
        else:
            print('*',end='')
    print()


'''

'''
l=[10,20,[300,400,[5000,6000],500],30,40]
l2=l[2]
l3=l2[2]
l3.append(7000)
#print(l3)
print(l)
'''
'''
l=[5,10,15,20,25,50,20]
x=l.index(20)

l.insert(x,200)
l.remove(20)
print(l)
'''

'''
l1=[]
l=[5,20,15,20,25,50,20]
for i in l:
    if i==20:
        l.remove(i)
        
print(l)

'''


l=[10,20,[300,400,[5000,6000],500],30,40]
l2=l[2]
print(id(l2[2]))
l3=l2[2]

l3.append(7000)
print(id(l3))
#print(l3)
print(l)















































