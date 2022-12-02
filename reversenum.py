'''
num=1234
p=1234%10
a=1234//10
q=a%10
b=a//10
r=b%10
c=b//10
s=c%10
print("reverse of 1234 is",(p*1000+q*100+r*10+s))
'''


#using while loop
num=1234
reverse=0
while num>0:
    reminder=num%10
    reverse=(reverse*10)+reminder
    num=num//10
print("Reverse of 1234=",reverse)



'''
#reverse any number using user input
num=int(input("Enter number="))
i=num
reverse=0
while i>0:
    reminder=i%10
    reverse=(reverse*10)+reminder
    i=i//10
print("Reverse of number",num,"=",reverse)
'''
