'''
#custom Exception by using in-built exception class

def m1(age):
    print('m1---start')
    if age<0:
        raise TypeError("age ---Problem")

    print('m1---end')
try:
    m1(-5)
except TypeError as e:
    print("except-- block--",e)
'''
#by creating own custom exception class

class AgeInvalidError(Exception):
    def __init__(self,msg):
        self.msg=msg
def m1(age):
    print("m1---start")
    if age<0:
        raise AgeInvalidError("Age problem")
try:
    m1(-5)
except AgeInvalidError as msg:
    print('except---block--',msg)
