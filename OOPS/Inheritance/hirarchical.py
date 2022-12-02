'''
class A:
    def m1(self):
        print("m1--A")
        

class B(A):
    def m1(self):
        print("m1--B")
        super().m1()
        

class C(A):
    def m1(self):
        print("m1--C")
        super.m1()

c=C()
c.m1()
b=B()
b.m1()
'''


class Animal:
    def name(self):
        print("Animal")

class Dog(Animal):
    def name(self):
        print("Dog Name")

class Horse(Animal):
    def color(self):
        print("Horse color is white")

class Cow(Animal):
    def name(self):
        print("Cow name")

class Pet(Animal):
    def name(self):
        print("Pet name")
        super().name()

p=Pet()
p.name()

d=Dog()
d.name()

h=Horse()
h.color()

print(Pet.mro())

































