'''
a='PYTHON'
l=[]
for i in a:
    print(i)
    l.append(i)
print(l)

#using comprehension
li=[i for i in a]
print(li)
'''
'''
li=[1,2,3,4,2,5,6,5,6,2,2,8,9]
l=[]
for i in li:
    if i!=2:
        l.append(i)
print(l)

l_comp=[i for i in li if i!=2]
print(l_comp)

'''
'''
l=[]
for i in range(101):
    if i%2==0 and i%5==0:
        l.append(i)
print(l)

l_comp = [i for i in range(101) if i%2==0 and i%5==0]
print(l_comp)
'''
'''
l=[1,2,3,4,5,2,6,7,2]
#s=set(l)
s={i for i in l}
print(s)
'''
'''
l=[1,2,3,4,5,6,7,8,9,10]
s=set()
for i in l:
    if i%2==0:
        s.add(i)
print(s)
        
s_comp={i for i in l if i%2==0}
print(s_comp)
'''
'''
t=('Akshay','Akash','Sagar','Pooja','Oshin','Kapil','Aashish')
s=set()
for i in t:
    if len(i)<6:
        s.add(i)
print(s)

s_comp={i for i in t if len(i)<6}
print(s_comp)
'''
'''
di={}
for i in range(1,11):
    #di[i]=i*i
    di.update({i:i*i})
print(di)

d_comp={i:i*i for i in range(1,11)}
print(d_comp)
'''

dollar={'milk':1,'coffee':2.5,'bread':1.5}
rupee=74
newdi={}
for i,v in dollar.items():
    newdi[i]=rupee*v
print(newdi)

di={i:rupee*v for i,v in dollar.items()}
print(di)

























































        
    
