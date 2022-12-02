'''
#1 capitalize :-it converts first character into upperase

a='shelar'
new=a.capitalize()
print(new)


#2 casefold :-it converts entire string into lowecase

a='SheLaR'
new=a.casefold()
print(new)


#3 center   :-it centers the dtring

a='AKSHAY'
new=a.center(15)
print(new)

#4 count  :-it returns the count of occurrence of specified string

a='We are leaning python and python is simple.'
new=a.count('python')
print(new)              #2

new=a.count('a')
print(new)              #3



#5 endswith  :-it checks whether given string ends with specified character or
#       not and it returns boolean value

a='We are leaning python and python is simple.'
new=a.endswith('simple')
print(new) 

#6 find :- it finds input string into existing string and returns position of
#        first occurrence of input string.If specified string not found it
#         returns -1

a='We are learning python and python is simple.'
new=a.find('learning')
print(new)



#7 index  :-it finds input string into existing string and returns position of
#        first occurrence of input string.If specified string not found it
#         returns ValueError Exception

a='We are learning python and python is simple.'
new=a.index('We')
print(new)


#8 isalnum :-it checks whether specified string is alphanumeric (alphabets+numbers)
#           or not

a='akshay12'
new=a.isalnum()
print(new)

#9 isalpha :-it checks whether specified string is made up of only alphabets and
#         if yes it returns True else it returns False

a='akshay'
new=a.isalpha()
print(new)


'''























