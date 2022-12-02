class A():
    pass

a=A()
a.x=100

a1=A()
a1.x=200

print(a.x)
print(a1.x)

print(id(a))
print(id(a1))

print(issubclass(A,object))
