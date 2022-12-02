'''
n=5
for i in range(5):
    n=5-i
    for j in range(5):
        print(n,end='')
    print()
    
OUTPUT
55555
44444
33333
22222
11111
'''

'''
for i in range(5):
    n=5
    for j in range(5):
        print(n,end='')
        n=n-1
    print()
    
OUTPUT
54321
54321
54321
54321
54321
'''

'''
n=1
for i in range(4):
    for j in range(5):
        print(n,end=' ')
        n=n+1
    print()
    
OUTPUT    
1 2 3 4 5 
6 7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 
'''


'''
n=1
for i in range(5):
    for j in range(5):
        print(n,end=' ')
        n=n+2
    print()

OUTPUT
1 3 5 7 9 
11 13 15 17 19 
21 23 25 27 29 
31 33 35 37 39 
41 43 45 47 49
'''


'''
for i in range(1,6):
    for j in range(5):
        print(i,end=' ')
        i=i+5
    print()

OUTPUT
1 6 11 16 21 
2 7 12 17 22 
3 8 13 18 23 
4 9 14 19 24 
5 10 15 20 25 
'''        

'''
for i in range(65,70,1):
    for j in range(i,i+5,1):
        print(chr(i),end=' ')
        i=i+5
    print()
    
OUTPUT
A F K P U 
B G L Q V 
C H M R W 
D I N S X 
E J O T Y
'''


'''
n=65
for i in range(5):
    for j in range(5):
        print(chr(n),end=' ')
        n=n+1

OUTPUT
A B C D E 
F G H I J 
K L M N O 
P Q R S T 
U V W X Y 
'''


'''
for i in range(65,70,1):
    for j in range(i,i+5,1):
        print(chr(i),end='')
        print(ord(chr(i)),end=' ')
        i=i+5
    print()
OUTPUT
A65 F70 K75 P80 U85 
B66 G71 L76 Q81 V86 
C67 H72 M77 R82 W87 
D68 I73 N78 S83 X88 
E69 J74 O79 T84 Y89
'''


'''
for i in range(65,70,1):
    for j in range(i,i+5,1):
        print(chr(i)+str(i),end=' ')
        i=i+5
    print()

OUTPUT
A65 F70 K75 P80 U85 
B66 G71 L76 Q81 V86 
C67 H72 M77 R82 W87 
D68 I73 N78 S83 X88 
E69 J74 O79 T84 Y89 
'''

'''
for i in range(69,64,-1):
    for j in range(5):
        print(chr(i),end=' ')
        i=i+5
    print()
    
OUTPUT
E J O T Y 
D I N S X 
C H M R W 
B G L Q V 
A F K P U 
'''

'''
for i in range(1,10,2):
    for j in range(5):
        print(i,end=' ')
        i=i+2
    print()

OUTPUT
1 3 5 7 9 
3 5 7 9 11 
5 7 9 11 13 
7 9 11 13 15 
9 11 13 15 17 
'''
'''
for i in range(5,0,-1):
    for j in range(1,6):
        if j<i:
            print(' ',end='')
        else:
            print('*',end='')
    print()

#output
    *
   **
  ***
 ****
*****
'''

'''
for i in range(1,6):
    for j in range(1,16):
        if j>=i:
            print('*',end='')
        else:
            print(' ',end='')
    print()


#output
    
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
'''

'''
for i in range(1,6):
    for j in range(i,6):
        print('*',end=' ')
    print()

#outpot
* * * * * 
* * * * 
* * * 
* * 
*

'''


'''
for i in range(5):
    for j in range(5):
        print(chr(i+33),end='')
    print()
'''



































