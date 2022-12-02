'''
class AgeValidate(BaseException):
    def __init__(self,msg):
        self.msg=msg

n=int(input('Enter your age'))

if n<1:
    raise AgeValidate('invalid age--')

'''
'''
class AgeValidate(Exception):
    pass

n=int(input('Enter your age'))
try:
    if n<1:
        raise AgeValidate('Invalid age')
    else:
        print('valid age entered')
except AgeValidate as e:
    print('Age Error--',e)

'''
'''
class AgeValidate(Exception):
    def __init__(self,msg):
        self.msg=msg

age=int(input('Enter your age-'))
if age<18:
    raise AgeValidate('you are not Eligible to vote')

else:
    print("You are eligible to vote")
    
'''
'''
class AgeValidateError(Exception):
    pass

age=int(input('Enter your age-'))
try:
    if age<18:
        raise AgeValidateError('invalid age enterred')
    else:
        print('valid Age')
except AgeValidateError as e:
    print('age Error--',e)

'''
'''
#If the try statement reaches a break, continue or return statement,
the finally clause will execute just prior to the break, continue or return statement’s execution.
def m1():
    try:
        print("try---start")
        return 100

    except ZeroDivisionError:
        print('Error occur')
        return 200

    else:
        return 200

    finally:
        return 400
        print("finally block--")
    
print(m1())

'''
'''
class MaxSpeedError(Exception):
    pass
class AgeEligibility(Exception):
    pass

speed=int(input('Enter speed --'))
age=int(input('Enter age--'))

try:
    if speed>200:
        raise MaxSpeedError('you are exceeded max speed')
    
    elif age<18:
        raise AgeEligibility('you are not eligible to drive')
    else:
        print('Safe speed')

except MaxSpeedError as e:
    print('Speed limit Error--',e)

except AgeEligibility as e:
    print("Age Error--",e)

else:
    print("No Error")

finally:
    print('Car name-ABC')

'''
'''
class EnteredNumError(Exception):
    pass

try:
    a=int(input("Enter first Number-"))
    b=int(input('Enter Second Number'))
    
    if b==0:
        raise EnteredNumError('invalid number')
    else:
        print("Division-",a/b)
        
except EnteredNumError as e:
    print('error occur',e)

'''
'''
class FirstCaseError(Exception):
    pass
def m1():
    try:
        s=input("enter string-")
        if s.istitle()==True:
            raise FirstCaseError('you entered first leterr upper case')

        else:
            print("coreect string---")


    except FirstCaseError as e:
        print('Error occur--',e)
        try:
            m1()
        except Exception:
            print('Exception occur')

m1()

'''

'''
class Error(Exception):
    pass

class ValueTooSmallError(Error):
    pass

class ValueTooLargeError(Error):
    pass

number = 10


while True:
    try:
        a = int(input("Enter a number: "))
        if a < number:
            raise ValueTooSmallError
        elif a > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print()

print("Congratulations! You guessed it correctly.")

'''












