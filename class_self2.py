class A:
    def m1(self):
        print("m1__self")
        print(self.x)
        print(id(self))

a=A()
a.x=100;
print(a.x)
print(id(a))

a1=A()
a1.x=200
print(a1.x)
print(id(a))
                  
