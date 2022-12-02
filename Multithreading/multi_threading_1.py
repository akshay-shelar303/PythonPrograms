'''
from threading import Thread,currentThread

print('Program Starts',currentThread().name)

def evens():
    print('Evens fun starts')
    for i in range(0,20,2):
        print(i,currentThread().name)

def odds():
    print('Odds fun starts')
    for i in range(1,20,2):
        print(i,currentThread().name)

print('Program Ends',currentThread().name)

t1=Thread(target=evens)
t2=Thread(target=odds)

t1.start()
t2.start()
'''

'''
from threading import Thread,currentThread

print('Program Starts',currentThread().name)

def evens(start,end):
    print('Evens fun starts')
    for i in range(start,end,2):
        print(i,currentThread().name)

def odds(start,end):
    print('Odds fun starts')
    for i in range(start,end,2):
        print(i,currentThread().name)

t1=Thread(target=evens,name='evensThread',args=(0,20))
t2=Thread(target=odds,name='oddsThread',args=(1,20))

t1.start()
t2.start()

print('Program Ends',currentThread().name)
'''

'''
from threading import Thread,currentThread
print('Program Starts',currentThread().name)

def evens():
    print('Evens fun starts')
    for i in range(0,20,2):
        print(i,currentThread().name)

def odds():
    print('Odds fun starts')
    for i in range(1,20,2):
        print(i,currentThread().name)

print('Program Ends',currentThread().name)

t1=Thread(target=evens)
t2=Thread(target=odds)
t1.setName('evensThread')
t2.setName('oddsThread')

t1.start()
t2.start()
'''
'''
from threading import Thread,currentThread

def fun(start,end,ins):
    for i in range(start,end,ins):
        print(i,currentThread().name)

t1=Thread(target=fun,name='evensThread',args=(0,20,2))
t2=Thread(target=fun,name='odssThread',args=(1,20,2))

t1.start()

t1.join()

t2.start()
t2.join()

'''

from threading import Thread,currentThread

def fun(start,end,ins):
    for i in range(start,end,ins):
        print(i)
        
t1=Thread(target=fun,args=(2,21,2))
t2=Thread(target=fun,args=(4,41,4))

t1.start()
t1.join()

t2.start()
t2.join()























