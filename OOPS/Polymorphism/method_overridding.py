class A:
    def m1(self):
        print('m1----A')

    def m2(self):
        print('m2---A')

    def price(self):
        print('price before discount')

class B(A):
    def m2(self):
        print('m2-----B')
        
    def m3(self):
        print('m3---B')
        
    def price(self):
        print('price after discount')
b=B()
b.m1()
b.m2()
b.m3()
b.price()
