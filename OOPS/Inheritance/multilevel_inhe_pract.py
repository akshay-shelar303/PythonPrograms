class Grandparent:
    def name(self):
        print("Grandparent name")

class Parent(Grandparent):
    def name(self):
        print("Parent class name")
        super().name()
        
    def hair_color(self):
        print("Parent class hair color")
       

class Child(Parent):
    def name(self):
        print("Child class name")
        super().name()
        
    def hair_color(self):
        print("Child class hair color")
        super().hair_color()
         
    def height(self):
        print("Child class Height")
        
       
'''
p=Parent()
p.name()
p.hair_color()

'''
c=Child()
c.name()
c.hair_color()
c.height()
print(Child.mro())
