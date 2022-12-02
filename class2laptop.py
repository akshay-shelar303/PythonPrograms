'''
class Laptop:
    def display(self):
        print(self.lapid)
        print(self.lapname)
        print(self.ram)
        print(self.processor)
        print(self.modelno)

a1=Laptop()
a1.lapid=1234
a1.lapname="Dell"
a1.ram="6Gb"
a1.processor="i3"
a1.modelno="5010N"
a1.display()

a2=Laptop()
a2.lapid=1234
a2.lapname="Dell"
a2.ram="6Gb"
a2.processor="i3"
a2.modelno="5010N"
a2.display()

a3=Laptop()
a3.lapid=1234
a3.lapname="Dell"
a3.ram="6Gb"
a3.processor="i3"
a3.modelno="5010N"
a3.display()

a4=Laptop()
a4.lapid=1234
a4.lapname="Dell"
a4.ram="6Gb"
a4.processor="i3"
a4.modelno="5010N"
a4.display()

a5=Laptop()
a5.lapid=1234
a5.lapname="Dell"
a5.ram="6gb"
a5.processor="i3"
a5.modelno="5010N"
a5.display()
'''

# def mydecorator(fun):
#     def wrapper():
#         x = fun()
#         return x.lower()
#     return wrapper


# @mydecorator
# def myname():
#     return "AKSHAY"

# print(myname())


# def mygen(n):
#     while n < 10:
#         yield n+2
#         n += 2

# x = mygen(0)
# # print(x.__next__())
# for i in x:
#     print(i)


# def countVowels(s):
#     count = 0
#     for i in s:
#         if i.lower() in ['a','e','i','o','u']:
#             count += 1
#     return count
# s = input("Enter string:-")
# print(countVowels(s))



def fib(n):
    f = 0
    s = 1
    li = [0, 1]
    for i in range(n):
        t = f + s
        f = s
        s = t
        li.append(t)
    return li

x = fib(10)
print(x)


