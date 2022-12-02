##age = int(input("Enter age:-"))
##if age >= 18:
##    print('you are eligible for voting')
##elif age < 0:
##    print('Please enter valid age')
##elif age > 0 and age < 18 :
##    print("not eligible ,please wait for ",18-age,'more yeares to vote')


##for i in range(101,1,-1):
##    if i % 10 == 0:
##        print(i)
##
##
##
##i = 100
##while i < 9:
##    if i % 10 == 0:
##        print(i)
##        i -= 1


##
##s = int(input("Enter number of students-"))
##d = dict()
##
##for i in range(s):
##        name = input("Enter student name:-")
##        marks = int(input("Enter student marks:-"))
##        d[name] = marks
##print(d)
##fh = open('C:/Users/DELL/Desktop/interview.txt','w')
##for k,v in d.items():
##        fh.write(f"Name:-{k} and Marks:-{v}\n")
##fh.close()




num = int(input("Enter the number:-"))
if num > 1:
        for i in range(2,num):
                if num % i == 0:
                        print(num,"is not prime number")
                        break
                else:
                        print("prime number")
                        break
else:
        print("not prime number")

            















