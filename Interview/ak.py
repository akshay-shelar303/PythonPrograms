##s = input("Enter String:-")
##
##l = []
##for i in s:
##    v = 0
##    n = 0
##    for j in range(ord('A'),ord(i)):
##        v = v + n
##        n += 1
##    l.append(v)
##print(l)
##total = 0
##for i in l:
##    total = total + i
##
##print(total)

##
##n = int(input("Enter n: "))
##i = 1
##flag = 0
##while i < 10000000:
##    if i == n:
##        i = i + 1
##        continue
##    if i % n == 0:
##        x = [int(a) for a in str(i)]
##        b = sum(x)
##        if b == n:
##            print("Value is:", i)
##            flag = 1
##            break
##    i = i + 1
##if flag == 0:
##    print(-1) 



##def func(n):
##    for i in range(n,1000000000,n):
##        a = str(i)
##        add = 0
##        for x in a:
##            add += int(x)
##        if add == n and n != i:
##            return i
##    return -1
##n = int(input("Enter n: "))
##print(func(n))
##
##

##def fib():
##    f =0
##    s= 1
##    li = [0,1]
##    for i in range(26):
##        t = f+s
##        f =s
##        s = t
##        li.append(t)
##    return li
##
##def func2(a):
##    add =0
##    li = fib()
##    for i in a:
##        num = ord(i)-65
##        add +=li[num]
##    return add
##
##print(func2("MAN"))
##
##






# def fun(name):
#     f = 0
#     s = 1
#     li = [0,1]
#     for i in range(24):
#         t = f+s
#         f = s
#         s = t
#         li.append(t)
#     add = 0
#     for i in name:
#         num = ord(i)-ord('A')
#         add += li[num]
#     return add
# name = input("Enter string:-")
# print(fun(name))




# def fib(n):
#     if n < 0:
#         raise ValueError('Negative numbers are not supported')
#     elif n == 0:
#         return 0
#     elif n <= 2:
#         return 1

#     return fib(n - 2) + fib(n - 1)

# print(fib(3))




# import copy
# l = [1,2,3,4,5,6,[5,8,4]]
# l1 = copy.copy(l)
# # l1 = copy.deepcopy(l)
# l1[6][0] = 15
# print("l = ",l)
# print("l1 = ",l1)


  

