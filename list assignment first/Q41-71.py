# ************Question 41 *************
# Write a Python program to create multiple lists.
# l=[]
# n=int(input("Enter How  Many list u want to create:"))
# for i in range(n):
#     l2=[]
#     for j in range(5):
#         x1=input(f"Enter value @ {i}{j}:")
#         l2.append(x1)
#     l.append(l2)
# print(l)

# *************Question 42 ****************
# Write a Python program to find missing and additional values in two lists.  
# Sample data : Missing values in second list: b,a,c
# Additional values in second list: g,h

# l1=['a','b','c','d','e']
# l2=['a','f','d','e','j']
# l3=[]
# for i in l1:
#     if(i not in l2):
#         l3.append(i)
# print(f"Missing values in second list: {l3}")
# l3=[]
# for i in l2:
#     if(i not in l1):
#         l3.append(i)
# print(f"Additional values in second list: {l3}")

# ****************Question 43 ************
# Write a Python program to split a list into different variables.
# l=['Anshul',19,'Gwalior']
# a,b,c=l
# print(a)
# print(b)
# print(c)

# ***********Question 44********
#  Write a Python program to generate groups of five consecutive numbers in a list.
# l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# l1=[]
# l2=[]
# j=0
# for i in range(len(l)):
#     if(j==5):  
#         l2.append(l1)
#         l1=[]
#         l1.append(l[i])
#         j=1    
#     else:
#         l1.append(l[i])
#         j+=1
# if(l1):
#     l2.append(l1)
# print(l2)

# ***********Question 45 **************
# Write a Python program to convert a pair of values into a sorted unique array.
# x=[(1,2),(3,4),(2,5),(4,6)]
# t=[]
# for i in x:
#     for j in i:
#         if(j not in t):
#             t.append(j)
# t.sort()
# print(t)

# **********Question 46 ************
# Write a Python program to select the odd items of a list.
# l=[2,7,8,11,14,19]
# t=[]
# for i in l:
#     if (i%2!=0):
#         t.append(num)
# print(t)

# **********Question 47 *************
# Write a Python program to insert an element before each element of a list.
# l=[1, 2, 3]
# t=[]
# n=int(input("Enter element:"))
# for i in l:
#     t.append(n) 
#     t.append(i)   
# print(t)

# **********Question 48 **********incomplete
# Write a Python program to print a nested lists (each list on a new line) using the print() function.
# l=[[1,2,3,4],[5,6,7,8],[3,6,2,7]]
# for i in l:
#     print(i)

# ********Question 49 **********
#  Write a Python program to convert list to list of dictionaries.  
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]

# l1=['black','Green','yellow']
# l2=['#4000','#7000','#0000']
# d={}
# for i in range(len(l1)):
#     d.setdefault(l1[i],l2[i])
# print(d)

# *************Question 50 ***********
# Write a Python program to sort a list of nested dictionaries.
# l1=[{"name": "Anshul", "age": "19"},{"name": "Rahul", "age": '17'},{"name": "Priya", "age": '20'}]
# n=input("Enter on what basis u want to sort name/age:")
# for i in range(len(l1)-1):
#     if(l1[i][n]>l1[i+1][n]):
#         l1[i],l1[i+1]=l1[i+1],l1[i]
# print(l1)

# ************Question 51 **************
# 51. Write a Python program to split a list every Nth element.  
# Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
# l=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# l1=[[],[],[]]
# i=0
# while(i<len(l)):
#     j=0
#     while(j <= 2 and i < len(l)):
#         l1[j].append(l[i])
#         i += 1
#         j += 1
# print(l1)

# ***************Question 52 ************
# . Write a Python program to compute the similarity between two lists.  
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
# Expected Output:
# Color1-Color2: ['white', 'orange', 'red']
# Color2-Color1: ['black', 'yellow']

# l1=["red", "orange", "green", "blue", "white"],["black", "yellow", "green", "blue"]
# l2=[[],[]]
# for i in range(len(l1)):
#     for j in l1[i]:
#         if (j not in l1[1]):
#             l2[0].append(j)
# for x in l1[1]:
#     if(x not in l1[0]):
#         l2[1].append(x)
# print(l2)

# **********Question 53 ***************
# Write a Python program to create a list with infinite elements.
# l=[]
# i=1
# while(True):
#     l.append(i)
#     print(l)
#     i += 1

# **********Question 54 *************
# Write a Python program to concatenate elements of a list.
# l=['Anshul','Loves','python']
# print("".join(l))

