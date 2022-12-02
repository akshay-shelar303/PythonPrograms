'''
try:
    a=int(input('Enter first number-'))
    b=int(input('Enter second number-'))
    div=a/b
    print('Division is-',div)

except ZeroDivisionError as e:
    print('You try to divide an integer by zero',e)

except ValueError as e:
    print('Value error occur',e)

print('Code executed successfully')
'''
'''
def fun(a,b):
    try:
        
        add=a+c

    except NameError as e:
        print('Exception ocuur',e)


a=int(input('enter first num-'))
b=int(input('enter first num-'))

fun(a,b)
'''
'''

a=[10,20,30]
print(a[1])
try:
    print(a[10])

except IndexError as e:
    print("you try to access invalid index",e)

'''
'''
try:
    x=int('CJC')
except ValueError as e:
    print("you have entered invalid input type",e)

'''
'''
try:
    x=int([10])

except TypeError as e:
    print("YU have entered invalid input",e)
'''

'''
try:
    x=int(input('Enter number-'))
    if x%2==0:
        print(x,'is even number')
    else:
        print(x,'is odd number')
except ValueError as e:
     print("entered invalid input",e)
except TypeError as e:
     print("entered invalid input",e)
    
'''

'''
print("---select choice----\n1.Even Number\n2.Odd Number")
ch=int(input('Enter your choice-'))
try:
    if ch==1:
        x=int(input('Enter number-'))
        if x%2==0:
            print("even number")
    elif ch==2:
        x=int(input('Enter number-'))
        if x%2==1:
             print('Odd number')

except ValueError as e:
    print('you have entered in valid input type',e)
    
'''
'''
try:
    a=int(input('enter first num-'))
    b=int(input('enter second num-'))
    div=a/b
    print('division is ',div)
except ValueError as e:
    print("you have entered invalid input value",e)
    try:
        a=int(input('enter first num-'))
        b=int(input('enter second num-'))
        div=a/b
        print('division is ',div)

    except ValueError as e:
        print("inner block exception ",e)
'''
'''
try:
    def m1():
        a=int(input('enter first num-'))
        b=int(input('enter second num-'))
        print(a,'---',b)
    m1()
except ValueError as e:
    print("you have entered invalid input value",e)
    try:
        m1()
    except ValueError as e:
        print("inner block exception ",e)

'''

'''

print("---select choice----\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
ch=int(input("Enter your choice-"))
try:
    def cal():
        
        a=int(input("Enter First Value-"))
        b=int(input("Enter second Value-"))
         
        if ch==1:
            def add(a,b):
                print("Addition-",a+b)
            add(a,b)

        if ch==2:
            def sub(a,b):
                print("Subtraction-",a-b)
            sub(a,b)

        elif ch==3:
            def mul(a,b):
                print("Multiplication-",a*b)
            mul(a,b)

        elif ch==4:
            def div(a,b):
                print("Division-",a/b)
            div(a,b)
    cal()
except ValueError as e:
    print("You have entered invalid input value",e)
    try:
        cal()
    except Exception as e:
        print("Exception occur",e)
        
except ZeroDivisionError as e:
    print("You are trying to divide integer by zero ",e)
    try:
        cal()
    except Exception as e:
        print("Exception occur",e)
'''   


try:
    class Akshay:
        print("---select choice----\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
        
        def cal(self):
            ch=int(input("Enter your choice-"))
            
            a=int(input("Enter First Value-"))
            b=int(input("Enter second Value-"))
         
            if ch==1:
                def add(a,b):
                    print("Addition-",a+b)
                add(a,b)

            if ch==2:
                def sub(a,b):
                    print("Subtraction-",a-b)
                sub(a,b)

            elif ch==3:
                def mul(a,b):
                    print("Multiplication-",a*b)
                self.mul(a,b)

            elif ch==4:
                def div(a,b):
                    print("Division-",a/b)
                div(a,b)
    obj=Akshay()
    obj.cal()
except ValueError as e:
    print("You have entered invalid input value",e)
    try:
        obj.cal()
    except Exception as e:
        print("Exception occur",e)
        
except ZeroDivisionError as e:
    print("You are trying to divide integer by zero ",e)
    try:
        obj.cal()
    except Exception as e:
        print("Exception occur",e)


'''
class A:
    def m1(self):
        try:
            
            a=int(input("first num-"))
            b=int(input("second num-"))
            
            print('division=',a/b)
        except ZeroDivisionError as e:
            print("Cant divide bt zero",e)
            try:
                self.m1()
            except Exception as e:
                print("Inner block exception",e)
        except ValueError as e:
            print("invalid inputs ",e)
            try:
                self.m1()
            except Exception as e:
                print("Inner block exception",e)
       
a=A()

a=A()
a.m1()



'''












































