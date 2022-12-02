#multithreading by inheriting Thread class
'''
from threading import Thread,currentThread
class Display(Thread):
    def run(self):
        for i in range(0,20,2):
            print(i,currentThread().name)

d=Display()
d.setName('EvensThraed')
d.start()
'''

'''
from threading import Thread,currentThread

class Display(Thread):
    def __init__(self,e):
        Thread.__init__(self)
        self.end=e
        
    def run(self):                       #run() is complusory 
        for i in range(2,self.end,2):
            print(i,currentThread().name)

t=Display(20)
t.setName('evensThread')
t.start()
'''

'''
from threading import Thread
class Display(Thread):
    def __init__(self,s,e,inc):
        Thread.__init__(self)
        self.s=s
        self.end=e
        self.inc=inc
        print(self.inc)

    def run(self):
        for i in range(self.s,self.end,self.inc):
            print(i)

t=Display(2,20,2)
t.start()

'''

#Thread Synchronisation
'''
from threading import Thread,currentThread,Lock
from time import sleep
l=Lock()
def greet(msg,s):
    for i in range(6):
        l.acquire()
        print('[')
        print(msg)
        print('[')
        sleep(s)
        l.release()

t1=Thread(target=greet,args=('Python',0))
t2=Thread(target=greet,args=('Java',0))

t1.start()
t2.start()

'''

from threading import Thread,currentThread,Lock
from time import sleep
l=Lock()
class Display(Thread):
    def __init__(self,msg,s):
        self.msg=msg
        self.s=s
        Thread.__init__(self)
        
    def run(self):
        for i in range(6):
            l.acquire()
            print('[')
            print(self.msg)
            print(']')
            sleep(self.s)
            l.release()

t1=Display('Python',0)
t2=Display('Java',0)

t1.start()
t2.start()



