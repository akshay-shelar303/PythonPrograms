'''
def m1():
    print('m1----Start')
    yield 'started'

    print('m1----end')
    return 'ended'

x=m1()
print(type(x))
print(next(x))
print(next(x))
'''



'''
def fun(n):
    while n<20:
        yield n
        n+=1
x=fun(1)
for i in x:
    print(i)
'''
'''
def even(n):
    i=0
    while i<=n:
        yield i
        i+=2
x=even(100)
for i in x:
    print(i)
'''
'''    
def odd(n):
    i=1
    while i<=n:
        yield i
        i+=2
x=odd(100)
for i in x:
    print(i)
'''
'''
def table(n):
    
    while n<=10:
        yield 2*n
        n+=1
x=table(1)
for i in x:
    print(i)

'''
'''
print('table for 3')
def table(n):
    while n<=10:
        yield 3*n
        n+=1
x=table(1)
for i in x:
    print(i)
    

print('table for 4')
def table(n):
    while n<=10:
        yield 4*n
        n+=1
x=table(1)
for i in x:
    print(i)




print('table for 5')
def table(n):
    while n<=10:
        yield 5*n
        n+=1
x=table(1)
for i in x:
    print(i)




print('table for 6')
def table(n):
    while n<=10:
        yield 6*n
        n+=1
x=table(1)
for i in x:
    print(i)




print('table for 7')
def table(n):
    while n<=10:
        yield 7*n
        n+=1
x=table(1)
for i in x:
    print(i)



print('table for 8')
def table(n):
    while n<=10:
        yield 8*n
        n+=1
x=table(1)
for i in x:
    print(i)


print('table for 9')
def table(n):
    while n<=10:
        yield 9*n
        n+=1

x=table(1)
for i in x:
    print(i)
    

print('table for 10')
def table(n):
    while n<=10:
        yield 10*n
        n+=1
x=table(1)
for i in x:
    print(i)
'''
'''
def fun():
    n=65
    while n<=90:
        yield chr(n)
        n=n+1
x=fun()
for i in x:
    print(i)

'''


'''
def lowercase():
    n=97
    while n<=122:
        yield chr(n)
        n+=1
x=lowercase()
for i in x:
    print(i)

'''
'''
def m1():
    print('m1----Start')
    yield 'started'

    print('m1----end')
    return 'ends here'

x=m1()
print(type(x))
print(next(x))
print(next(x))
print(x)

'''




















































    
