#read(n)
'''
fh=open('C:/Users/prashant/Desktop/fh/aaa.txt')
print(fh.read(5))
fh.close()
'''


#readline()-
'''
The readline() method reads the lines of the file from the beginning,
i.e., if we use the readline() method two times,
then we can get the first two lines of the file.
'''
'''
fh=open('C:/Users/prashant/Desktop/fh/aaa.txt')
print(fh.readline())
print(fh.readline())
print(fh.readline())
fh.close()
'''

#readline(n)
'''
fh=open('C:/Users/prashant/Desktop/fh/aaa.txt')
print(fh.readline(5))
print(fh.readline())
fh.close()
'''

#readlines()-It returns the list of the lines till the end of file is reached.
'''
fh=open('C:/Users/prashant/Desktop/fh/aaa.txt')
print(fh.readlines())
fh.close()
'''

#writelines()
'''
fh=open('C:/Users/prashant/Desktop/fh/xyz.txt','w')
fh.writelines(['Akshay Shelar\n','Python Learning\n','CJC Pune'])
fh.close()
'''


#tell()
'''
fh=open('C:/Users/prashant/Desktop/fh/xyz.txt')
print(fh.tell())
print(fh.readline())
print(fh.tell())
fh.close()
'''

#seek()
'''
fh=open('C:/Users/prashant/Desktop/fh/xyz.txt')
print(fh.tell())
fh.seek(15)
print(fh.readline())
print(fh.tell())
fh.close()
'''


#readable() and writable()
'''
fh=open('C:/Users/prashant/Desktop/fh/xyz.txt','r+')  #read+write mode
print(fh.readable())
print(fh.writable())
print(fh.read())
fh.write('Akshay Shelar')
fh.close()
'''
'''
fh=open('C:/Users/prashant/Desktop/fh/xyz.txt','r+')
fh.write('hi we')
fh.flush()
print(fh.tell())
fh.seek(0)
print(fh.read())
fh.close()


'''

#closed :-
#it is used to check whether file is closed or not.it returns boolean value
'''
fhnew = open('C:\\Users\\prashant\\Desktop\\fh\\newfi.jpg','wb')
fhnew.write(data)
print(fhnew.closed)
fhnew.close()

'''
#mode :-return the mode of file in which it is opened
'''
fh=open('C:/Users/prashant/Desktop/fh/aaa.txt','r+')
print(fh.mode)
fh.close
'''
'''
#name :-it returns the path of file i.e filename
fh=open('C:/Users/prashant/Desktop/fh/aaa.txt','r+')
print(fh.name)
fh.close()
'''


#with block :-in with block we need not to close the file
'''
with open('C:/Users/prashant/Desktop/fh/aaa.txt','r+') as fh:
    print(fh.read())
'''



'''

fh=open('C:/Users/prashant/Desktop/fh/xyz.txt','r+')
fh.seek(11)
fh.write('Om    ')
fh.flush()
fh.seek(49)
fh.write('in python')
fh.flush()
fh.seek(0)
print(fh.read())
fh.close()
'''

'''
fh=open('C:/Users/prashant/Desktop/fh/xyz.txt','r')
print(fh.read())
fh.close()
'''
'''
#write the program to count no of lines in text file

fh=open('C:/Users/prashant/Desktop/fh/aaa.txt','r+')
print(len(fh.readlines()))
fh.close()



'''
'''
#write the program to write a list to file

fh=open('C:/Users/prashant/Desktop/fh/newfile.txt','w+')

l=['aa','bb','cc','dd']

fh.writelines(l)
fh.flush()
fh.seek(0)
print(fh.read())
fh.close()

'''
'''
fh=open('C:/Users/prashant/Desktop/fh/abcd.txt','r')
l=fh.readlines()
fh.close()

new=open('C:/Users/prashant/Desktop/fh/newfile.txt','a')
for i in l:
    x=l.index(i)
    if x%2!=0:
        new.write(str(i))

new.close()
'''

fh=open('C:/Users/prashant/Desktop/fh/abs.txt','r')
data=fh.read()
print(data)
fh.close()

print('--After replace---\n')

file=open('C:/Users/prashant/Desktop/fh/absnew.txt','w+')

x=data.replace('a','Z')
x=x.replace('A','Z')

file.write(x)
file.flush()
file.seek(0)
print(file.read())
file.close()














































