#Multiple Inheritance
class A:
    def m1(self):
        print("m1----A")
        
        

class B:
    def m1(self):
        print("m1----B")
        

class C(A,B):           #C--->A--->B
    pass

'''
class C(B,A):     #C--->B--->A
    pass
'''
c=C()
c.m1()

print(C.mro())       #mro-Method Resolution Order
