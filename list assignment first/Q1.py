# ********Question 1 ********
# Write a Python program to sum all the items in a list.
# l=[]
# for i in range(5):
#     k=int(input("Enter value:"))
#     l.append(k)
# print(sum(l))

# ********Question 2 ********
# Write a Python program to multiplies all the items in a list.
# l=[]
# p=1
# for i in range(5):
#     k=int(input("Enter value:"))
#     p=p*k 
#     l.append(k)
# print(l)
# print("product:",p)

# *********Question 3 *********
# Write a Python program to get the largest number from a list.
# l=[]
# for i in range(5):
#     k=int(input("Enter value:"))
#     l.append(k)
# print(max(l))

# ********Question 4********
# Write a Python program to get the smallest number from a list.
# l=[]
# for i in range(5):
#     k=int(input("Enter value:"))
#     l.append(k)
# print(min(l))

# ********Question 5 *********
# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.  
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
# x=['abc','xyz','aba','121']
# c=0
# for i in x:
#     if(len(i)>2):
#         if(i[0]==i[len(i)-1]):
#             c+=1
# print(c)

# *********Question 6 **********
# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.  
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# l=[(2,5),(1,2),(4,4),(2,3),(2,1)]
# for v in range(len(l)):
#     for i in range(len(l)-1):
#         if(l[i][1]>l[i+1][1]):
#             t=l[i]
#             l[i]=l[i+1]
#             l[i+1]=t
# print(l)

# *********Question 7 ************
# Write a Python program to remove duplicates from a list.
# l=[1,2,3,2,5,3,7]
# y=[]
# for v in l:
#     if(l.count(v)==1):
#         y.append(v)
# print(y)

# ********Question 8********
# Write a Python program to check a list is empty or not.
# l=[1,2,3,4]
# t=[]
# print(any(l))
# print(any(t))

# ********Question 9******
# Write a Python program to clone or copy a list.
# l=[1,2,3,4]
# t=l.copy()
# print(t)

# *********Question 10******
# Write a Python program to find the list of words that are longer than n from a given list of words.
# l=[]
# for i in range(5):
#     k=input("Enter word:")
#     l.append(k)
# n=int(input("Enter value of n:"))
# for v in l:
#     if(len(v)>=n):
#         print(v)

# *********Question 11*************
# Write a Python function that takes two lists and returns True if they have at least one common member.
# x=[1,2,3,4]
# y=[1,5,6,7]
# c=0
# for v in x:
#     if(v in y):
#         print(True)
#         break 

# *********Question 12 **********
# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.  
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

# x=['red','green','white','black','pink','yellow']
# for i in [5,4,0]:
#     n=x.pop(i)
# print(x)

# ********Question 13 **********
# Write a Python program to generate a 3*4*6 3D array whose each element is *
# l=[]
# for k in range(3):
#     t=[]
#     for i in range(3):
#         c=[]
#         for j in range(3):
#             t1=int(input(f"Enter value @ {i},{j}:"))
#             c.append(t1)
#         t.append(c)
#     l.append(t)
# print(l)

# *********Question 14*********
# Write a Python program to print the numbers of a specified list after removing even numbers from
# l=[2,3,4,5,6,7,8,9,10]
# t=[]
# for i in l:
#     if(i%2!=0):
#         t.append(i)
# print(t)

# *******Question 15 *******
# Write a Python program to shuffle and print a specified list. 

# *******Question 16 *******
# Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included). 
# l=[]
# for i in range(1,31):
#     t=i*i
#     l.append(t)
# print(l[:5])
# print(l[-5:])

# **********Question 17******
# Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included).
# l=[]
# for i in range(1,31):
#     t=i*i
#     l.append(t)
# print(l[5:])

# ********Question 18 *******
# Write a Python program to generate all permutations of a list in Python.

# ********Question 19 *******
# Write a Python program to get the difference between the two lists. 
# l=[1,3,5,7]
# t=[1,2,3,4]
# v=[]
# for i in range(len(l)):
#     c=l[i]-t[i]
#     v.append(c)
# print(v)

# *********Question 20 *******
# Write a Python program access the index of a list.
# t=(33,44,55,77,88,99)
# for i,v in enumerate(t):
#     print(i,v)

# *******Question 21 *********
# Write a Python program to convert a list of characters into a string. 
# t=['a','n','s','h','u','l']
# print("".join(t))

# *******Question 22 *********
# Write a Python program to find the index of an item in a specified list. 
# t=[33,44,55,77,88,99]
# n=int(input("Enter elent u want to search:"))
# print(t.index(n))

# *********Question 23 *********
# Write a Python program to flatten a shallow list.