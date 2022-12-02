'''
from abc import ABC,abstractmethod

class A(ABC):

    @abstractmethod
    def m1(self):
        pass

    def m2(self):
        print("m2---A")


class B(A):
    def m1(self):
        print("m1---B")
        
b=B()
b.m1()
b.m2()


'''


'''
#default implementataion for abstract method
from abc import ABC,abstractmethod

class A(ABC):

    @abstractmethod
    def m1(self):
        print("m1---A")

    @abstractmethod
    def m3(self):
        print("m3----A")


    def m2(self):
        print("m2---A")


class B(A):
    def m1(self):
        print("m1---B")
        super().m1()


    def m3(self):
        print("m3---B")

b=B()
b.m1()
b.m2()
b.m3()
    
'''




































