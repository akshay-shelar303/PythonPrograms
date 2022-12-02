'''
fh=open('C:/Users/prashant/Desktop/abs.txt','r')
print(fh.read())
fh.close()
'''

'''
a=open('C:/Users/prashant/Desktop/abs12.txt','x')
a.write('new file')
a.close()

'''

'''
a=open('C:/Users/prashant/Desktop/abs.txt','w')
a.write('hi I am Akshay')
a=open('C:/Users/prashant/Desktop/abs.txt','a')
a.write('\nPython')
a.write('\nCJC')
a=open('C:/Users/prashant/Desktop/abs.txt','r')
print(a.read())
a.close()
'''

'''
ah=open('D:/python/12.py','a')
ah.write('\nsuccessfully executed')
ah=open('D:/python/12.py')
print(ah.read())
ah.close()
'''
'''
a=open('C:/Users/prashant/Desktop/abs.txt','w')
a.write('Akshay Shelar')

a=open('C:/Users/prashant/Desktop/abs.txt','a')
a.write('\nlearning python\nCJC pune')

a=open('C:/Users/prashant/Desktop/abs.txt','r')
print(a.read())
a.close()

'''

'''
print('---select menu---\n1.read\n2.write\n3.append')
ch=int(input('Enter your choice-'))
fn=input('enter file name-')

if ch==1:
    a=open(fn,'r')
    print(a.read())
          
elif ch==2:
    a=open(fn,'w')
    dw=input('enter data tobe written-')
    a.write(dw)

elif ch==3:
    a=open(fn,'a')
    dapp=input('enter data tobe append')
    a.write(dapp)
else:
    print('invalid chice')

a.close()
    
'''



'''
try:
    print('---select menu---\n1.read\n2.write\n3.append\n4createfile')
    ch=int(input('Enter your choice-'))
    fn=input('enter file name-')
    
    if ch==1:
        a=open(fn,'r')
        print(a.read())
              
    elif ch==2:
        a=open(fn,'w')
        dw=input('enter data tobe written-')
        a.write(dw,2)

    elif ch==3:
        a=open(fn,'a')
        dapp=input('enter data tobe append')
        a.write(dapp)

    elif ch==4:
        a=open(fn,'x')
        dapp=input('enter data tobe write')
        a.write(dapp)
        
    else:
        print('invalid chice')
        
except FileNotFoundError as e:
    print('file not exist',e)

except FileExistsError as e:
    print('file already exist',e)

except TypeError as e:
    print('invalid arguments',e)

    
finally:
    try:
        a.close()
    except NameError as e:
        print('name is not defined',e)
'''       

'''
file=open('C:/Users/prashant/Desktop/abs.txt','w')
file.write('Hi, I am akshay Shelar.\nI have completed my graduation fron pune university\n')
file=open('C:/Users/prashant/Desktop/abs.txt')
data=file.read()
file.close()

new=open('C:/Users/prashant/Desktop/xyz.txt','w')
new.write(data)
new.close()

'''
'''
li=['abc','xyz',1,2,3]
file=open('C:/Users/prashant/Desktop/akshay.txt','a')
for i in li:
    file.write(str(i))
file.close()
'''
'''
file=open('C:/Users/prashant/Desktop/fh/num.txt','a')  
for i in range(1,101):
    if i%5==0:
        file.write(str(i))
file.close()

'''





# try:
#     print('---select menu---\n1.read\n2.write\n3.append\n4createfile')
#     ch=int(input('Enter your choice-'))
#     fn=input('enter file name-')
#     a=open(fn,'r')
#     if ch==1:
# ##        a=open(fn,'r')
#         print(a.read())
              
#     elif ch==2:
#         a=open(fn,'w')
#         dw=input('enter data tobe written-')
#         a.write(dw,2)

#     elif ch==3:
#         a=open(fn,'a')
#         dapp=input('enter data tobe append')
#         a.write(dapp)

#     elif ch==4:
#         a=open(fn,'x')
#         dapp=input('enter data tobe write')
#         a.write(dapp)
        
#     else:
#         print('invalid chice')
        
# except FileNotFoundError as e:
#     print('file not exist',e)

# except FileExistsError as e:
#     print('file already exist',e)

# except TypeError as e:
#     print('invalid arguments',e)

    
# finally:
#     try:
#         a.close()
#     except NameError as e:
#         print('name is not defined',e)
















        








