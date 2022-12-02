bal=2000
def deposit(amt):
    global bal
    bal=bal+amt
    print("Balance after deposit=",bal)
def withdraw(amt):
    global bal
    bal=bal-amt
    print("Balance after withdraw=",bal)
def bal_check():
    print("Available balance=",bal)

deposit(1000)
withdraw(500)
bal_check()


#without using global  
bal=2000
def deposit(tbal,amt):
    tbal=tbal+amt
    print("Balance after deposit=",tbal)
    return tbal
def withdraw(tbal,amt):
    tbal=tbal-amt
    print("Balance after withdraw=",tbal)
    return tbal
def bal_check(tbal):
    print("Available balance=",tbal)
    

bal=deposit(bal,1000)
bal=withdraw(bal,500)
bal_check(bal)
