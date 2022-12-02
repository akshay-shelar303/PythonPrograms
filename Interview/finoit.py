'''
class A:
    def __init__(self,s):
        self.s = s

    def print(self):
        print(s)

a = A("Welcome")
a.print()

##NameError: name 's' is not defined
'''


'''
t = ('abcd',786,2.23,'john',70.2)
print(t[1:3])
print(t[-1])
print(t[-1:])
print(t[5])
print(t[6])

##(786, 2.23)
##70.2
##(70.2,)
##Traceback (most recent call last):
##  File "D:\Python\Interview\finoit.py", line 19, in <module>
##    print(t[5])
##IndexError: tuple index out of range
'''


s = '1251263254812454586503'
##d = {}
##for i in range(len(s)-1):
##    k = s[i]
##    v = 0
##    for j in range(i,len(s)):
##        if s[j] == s[i]:
##            v += 1
##    count = dict({k:v})
##    if k not in d:
##        d.update(count)
##print(d)    

d = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
for i in s:
    d[i] = d[i]+1

print(d)





















    
