class A:
    pass
class Parent:
    pass
class Child(Parent):
    pass
c=Child()
print(issubclass(Child,Parent))
print(issubclass(Child,A))


print("--instance---")
print(isinstance(c,Child))
print(isinstance(c,Parent))
print(isinstance(c,A))
