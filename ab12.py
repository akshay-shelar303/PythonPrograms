def outer(a,b):
    def inner(a,b):
        sum=a+b
        return sum
    return inner(a,b)+5
print(outer(2,3))
