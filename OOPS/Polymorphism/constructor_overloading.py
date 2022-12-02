class A:
    def __init__(self,a=0,b=0,c=0):
        if a!=0 and b!=0 and c!=0:
            print("Three Parameter Parameter")

        elif a!=0 and b!=0:
            print("Two parameter constructor")

        elif a!=0:
            print("One parameter constructor ")
        else:
            print("NO parameter value")



a=A()
a=A(2)
a=A(2,3)
a=A(2,3,4)
