'''
def addition(a,b):
    add=a+b
    return add

a=int(input('Enter first no-'))
b=int(input('Enter second no-'))

result=addition(a,b)
print('result=',result)

while True:
    print('Select operand\n1.+\n2.-\n3.*\n4./')
    ch=int(input('Enter your choice-'))
    if ch==1:
        n=int(input('Enter number:-'))
        result =result + n
        print(result)
    elif ch==2:
        n=int(input('Enter number:-'))
        result =result - n
        print('Result=',result)
        
    elif ch==3:
        n=int(input('Enter number:-'))
        result =var * n
        print('Result=',result)

    elif ch==4:
        n=int(input('Enter number:-'))
        result =var / n
        print('Result=',result)
'''        
'''
def addition(a,b):
    add=a+b
    return add

a=int(input('Enter first no-'))
b=int(input('Enter second no-'))

result=addition(a,b)
print('result=',result)

while True:
    x,y=input('Enter operand and number-').split()
    
    if x== '*':
        result=result*(int(y))
        print(result)

    elif x== '/':
        result=result/(int(y))
        print(result)
            
    elif x== '+':
    
        result=result+(int(y))
        print(result)

    elif x== '-':
  
        result=result-(int(y))
        print(result)

'''

def addition(a,b):
    add=a+b
    return add

a=int(input('Enter first no-'))
b=int(input('Enter second no-'))

result=addition(a,b)
print('result=',result)

while True:
    n=input('Enter operand and number-')
    for i in n:
        if i== '*':
            result=result*(int(n[1:]))
            print('Reasult=',result)

        elif i== '/':
            result=result/(int(n[1:]))
            print('Reasult=',result)
                
        elif i== '+':
            result=result+(int(n[1:]))
            print('Reasult=',result)

        elif i== '-':
            result=result-(int(n[1:]))
            print('Reasult=',result)

    if n=='end':
        break





















