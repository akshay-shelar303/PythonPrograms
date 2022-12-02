'''
try:
    x=int(input('Enter a value-'))
    a=10/x

except ZeroDivisionError as e:
    print('Enter non zero value--',e)

except ValueError as e:
    print('Enter number---',e)

except:
    print("except---block")

else:
    print('No exception ---else block')

print('Pragram ---end')
'''
'''
try:
    
    print("try block initiated----")
    a=int(input('Enter first number-'))
    b=int(input('Enter second number'))
    div=a/b
    print('Division is :-',div)

except ValueError as e:
    print('You have entered invalid value--',e)

except ZeroDivisionError as e:
    print('cannot divide by zero--',e)

except:
    print('Exception occur')

else:
    print('else block executed')

finally:
    print('finally program ends----')

'''

'''
try:
    def m1():
        a=int(input('Enter first value:-'))
        b=int(input('Enter second value:-'))
        div=a/b
        print('division',div)
    m1()


except ValueError as e:
    print('you have entered invalid input--',e)

except ZeroDivisionError as e:
    print('cannot divide by zero--',e)
    
else:
    print('no exception occur')

finally:
    print('finaaly program ends ')

'''
'''
try:
    a=int(input('enter first num-'))
    b=int(input('enter second num-'))
    div=a/b
    print('Division-',div)

    try:
        l=[1,2,3,4]
        i=int(input('Enter index number-'))
        print(l[i])
        
    except IndexError as e:
        print('You have entered invalid index',e)
    except ValueError as e:
        print('entered invalid input',e)

except ZeroDivisionError as e:
    print('cannot divide by zero--',e)
except ValueError as e:
    print('enter valid input',e)

'''
'''
try:
    l=[1,2,3]
    l.append(4,2)
    
except NameError as e:
    print("invalid list name entered",e)
except  TypeError  as e:
    print('invalid arguments',e)

'''
'''
try:
    l=[1,2,3,4]
    l.extend('AKSHAY')
    print(l)

except NameError as e:
    print("invalid list name entered",e)
except  TypeError  as e:
    print('invalid arguments',e)
'''
'''
try:
 l=[1,2,3]
 l.insert('a',2)
 print(l)
except  TypeError  as e:
    print('invalid arguments',e)

except NameError as e:
    print("invalid list name entered",e)



'''
'''
try:
    l=[1,2,3]
    l.pop(4)
except IndexError as e:
    print('entered invalid index',e)
except NameError as e:
    print("invalid list name entered",e)

except  TypeError  as e:
    print('invalid arguments',e)

'''
'''
try:
    l=[2,4,6,8]
    l.remove('a')
    print(l)

except ValueError as e:
    print('entered value is not in list',e)
    
except NameError as e:
    print("invalid list name entered",e)

except  TypeError  as e:
    print('invalid arguments',e)
'''

'''
try:
    l=['aaa','b','c']
    l.index('aaa','b')

except ValueError as e:
    print('entered value is not in list',e)
    
except NameError as e:
    print("invalid list name entered",e)

except  TypeError  as e:
    print('invalid arguments',e)
'''
'''
try:
    
    l=[1,2,3,4,5,5]
    print(l.count(6,2))

except  TypeError  as e:
    print('invalid arguments',e)

except NameError as e:
    print("invalid list name entered",e)

'''
'''
#set method exception handling
try:
    
    s={1,2,3,4}
    s.add()

except  TypeError  as e:
    print('invalid arguments',e)

except NameError as e:
    print("invalid name entered",e)
'''

'''
try:
    s={'a',1,2}
    s.remove(1,2)

except KeyError as e:
    print('you have enterd invalid value',e)

except  TypeError  as e:
    print('invalid arguments',e)

except NameError as e:
    print("invalid name entered",e)
'''
'''
try:
    s={1,2,3,4}
    s.update(1)

except  TypeError  as e:
    print('invalid arguments',e)

except NameError as e:
    print("invalid name entered",e)
'''
'''
try:
    s={10,20,3,0,40}
    s.discard([10,20])

except  TypeError  as e:
    print('invalid arguments',e)

except NameError as e:
    print("invalid name entered",e)

'''
'''
try:
    s={1,2,3,4}
    s1=s.copy(4)

except  TypeError  as e:
    print('invalid arguments',e)

except NameError as e:
    print("invalid name entered",e)

'''

#dictinary methods - exception handling
'''
try:
    d={1:'a',2:'b',3:'c'}
    d.update(2)
except TypeError as e:
    print('invalid input--',e)

except NameError as e:
    print('entered name is not found--',e)
'''

'''
try:
    d={1:'a',2:'b',3:'c'}
    d.pop(4)

except KeyError as e:
    print('Entered key is not present--',e)

except TypeError as e:
    print('invalid input--',e)

except NameError as e:
    print('entered name is not found--',e)
'''

'''
try:
    d={1:'a',2:'b',3:'c'}
    d.popitem(1)

except TypeError as e:
    print('invalid input--',e)

except NameError as e:
    print('entered name is not found--',e)
'''

'''
try:
    d={1:'a',2:'b',3:'c'}
    print(d.get(4,6))

except TypeError as e:
    print('invalid input--',e)

except NameError as e:
    print('entered name is not found--',e)

'''
'''
try:
    d={1:'a',2:'b',3:'c'}
    d.clear(1)

except TypeError as e:
    print('invalid input--',e)

except NameError as e:
    print('entered name is not found--',e)
'''


'''
try:
    d={1:'a',2:'b',3:'c'}
    d1=d.copy(1)
    print(di)

except TypeError as e:
    print('invalid input--',e)

except NameError as e:
    print('entered name is not found--',e)
'''


'''
try:
    d={1:'a',2:'b',3:'c'}
    d.items(1)

except TypeError as e:
    print('invalid input--',e)

except NameError as e:
    print('entered name is not found--',e)

'''

'''
try:
    d={1:'a',2:'b',3:'c'}
    d.keys(1)

except TypeError as e:
    print('invalid input--',e)

except NameError as e:
    print('entered name is not found--',e)
'''
'''
try:
    print("---select choice----\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
    ch=int(input("Enter your choice-"))
    def cal():
        a = int(input('Enter first value-'))
        b = int(input('Enter second value-'))
        if ch==1:
            def add(a,b):
                print('Addition-',a+b)
                
        elif ch==2:
            def sub(a,b):
                print('Subtraction-',a-bb)

        elif ch==4:
            def mul(a,b):
                print('Multiplication-',a/b)

        elif ch==3:
            def div(a,b):
                print('Division-',a/b)
    cal()
except ZeroDivisionError as e:
    print('cannot divide by zero',e)

except ValueError as e:
    print('invalid input',e)

else:
    print('No exception')

finally:
    print('program ends')
            
'''

class Calculator:
   
    def add(self,a,b):
        print('Addition-',a+b)

    def sub(self,a,b):
        print('Subtraction-',a-b)

    def mul(self,a,b):
        print('Multiplication-',a*b)

    def div(self,a,b):
        print('Division-',a/b)


c=Calculator()
try:
    print("---select choice----\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
    ch=int(input("Enter your choice-"))
    
    a = int(input('Enter first value-'))
    b = int(input('Enter second value-'))
    if ch==1:
        c.add(a,b)
                    
    elif ch==2:
        c.sub(a,b)
    elif ch==3:
        c.mul(a,b)

    elif ch==4:
        c.div(a,b)

except ZeroDivisionError as e:
    print('cannot divide by zero',e)

except ValueError as e:
    print('invalid input',e)

else:
    print('No exception')

finally:
    print('program ends')
            
            

















    
