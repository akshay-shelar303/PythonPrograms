#PARAMETERIZED FUNCTIONS WITH RETURN STATEMENT
#1
def tuple_t(t):
    print("tuple")
    return t
print(tuple_t((1,2,3)))

#2
def floor(x,y):
    print(x//y)
    return x
print(floor(20,2))

#3
def state(a,b):
    print("india")
    return a
print(state("MH","GJ"))

#4
def set_diff(s1,s2):
    print(s1-s2)
    return s1
print(set_diff({1,2,3},{2,3}))


#5
def fun(p,q):
    print("return p")
    return p
print(fun(100,20))

