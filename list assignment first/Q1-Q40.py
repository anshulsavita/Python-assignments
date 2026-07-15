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

# *******Question 15 *******incomplete
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

# ********Question 18 *******incomplete
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
# l=[1,[2,3],4,[5,6]]
# t1=[]
# for i in l:
#     if(isinstance(i,list)):
#         t1.extend(i)
#     else:
#         t1.append(i)
# print(t1)

# *********Question 24 ********
# Write a Python program to append a list to the second list.
# l1=[1,2,3]
# l2=[4,5,6]
# l2.extend(l1)
# print(l2)

# **********Question 25 ********incomplte.
#  Write a Python program to select an item randomly from a list.

# *********Question 26************
# Write a python program to check whether two lists are circularly identical.
# l=[1,2,3,4]
# l2=[3,4,1,2]
# c=False
# for i in range(len(l)):
#     t=l[0]
#     l.remove(l[0])
#     l.append(t)
#     if(l==l2):
#         c=True
#         break

# if(c==True):
#     print(f"Yes..,{l} and {l2} are circularly identical.")
# else:
#     print(f"No..,{l} and {l2} are not circularly identical.")

# ********Question 27 ************
#  Write a Python program to find the second smallest number in a list.
# l=[4,7,9,4,2,7,8]
# t=[]
# for i in l:
#     if(i not in t):
#         t.append(i)
# t.sort()
# print(t)
# print(t[1])

# ***********Question 28 *********
# Write a Python program to find the second largest number in a list.
# l=[4,7,9,4,2,7,8]
# t=[]
# for i in l:
#     if(i not in t):
#         t.append(i)
# t.sort()
# print(t)
# print(t[len(t)-2])

# *********Question 29 **********
# Write a Python program to get unique values from a list.
# l=[4,7,9,4,2,7,8]
# t=[]
# for i in l:
#     if(i not in t):
#         t.append(i)
# print(t)

# *********Question 30 ***************
# Write a Python program to get the frequency of the elements in a list. 
# l=[2,2,5,6,7,7,5,4,9,7,9,0,4]
# t=[]
# for i in l:
#     if(i not in t):
#         t.append(i)
#         c=l.count(i)
#         print(f"{i}= {c}")

# **********Question 31 *********
# Write a Python program to count the number of elements in a list within a specified range.
# l=[3,6,8,45,32,12,14,22,30]
# t=[]
# i=int(input("Enter starting range:"))
# j=int(input("Enter ending range:"))
# for v in l:
#     if(v>=i and v <=j):
#         t.append(v)
# print(t)

# *********Question 32 **********
#  Write a Python program to check whether a list contains a sublist.
# l=[1,[1,2],3,4,[5,6]]
# c=False
# for i in l:
#     if(isinstance(i,list)):
#         c=True
#         break
# if(c==True):
#     print(f"Yes..List contains a sublist.")
# else:
#     print(f"No..List does not contain a sublist.")

# *********Question 33 *********
# Write a Python program to generate all sublists of a list.
# l=[1,[1,2],3,4,[5,6]]
# t=[]
# for i in l:
#     if(isinstance(i,list)):
#         t.append(i)
# print(t)

# ************Question 34 **********recheck
# Write a Python program using Sieve of Eratosthenes method for computing primes upto a specified number.  
# l=[]
# x=int(input("Enter number:"))
# for i in range(2,x):
#     if(i%2!=0):
#         l.append(i)
# print(l)

# *************Question 35 ***********
# Write a Python program to create a list by concatenating a given list which range goes from 1 to n.  
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

# l=['p','q']
# t=[]
# n=int(input("Enter number:"))
# for i in range(1,n+1):
#     for j in range(len(l)):
#         x=l[j]+str(i)
#         t.append(x)
# print(t)

# ***************Question 36 ***********recheck
# Write a Python program to get variable unique identification number or string.
# l=[1,'Anshul',8,'Abcd']
# for i in l:
#     print(id(i))

# ************Question 37 ***********
# Write a Python program to find common items from two lists. 
# l=[1,2,3,4,5]
# l2=[4,5,6,7,8]
# t=[]
# for i in l:
#     if(i in l2):
#         t.append(i)
# print(t)

# **********Question 38 ***********
# Write a Python program to change the position of every n-th value with the (n+1)th in a list. 
# l=[0,1,2,3,4,5]
# for i in range(0,len(l)-1,2):
#     t=l[i]
#     l[i]=l[i+1]
#     l[i+1]=t
# print(l)

# ***********Question 39 *********
# Write a Python program to convert a list of multiple integers into a single integer.
# l=[11,33,50]
# t=''
# for i in l:
#     t=t+str(i)
# print(int(t))

# ************Question 40 **********
# Write a Python program to split a list based on first character of word.
l=['Apple','Anshul','Bat','Bomb','Cat','Cow']
t1=''
l1=[]
for i in l:
    if(i not in t1):
        x=i[0]
        t=[]
        for j in l:
            if (j not in t1):
                if(j.startswith(x)):
                    t.append(j)
                    t1=t1+j
        l1.append(t)
print(l1)