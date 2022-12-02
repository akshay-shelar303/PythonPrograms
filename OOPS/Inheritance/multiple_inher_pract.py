class Parent1:
    def m1(self):
        print("m1---Parent1")
    def m2(self):
        print("m2---Parent1")
        super().m2()

class Parent2:
    def m2(self):
        print("m2---Parent2")
    def m3(self):
        print("m3---Parent2")
    def m4(self):
        print("m4---Parent2")
        
class Child(Parent1,Parent2):
    def m1(self):
        print("m1---Child")
    def m4(self):
        print("m4---Child")
    def m6(self):
        print("m6---Child")

c=Child()
'''
c.m1()
c.m4()
c.m6()
c.m2()
'''
#print(Child.mro())
print(issubclass(Parent1,Child))
