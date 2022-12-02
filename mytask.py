'''
1.Write a program that takes two strings as an input and checks whether 
the first character of first string is equal to last charater of second string
'''
#1 
##s1 = input("Enter first String:-")
##s2 = input("Enter last String:-")
##
##if s1[0] == s2[len(s2)-1]:
##    print("First charater of string s1 and last character of string s2 is equal")
##else:
##    print("not equal")
##
##

#2
##s1 = input("Enter first String:-")
##s2 = input("Enter last String:-")
##first = s1[0]
##if s1.startswith(first) and s2.endswith(first):
##    print("first and last character are same")
##else:
##    print("not same")
##    

'''
2.Write a program that takes string as an input and checks whether middle
character is 'd' or not if the middle charater is 'd' then it should
print message 'successful' otherwise 'unsuccessful'
'''
##s = input("Enter string:-")
##if len(s) % 2 != 0:
##    if s[(len(s)-1)//2] == 'd':
##        print("successfull")
##else:
##    print("unsuccessfull")




'''
3.Write a program that takes two strings as an input and
checks whether both are equal or not
'''
##s1 = input("Enter first String:-")
##s2 = input("Enter last String:-")
##if s1 == s2:
##    print("both strings are equal")
##else:
##    print("not equal")




'''
4.Write a program that takes string as an argument and it should
count occurances of 'a' in that string (without using an in-built method)
'''

##s = input("Enter string:-")
##count = 0
##for i in s:
##    if i == 'a':
##        count += 1
##print("The count of a is ",count)



'''
finally block
'''
##import os
##try:
##    print("try block ")
##    os._exit(0)
##    
##except:
##    print("except block")
##
##finally:
##    print("finally block")


'''
ip = [10,20,30,40,50,10,10,10,10,10,20,20,20,30,30]
def count(x):
    count = 0
    for i in ip:
        if i == x:
            count += 1
    return count
dup = dict()
dup_list = []
for i in ip:
    dup[i] = count(i)
    if i not in dup_list:
        dup_list.append(i)
print(dup)
print(dup_list)
'''

##ip = [10,20,30,40,50,10,10,10,10,10,20,20,20,30,30]


##
##dip = {'a':45,'b':20,'c':452,'d':90,'e':3,'f':200}
##op = {'c':452,'f':200,'d':90,'a':45,'b':20,'e':3}
##temp = 0
##d = dict()
##li = []
##print(dip)
##for i in dip.keys():
##    print(dip[i])
##    if dip[i] > temp:
##        temp = dip[i]
##        li.append(i)
##print(temp)
##print(li)
##    
##





dip = {'a':45,'b':20,'c':452,'d':90,'e':3,'f':200}
t = list(dip.items())
for i in range(len(t)):                   
    for j in range(len(t)-1):             
        if (t[j][1] < t[j + 1][1]): 
            temp = t[j] 
            t[j]= t[j + 1] 
            t[j + 1]= temp
print(t)
##dop = dict()
##for i in t:
##    dop[i[0]] = i[1]
dop = {i[0]:i[1] for i in t}
print(dop)



##1.len()
'''
def lenFun(x):
    length = 0
    for i in x:
        length += 1
    print(length)

lenFun([1,2,3,4,5])
    
'''


#2 sort()
'''
def sortFun(x):
    for i in range(len(x)-1):
        for j in range(0,len(x)-i-1):
            if x[j] > x[j+1]:     #descending order
                temp = x[j]
                x[j] = x[j+1]
                x[j+1] = temp
    print(x)

sortFun([2,4,3,6,7,8])
'''

##for i in range(5):
##    for j in range(i,5):
##        print('*',end='')
##    print()
##
##




       

































































