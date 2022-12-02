d={}
d1=dict()
print(d, type(d))
print(d1, type(d1))


d2={1:'abc',2:'xyz',3:456}
print(d2)
print(d2[2])

d2[4]='aaa'
print(d2)

for k in d2:                 #iterate keys bydefault
    print("keys----",k)


for k in d2.keys():
    print("keys---",k)

for v in d2.values():
    print('values---',v)

for k,v in d2.items():
    print(k,'---',v)
