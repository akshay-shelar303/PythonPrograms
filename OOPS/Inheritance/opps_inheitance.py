'''
class A:                  #parent class
    x=10
    def m1(self):
        print("m1---A")
        
class B(A):               #child class
    pass

b=B()
print(b.x)
b.m1()
'''
'''
class Animal:
    def animalname(self):
        print("Animal name is Horse")
    def legs(self):
        print("Horse has four legs")

class Child(Animal):
    def legs(self):
        print("Horse has four legs in child class")
    def colour(self):
        print("Horse  colour is White ")

c=Child()
c.legs()
c.animalname()
'''

class Parent:
    a=10
    b='Parent'
    def m1(self):
        print('m1-----Parent')
    def m2(self):
        print('m2-----Parent')

class Child(Parent):
    c=20
    d='Child'
    def m3(self):
        print('m3-----child')
    def m4(self):
        print('m4-----Child')
    def m2(self):
        Parent.m2(self)
        print('m2-----Child')

c=Child()
print('Parent variables-',c.a,c.b)
print('Child variables-',c.c,c.d)
c.m1()
c.m2()
c.m3()
c.m4()

















































