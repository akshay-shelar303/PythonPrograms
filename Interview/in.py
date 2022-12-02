'''
def myfun(l):
    new_list = []
    for i in l:
        if i not in new_list:
            new_list.append(i)

    print(new_list)

myfun([1,2,3,1,5,4,3])
'''

def phi(n):
    fact = 1
    i = 1
    while i <= n:
        fact = fact * i
        i += 1
    print(fact)
    c = 0
    while fact % 2 == 0:
        c += 1
        fact = fact // 2
        print(fact)
    print(c)
phi(5)
        
