class Car:
    def __init__(self,name,milege,maxspeed):
        self.name=name
        self.milege=milege
        self.maxspeed=maxspeed
    def __str__(self):
        return "Name:-{} Milege:-{} MaxSpeed:-{}".format(self.name,self.milege,self.maxspeed)
class Details(Car):
    def display(self):
        print("car details")
        print(b)
b=Details('XYZ','25mpl','250rpm')
b.display()
