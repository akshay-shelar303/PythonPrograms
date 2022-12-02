class A:
    def __str__(self):
        return "Count={}".format(self.count)
a1=A()
a1.count=101
print(a1)

a2=A()
a2.count=200
print(a2)
