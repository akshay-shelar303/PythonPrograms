x=30

def m1():
    x=20
    print(x)
    print(globals()['x'])

    
def m2():
    global x
    x=x+5
    print(x)

def m3():
    global x
    x=x*5
    print(x)

def m4():
    globals()['x']=globals()['x']+20
    print(x)

    
m1()
m2()
m3()
m4()
