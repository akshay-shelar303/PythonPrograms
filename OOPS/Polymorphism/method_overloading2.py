class A:
    def m1(self,*a):
        s=0
        for i in a:
            s=s+i
        print(s)

a=A()
a.m1()
a.m1(2)
a.m1(2,3)
a.m1(2,3,4)
a.m1(2,3,4,5)
