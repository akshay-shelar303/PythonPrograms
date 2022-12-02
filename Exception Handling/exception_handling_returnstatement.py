'''
def m1():
    try:
        print('try--start')
        return 10
        
    finally:
        print('finally --block')

x=m1()
print(x)
'''

'''
def m1():
    try:
        print('try ---start')
        return 10
    finally:
        print('finally---block')
        return 20

x=m1()
print(x)
'''


def m1():
    x=10
    try:
        print('try--start')
        return x

    finally:
        x=20
        print('finally--block--',x)

x=m1()
print(x)
