##[2, 5, [3, 4, 7],[4, 6, 2, [7, 3]]]


# def addfun(l):
#     add = 0
#     for i in l:
#         if type(i) == list:
#             for j in i:
#                 if type(j) == list:
#                     for k in j:
#                         add = add+k
#                 else:
#                     add = add+j
#         else:
#             add = add+i
#     print(add)

# addfun([2, 5, [3, 4, 7],[4, 6, 2, [7, 3]]])
                
        
        
# def addfun(l):
#     li = []
#     for i in l:
#         if type(i) is list:
#             li.extend(addfun(i))
#         else:
#             li.append(i)
#     return li
# var = addfun([2, 5, [3, 4, 7],[4, 6, 2, [7, 3]]])
# print(var)
