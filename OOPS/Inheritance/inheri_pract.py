'''
class Company:
    def name(self):
        print("Company  name")

class Product1(Company):
    def name(self):
        print("Product1 name")
        super().name()
        
    def price(self):
        print("Product1 price")

class Product2(Product1):
    def name(self):
        print("Product 2 name")
        super().name()
        
    def price(self):
        print("Priduct 2 Price")
        super().price()

p=Product2()
p.name()
p.price()
'''

class Country:
    def name(self):
        print("India")

class State(Country):
    def name(self):
        print("Mahrastra")
        super().name()
    def code(self):
        print("1")

class District(State):
    def name(self):
        print("Nashik")
        super().name()
    def code(self):
        print("2")

class Town(District):
    def name(self):
        print("Malegaon")
        super().name()
    def river(self):
        print("Girna")
class Village(Town):
    def name(self):
        print("Yesgaon")
        super().name()
        
    def population(self):
        print("1500")

v=Village()
v.name()
v.population







































