#MULTILEVAL Inheritance
class A:
    def m1(self):
        print("m1----A")

class B(A):
    def m1(self):
        print("m1----B")
        A.m1(self)

class C(B):
    def m1(self):
        print("m1----C")
        B.m1(self)
        #super().m1()

s=C()
s.m1()
print(C.__mro__)
