# i=int(input("Enter starting number:-"))
# num=int(input("Enetr end Number:-"))
# while i<=num:
#     if i%2==1:
#         print(i)  
#     i=i+1
 
# open_list = ["[","{","("]
# close_list = ["]","}",")"]
  
# # Function to check parentheses
# def check(myStr):
#     stack = []
#     for i in myStr:
#         if i in open_list:
#             stack.append(i)
#         elif i in close_list:
#             pos = close_list.index(i)
#             if ((len(stack) > 0) and
#                 (open_list[pos] == stack[len(stack)-1])):
#                 stack.pop()
#             else:
#                 return "Unbalanced"
#     if len(stack) == 0:
#         return "Balanced"
#     else:
#         return "Unbalanced"
  
  
# # Driver code
# string = "{[]{()}}"
# print(string,"-", check(string))
  
# string = "[{}{})(]"
# print(string,"-", check(string))
  
# string = "((()"
# print(string,"-",check(string))


# def checkBalance(str1):  
#     count= 0   
#     for i in str1:  
#         if i == "(" or i == "{" or i == "[":  
#             count += 1  
#         elif i == ")" or i == "}" or i == "]":  
#             count-= 1  
#         if count < 0:  
#             return "Unbalanced"  
#     if count==0:  
#         return "balanced"  
#     return "Unbalanced"  
# str1=input("Enter a string of brackets: ")   
# print("Given string is :", checkBalance(str1))  


def checkBalance(str1):  
    count= 0   
    # for i in str1:  
    #     if "()" in str1:  
    #         new_str1 = str1.replace("()", '')       
    new_str1 = str1.replace("()", '')
    return len(new_str1)  
str1=input("Enter a string of brackets: ")   
print("Given string is :", checkBalance(str1)) 