# ***********Question 55 ************
# Write a Python program to remove key values pairs from a list of dictionaries.
# l=[{"name": "Anshul", "age": 19},{"name": "Rahul", "age": 17},{"name": "Priya", "age": 20}]
# n=input("Enter u want to remove name/age:")
# for i in l:
#     del i[n]
# print(l)

# ***********Question 56 *************
# Write a Python program to convert a string to a list.
# l='abcdefghji'
# l1=[]
# for i in l:
#     l1.append(i)
# print(l1)

# **********Question 57 ************
# Write a Python program to check if all items of a list is equal to a given string.
# l=['anshul','anshul','anshul']
# n='anshul'
# c=True
# for i in l:
#     if(i!=n):
#         c=False
# if(c==False):
#     print("all are not equal")
# else:
#     print("all are equal")

# **********Question 58 **********
# Write a Python program to replace the last element in a list with another list.  
# Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]

# l1=[1, 3, 5, 7, 9, 10]
# l2=[2, 4, 6, 8]
# l3=[]
# for i in range(len(l1)-1):
#     l3.append(l1[i])
# l3.extend(l2)
# print(l3)

# **********Qestion 59 *********
# Write a Python program to check if the n-th element exists in a given list.
# l=[1,2,3,4,5]
# n=int(input("Enter index:"))
# if(len(l)-1>n-1>0):
#     print("True")
# else:
#     print("False")

# ************Question 60 **********
# Write a Python program to find a tuple, the smallest second index value from a list of tuples.
# l=[(1,5),(2,3),(4,8),(6,1)]
# min=l[0][1]
# for i in l:
#     for j in i:
#         if(j<min):
#             min=j
#             k=i
# print(i)

# *************Question 61 ************
# Write a Python program to create a list of empty dictionaries.
# l=[]
# for i in range(0,5):
#     l.append({})
# print(l)

# ************Question 62***********
# Write a Python program to print a list of space-separated elements.
# l=["Anshul", "Loves", "Python"]
# print(" ".join(l))

# *********Question 63 *************
# Write a Python program to insert a given string at the beginning of all items in a list.  
# Sample list : [1,2,3,4], string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
# l=[1,2,3,4]
# l1=[]
# n=input("Enter string:")
# for i in l:
#     l1.append(n+str(i))
# print(l1)

# ************Question 64 ************
# Write a Python program to iterate over two lists simultaneously.  
# l1=[1, 2, 3]
# l2=['A','B','C']
# for i in range(len(l1)):
#     print(f"{l1[i]} {l2[i]}")

# **********Quetion 65 *************
# Write a Python program to access dictionary keys element by index.  
# d={"name": "Anshul","age": 19,"city": "Gwalior"}
# n=int(input("Enter index:"))
# v=list(d.keys())
# print(v[n])

# *********Question 66 **************
# Write a Python program to find the list in a list of lists whose sum of elements is the highest.  
# Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
# Expected Output: [10, 11, 12]

# l=[1,2,3],[4,5,6],[10,11,12],[7,8,9]
# s=sum(l[0])
# for i in range(len(l)):
#     if(sum(l[i])>s):
#         s=sum(l[i])
#         k=l[i]
# print(k)

# ************Question 67 ************
# Write a Python program to find all the values in a list are greater than a specified number.  
# l=[1,2,3,4,5,6,7,8]
# l1=[]
# n=int(input("Enter value:"))
# for i in l:
#     if(i>n):
#         l1.append(i)
# print(l1)

# *************Question 68 **********  
# Write a Python program to extend a list without append.  
# Sample data: [10, 20, 30]
# [40, 50, 60]
# Expected output : [40, 50, 60, 10, 20, 30]

# l1=[10, 20, 30]
# l2=[40, 50, 60]
# l1.extend(l2)
# print(l1)

# ************Question 69 **********
# Write a Python program to remove duplicates from a list of lists.  
# Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# New List : [[10, 20], [30, 56, 25], [33], [40]]

# l1=[[10, 20],[40],[30, 56, 25], [10, 20], [33], [40]]
# l2=[]
# for i in l1:
#     if(i not in l2):
#         l2.append(i)
# print(l2)

# *************Question 70***********
# Write a Python program to get the depth of a dictionary. 
# d = {"student": {"address": {"city": "Gwalior"}}}
# c=1
# t=d.values()
# for i in t:
#     if(type(i) == dict):
#         c+=1
#         for j in i.values():
#             if(type(j) == dict):
#                 c+=1

# print(c)

# ************Question 71 **************
# Write a Python program to check if all dictionaries in a list are empty or not.  
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False

l=[{},{},{}]
c=True
for i in l:
    if (i != {}):
        c=False
        break
print(c)
