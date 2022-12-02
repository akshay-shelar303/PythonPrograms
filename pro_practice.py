'''
def mydecorator(fun):
    def inner(a,b):
        if b == 0:
            print(0)
        else:    
            fun(a,b)
    return inner

@mydecorator
def divide(a,b):
    print(a/b)

divide(10,0)
'''
'''
def m1():
    try:
        print("try---start")
        return 100

    except ZeroDivisionError:
        print('Error occur')
        return 200

    else:
        return 200

    finally:
        return 400
        print("finally block--")
    
print(m1())
'''


##l = [10,50,6,7,50,90,100,30]
##for i in range(len(l)-1):
##    for j in range(0,len(l)-i-1):
##        if l[j] > l[j+1]:
##            l[j],l[j+1] = l[j+1],l[j]
##
##    print(l)
##    



##d1 = {6:3,9:2,8:1,7:4}
##l = list(d1.items())
##for i in range(len(l)-1):
##    for j in range(0,len(l)-i-1):
##        if l[j][1] > l[j+1][1]:
##            l[j],l[j+1] = l[j+1],l[j]
##print(l)
##d = {}
##for i in range(len(l)):
##    d[l[i][0]] = l[i][1]
##print(d)
##    


##l = [('yt',5),('fb',7),('yt',45),('google',6)]
##d = {}
##for i in range(len(l)):
##    for j in range(1+i,len(l)):
##        if l[i][0] == l[j][0]:
##            l1 = list(l[i])
##            l2 = list(l[j])
##            l1[1] += l2[1]
##            t1 = tuple(l1)
##            t2 = tuple(l2)
##            d[t1[0]] = t1[1]
##            d[t2[0]] = t1[1]
##else:
##    d[l[i][0]] = l[i][1]
##         
##print(d)
            

##
##l = [{'name':'Nandini','age':20},
##     {'name':'Manjeet','age':20},
##     {'name':'Nikhil','age':19}]
##
##for i in range(len(l)-1):
##    for j in range(0,len(l)-i-1):
##        if l[j]['age'] > l[j+1]['age']:
##            l[j],l[j+1] = l[j+1],l[j]
##print(l)




##
##n = 209
##rev = 0
##while n > 0:
##    digit = n % 10
##    rev = (rev*10) + digit
##    n = n // 10
##print(rev)


##f = 0
##s = 1
##li = [0,1]
##for i in range(100):
##    t = f+s
##    f = s
##    s = t
##    li.append(t)
##print(li[len(li)-1])
##



##num = int(input("Enter number:-"))
##
##if num > 1:
##    for i in range(2,num):
##        if num % i == 0:
##            print(num,"is not prime number")
##            break
##    else:
##        print("prime number")
##else:
##    print('not prime number')
##        
        

'''
import time
from threading import Thread

COUNT = 50000000

def countdown(n):
    while n>0:
        n -= 1

start = time.time()
countdown(COUNT)
end = time.time()

print('Time taken in seconds -', end - start)
'''
'''
import time
from threading import Thread

COUNT = 50000000

def countdown(n):
    while n>0:
        n -= 1

t1 = Thread(target=countdown, args=(COUNT//2,))
t2 = Thread(target=countdown, args=(COUNT//2,))

start = time.time()
t1.start()
t2.start()
##t1.join()
##t2.join()
end = time.time()

print('Time taken in seconds -', end - start)

'''




##l1 = [1,2,3,4]
##l2 = ['a','b','c','d']
##l3 = [f"{l1[i]}/{l2[i]}" for i in range(len(l1))]
##for i in range(len(l1)):
##    l3.append(f"{l1[i]}/{l2[i]}")
##
##print(l3)

'''
from threading import Thread
from time import sleep

def evenfun(n):
    for i in range(n):
        if i % 2 == 0:
            print(i)
def oddfun(n):
    for i in range(n):
        if i % 2 != 0:
            print(i)

t1 = Thread(target=evenfun ,args=(20,))
t2 = Thread(target=oddfun ,args=(20,))

t1.start()
t1.join()
t2.start()

'''


'''

class even:
    def __init__(self,x):
        self.x = x
        self.i = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.x:
            y = self.i*self.i
            self.i += 1
            return y
##        else:
##            raise StopIteration
##
e = even(3)
print(next(e))
print(next(e))
print(next(e))
print(next(e))

'''

'''
l = [1,2,3,4,1,2,5,1,4,3,3,3]
d = {}
count = 0
for i in range(len(l)):
    for j in range(i,len(l)):
        if l[j] == l[i]:
            count = count+1
    if l[i] not in d:
        d[l[i]] = count
    count = 0
for k,v in d.items():
    print(k,'is ',v,'times')
    
'''


s = 'aabbbcccddaa'
new_s = ''
count = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count = count + 1

    else:
        new_s = new_s + s[i] + str(count)
        count = 1
new_s = new_s + s[i+1] + str(count)

print(new_s)
    









































