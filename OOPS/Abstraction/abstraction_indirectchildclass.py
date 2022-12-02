from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m3(self):
        pass

    def m2(self):
        print("m2---A")

class B:
    def m1(self):
        print("m1---B")

    def m3(self):
        print("m3---B")

A.register(B)                #indirect child class creation
print(issubclass(B,A))

b=B()
b.m1()
b.m3()

