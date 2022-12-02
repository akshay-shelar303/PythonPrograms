'''
fh=open('C:/Users/prashant/Desktop/fh/pic.jpg','rb')
data=fh.read()
fh.close()

'''
'''
old=open('C:/Users/prashant/Desktop/fh/pic.jpg','rb')
data=old.read()
old.close()

new=open('C:/Users/prashant/Desktop/fh/piccopy.jpg','wb')
new.write(data)
new.close()
'''

'''
with open('C:/Users/prashant/Desktop/fh/aaa.txt','r+') as fh:
    fh.write('Akshay Shelar')
    fh.seek(0)
    print(fh.read())

'''
'''
fh = open('C:\\Users\\prashant\\Desktop\\fh\\client_server_model.jpg','rb')
data=fh.read()
fh.close()

fhnew = open('C:\\Users\\prashant\\Desktop\\fh\\newfi.jpg','wb')
fhnew.write(data)
print(fhnew.closed)
fhnew.close()
'''


'''
with open('C:/Users/prashant/Desktop/fh/aaa.txt','r+') as a:
    print(a.read())
    print('inside with blocj')
    #a.close()
    print(a.closed)
print('outside with block')
print(a.closed)

'''
'''
with open('C:/Users/prashant/Desktop/fh/aaa.txt','r+') as a:
    print(a.read())
    print(a.mode)
    print(a.name)
'''
'''

with open('C:/Users/prashant/Desktop/fh/aaa.txt','a+') as a:
    for i in range(1,101):
        a.write(str(i)+'\n')
    a.seek(0)
    data=a.readlines()
    for i in data:
        x=int(i)
        if x%4==0:
            print(x)
 
'''
    
'''
with open('C:/Users/prashant/Desktop/fh/aaa12.txt','w+') as a:
    for i in range(1,101):
        a.write(str(i)+'\n')
    a.seek(0)
    data=a.readlines()
    for i in data:
        x=int(i)
        if x%4==0:
            print(x)
 
'''
'''
fh=open('C:/Users/prashant/Desktop/fh/abs.txt','r')
data=fh.read()
##print(data)
print(data.count('a'))
fh.close()


'''
'''
fh=open('C:/Users/prashant/Desktop/fh/abs.txt','r')

data=fh.read()
print(data)
for i in range(65,91):
    print('count of ',chr(i),'-',data.count(chr(i)))
    
for i in range(97,123):
    print('count of ',chr(i),'-',data.count(chr(i)))
    
fh.close()

'''
'''
try:
    old=open('C:/Users/prashant/Desktop/fh/pic.jpg','rt')
    data=old.read()
    

    new=open('C:/Users/prashant/Desktop/fh/piccop.jpg','rb')
    new.write(data)
    new.close()
    
except FileNotFoundError as e:
    print('file not in directory',e)

except UnicodeDecodeError as e:
    print('wrong mode to access',e)

finally:
    old.close()
    
'''

'''
try:    
    with open('C:/Users/prashant/Desktop/fh/aa.txt','r') as a:
        print(a.read())
        print('inside with blocj')
        
except FileNotFoundError as e:
    print('file not in directory',e)


finally:
    print('finally block executed')



'''
'''
def m1():
    try:
        return 10

    except:
        return 20

    else:
        return 300
    
print(m1())
        
'''
'''
try:
    with open('C:/Users/prashant/Desktop/fh/aaa.txt','r') as a:
            for i in range(1,101):
                a.write(str(i)+'\n')
            a.seek(0)
            data=a.readlines()
            for i in data:
                x=int(i)
                if x%4==0:
                    print(x)

except FileExistsError as e:
    print('File already exist',e)
    
except Exception as e:
    print(e)

finally:
    print('finally block')



'''



with open('C:/Users/prashant/Desktop/fh/aaa12.txt','w+') as a:
    for i in range(1,101):
        a.write(str(i)+'\n')
    print(a.tell())
    a.seek(0)
    data=a.readlines()
    for i in data:
        x=int(i)
        if x%4==0:
            print(x)
 



















