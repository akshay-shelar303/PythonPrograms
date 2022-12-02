##
##fh = open('C:/Users/DELL/Desktop/aaa.txt','r')
##data=fh.read()
##print(data)
##fh.close()


##l = [10,20,30,40,50]
####l.pop(6)           ---->IndexError
####l.remove(60)       ---->ValueError
##print(l.pop(3))
##print(l.remove(50))
##print(l)

##d = {"a":1,"b":2}
##print(d["a"])

##l = range(10)
##print(type(l),l)
##

'''
import random
for i in range(20):
    n = random.randint(1000,9999)
    print(n)
'''


##l = [1,2,0,3,0,4,5,0,6]
##
##for i in l:
##    if i == 0:
##        l.remove(i)
##        l.append(i)
##print(l)

'''
def myDecorator(fn):
    def inner_fun():
        print("My name is ",end='')
        fn()
    return inner_fun


@myDecorator
def greet():
            print("Akshay Shelar")

greet()

'''


#for finding max no of occurance
'''
l = [1,2,3,1,2,4,2,1,3,2,1,1,1]
d = dict()
for i in l:
    c = l.count(i)
    d[i]=c
max_value = max(d.values())
print(max_value)
##print(d.keys())
##print(d.values())
max_occur_num = list(d.keys())[list(d.values()).index(max_value)]
print(max_occur_num)
'''

'''
l = [1,2,3,1,2,4,2,1,3,2,1,1,1]
lc = []
for i in l:
    c = l.count(i)
    lc.append(c)
print(max(lc))

'''
'''
l = [1,2,3,4,5,[6,7,8]]
li = l[:]
print('l-->',id(l))
print('li-->',id(li))
print('l-->',l)
print('li-->',li)

li[5][0]=60
print('l-->',l)
print('li-->',li)
'''
'''
import math
num =-230
n = str(num)
if n[0] == '-':
    print('-',n[:0:-1])

else:
    print(n[::-1])

print(dir(math))
print(help(math))

'''
'''
import pickle

f = open("C:/Users/DELL/Desktop/newfile.txt","wb")

class MyData():
    def __init__(self,n):
        self.n = n

    def __str__(self):
        return f"{self.n}"
obj = MyData("Akshay")
pickle.dump(obj,f)
f.close()
'''

##class MyName():
##    _a = "Akshay"
##    __b = "Shelar"
##
##o = MyName()
##print(o._a)
##print(o.__b)



##from abc import ABC,abstractmethod
##class Parent(ABC):
##    @abstractmethod
##    def m1(self):
##        pass
##
##    @abstractmethod
##    def m2(self):
##        pass
##
##class Child1(Parent):
##    def m1(self):
##        print("child1 m1 method")
##    def m2(self):
##        print("child m2 method")
##
##class Child2(Child1):
##    def m2(self):
##        print('Child2 m2 method')
##    
##
##c2 = Child2()
##c2.m1()
##c2.m2()

'''
##Program to reverse number
n=int(input("Enter number: "))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("The reverse of the number:",rev)
'''

'''
#program to count number of digits
n=int(input("Enter number:"))
count=0
while(n>0):
    count=count+1
    n=n//10
print("The number of digits in the number is:",count)

'''
##
##n=int(input("Enter number:"))
##for i in range(11):
##    table = n*i
##    print(table)



'''
##comon elements between strings
s1 = input("Enter first strind:-")
s2 = input("Enter second strind:-")
s = set()
for i in s1:
    if i in s2:
        s.add(i)
print(s)
'''

'''
#prime number
num = int(input("Enter number :-"))

if num > 1:
    for i in range(2,(num//2)+1):
        if num % i == 0:
            print(num," is not prime number")
            break
    else:
        print(num, "is prime number")
else:
    print(num,"is not prime number")
        
'''




























