l1 = [1,2,3,3,4,4]
l2 = []

op = [1,2,999,999]
for i in range(len(l1)):
    if l1[i] == 3:
        l2.append(999)
    else:
        l2.append(l1[i])
print(l2)
'''
count = 1
for i in l1:
    if i not in l2:
        l2.append(i)
    else:
        l2.remove(i)
print(l2)
'''
'''
def sqfun(n):
    i = 1
    while i <= n:
        yield i**2
        i += 1

x =sqfun(10)
for i in x:
    print(i)
'''
n = int(input("enter number"))
l = ['prime number' for i in range(2,n) if n%i!=0 else'not peime' ]





























