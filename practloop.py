'''
for i in range(1,6):
    for j in range(1,6):
        print('*',end='')
    print()
'''
'''
for i in range(1,6):
    for j in range(1,i+1,1):
        print('*',end='')
    print()
'''
'''
for i in range(6,0,-1):
    for j in range(i,0,-1):
        print(j,end='')
    print()
'''
'''
for i in range(6,1,-1):
    for j in range(1,i,1):
        print(j,end='')
    print()
'''
'''
for i in range(1,6):
    for j in range(1,i+3,1):
        print(i,end='')
    print()
'''
n=0
for i in range(3,6):
    for j in range(i,i+3+n,1):
        print(j,end='')
    n=n+1
    print()
