#Diamond(Hybrid)
class A:
    def m1(self):
        print("m1---A")

class B(A):
    def m1(self):
        print("m1---B")
        super().m1()

class C(A):
    def m1(self):
        print("m1---C")
        super().m1()

class D(B,C):
    def m1(self):
        print("m1---D")
        super().m1()
    

d=D()
d.m1()
print(D.__mro__)






















'''

class A:
    def m1(self):
        print("m1---A")

class B(A):
    def m1(self):
        print("m1---B")
        

class C(A):
    def m1(self):
        print("m1---C")
        A.m1(self)

class D(C,B):
    pass

d=D()
d.m1()
'''
