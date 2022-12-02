li=[1,2,3,4,5]
#append -adds single element at the end of list
li.append(6)  
print (li)

#extend  -adds multiple elements at the end of list
li.extend([7,8,'abs'])  
print(li)

#insert  -add element at specific index
li.insert(1,'Akshay') 
print(li)


#pop -it removes last element of list
l=[1,2,3,4,5,6]
l.pop() 
print(l)

#remove  -#it removes specific element
l.remove(3) 
print(l)    #l=[1, 2, 4, 5]

#index  -it returns the index or position of first occurance of specifiesd value
l2=[1,2,3,5]
var=l2.index(3)
print(var)

#count  -it returns no of elements with specified value
l3=[1,2,1,3,4,1,8,1]
print(l3.count(1))  


#sort  -it returns sorted list .it made changes in cureent list
l4=[6,4,2,3,5,1]
l4.sort()  
print(l4)

#reverse  -it reverse the list
l4.reverse()
print(l4)

#sorted -it sort the list and give new list
print(sorted(l4))
