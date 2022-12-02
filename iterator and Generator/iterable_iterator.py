
'''
class Myrange:
    def __init__(self,n):
        self.n=n
        self.i=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i<self.n:
            x=self.i
            self.i+=1
            return x
        else:
            raise StopIteration()
y=Myrange(3)
print(next(y))
print(next(y))
print(next(y))
print(next(y))

'''



'''
class Myrange:                      #iterable class
    def __init__(self,n):
        self.n=n

    def __iter__(self):
        return Myrange_iter(self.n)
    

class Myrange_itr:                  #iterator class
    def __init__(self,n):
        self.n=n
        self.i=0


    def __next__(self):
        if self.i<self.n:
            x=self.i
            self.i+=1
            return x
        else:
            raise StopIteration

'''
'''
li=[1,2,3,4,5]
x=iter(li)
print(type(x))

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

'''
'''
#even nums

class Myrange:
    def __init__(self,n):
        self.n=n
        self.i=2
    def __iter__(self):
        return self

    def __next__(self):
        if self.i<self.n:
            x=self.i
            self.i+=2
            return x
        else:
            raise StopIteration('seqeunce exhausted')
x=Myrange(100)
for i in x:
    print(i)
'''

'''
#odd numbers
class Myrange:
    def __init__(self,n):
        self.n=n
        self.i=1
    def __iter__(self):
        return self

    def __next__(self):
        if self.i<self.n:
            x=self.i
            self.i+=2
            return x
        else:
            raise StopIteration('seqeunce exhausted')
x=Myrange(100)
for i in x:
    print(i)

'''

'''
x=20
y=iter(x)        #int cannot be 
print(next(y))
'''
'''
x='AKSHAY'
y=iter(x)
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))

'''
'''
class Myrange:
    def __init__(self,n):
        self.n=n
        self.i=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i<len(self.n):
            x=self.i
            self.i+=2
            return self.n[x]
        else:
            raise StopIteration('sequence exhausted')

x=Myrange('AKSHAYSHELAR')
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))


'''


'''
class Myrange:
    def __init__(self,start,stop,step):
        self.start=start
        self.stop=stop
        self.step=step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            var=self.start
            self.start=self.start+self.step
            return var
        
        elif self.start > self.stop:
            var=self.start
            self.start=self.start+self.step
            return var
        
        else:
            raise StopIteration()
        
start=int(input('Enter start value='))
stop=int(input('Enter stop value='))
step=int(input('Enter step value='))

x=Myrange(start,stop,step)
for i in x:
    print(i)

'''


l=[1,2,3]
print(l[-2:-1:-1])




























        
