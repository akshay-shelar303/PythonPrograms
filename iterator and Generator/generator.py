'''
def m1():
    print('m1----1')
    yield 'Python'

    print('m1----2')
    yield'Java'

    print('m1-----3')
    yield 'Akshay'

    print('m1----end')

x=m1()
print(next(x))
print(next(x))
print(next(x))
print(next(x))

##for i in x:
##    print(i)

'''


def myrange(n):
    i=0
    while i < n:
        yield i
        i+=1

x=myrange(5)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

##for i in x:
##    print(i)







































