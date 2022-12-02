#propagating exception

def m1():
    
    print('m1----')
    print(10/0)
    print('m1---end')
    
try:
    m1()
except ZeroDivisionError as e:
    print('canot divide by zero',e)
