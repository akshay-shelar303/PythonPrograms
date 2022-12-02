'''
#exception 
print('A--file --Start')
print(10/0)                  #ZeroDivisionError
print('A--file --End')
'''


#exception handling

print('A--File--Start')
try:
    print(10/0)
    
except ZeroDivisionError:
    print('except--block')

print('A--file--End')






print('A--File--Start')
try:
    print('try block start')
    print(10/0)
    print('try block end')
    
except ZeroDivisionError:
    print('except--block')

print('A--file--End')



#no exception- except block will be skipped
print('A--File--Start')
try:
    print('try block start')
    print(10/2)
    print('try block end')
    
except:
    print('except--block')

print('A--file--End')





























