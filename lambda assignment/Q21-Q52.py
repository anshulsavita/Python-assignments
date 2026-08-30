# incomplete --> 46
# ************Question 21**********
# Write a Python program that multiply each number of given list with a given number using lambda function. Print the result.  
# Original list: [2, 4, 6, 9, 11]
# Given number: 2
# Result:
# 4 8 12 18 22

# l=[2,4,6,9,11]
# n=int(input("Enter number:"))
# k=list(map(lambda a: a*n,l))
# print(k)

# **************Question 22 **********
# . Write a Python program that sum the length of the names of a given list of names after removing the names that starts with an lowercase letter. Use lambda function.  
# Result:
# 16

# l=['Anshul', 'rahul', 'Aman', 'rohit']
# k=list(filter(lambda a: a[0].isupper(),l))
# c=0
# for i in k:
#     c=c+len(i)
# print(c)

# ***************Question 23 **********
# Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using lambda function.  
# Original list: [2, 4, -6, -9, 11, -12, 14, -5, 17]
# Sum of the positive numbers: -32
# Sum of the negative numbers: 48

# x = [2, 4, -6, -9, 11, -12, 14, -5, 17]
# p=list(filter(lambda a: a>0,x))
# n=list(filter(lambda a: a<0,x))
# print("Sum of positive numbers:",sum(p))
# print("Sum of negative numbers:",sum(n))

# **************Question 24***********
# Write a Python program to find numbers within a given range where every number is divisible by every digit it contains.  
# Sample Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
# x=['11','12','13','14','15','16','17',"18","19","20"]
# x = range(1, 23)
# def find(a):
#     c=0
#     for j in str(a):
#         if(int(j)==0):
#             c=c-1
#             break
#         elif(int(a)%int(j)==0):
#             c=c+1
#     if(c==len(str(a))):
#         return a

# x1 = list(filter(lambda i: find(i), x))
# print(x1)
# ************Question 25 **************
# Write a Python program to create the next bigger number by rearranging the digits of a given number.  
# Original number: 12
# Next bigger number: 21
# Original number: 10
# Next bigger number: False
# Original number: 201
# Next bigger number: 210
# Original number: 102
# Next bigger number: 120
# Original number: 445
# Next bigger number: 454

# from itertools import permutations
# x=input("Enter number:")
# l=list(permutations(x))
# l1=list(map(lambda a:"".join(a),l))
# f=list(filter(lambda a: int(a)>int(x),l1))
# print(f[0])

# **************Question 26 ***********
# Write a Python program to find the list with maximum and minimum length using lambda.  
# Original list:
# [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])

# x = [[0],[1,3],[5,7],[9,11],[13,15,17]]
# m = max(x, key=lambda a: len(a))
# mi=min(x, key=lambda a: len(a))
# print((len(m),m))
# print((len(mi),mi))

# *************Question 27 *************
# Write a Python program to sort each sublist of strings in a given list of lists using lambda.  
# Original list:
# [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
# After sorting each sublist of the said list of lists:
# [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]

# l=[['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
# l1=list(map(lambda a: sorted(a),l))
# print(l1)

# *************Question 28 **************
# Write a Python program to sort a given list of lists by length and value using lambda.  
# Original list:
# [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
# Sort the list of lists by length and value:
# [[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]

# l = [[2],[0],[1,3],[0,7],[9,11],[13,15,17]]
# l1 = sorted(l, key=lambda x: (len(x), x))
# print(l1)

# ***************Question 29 ***************
# Write a Python program to find the maximum value in a given heterogeneous list using lambda.  
# Original list:
# ['Python', 3, 2, 4, 5, 'version']
# Maximum values in the said list using lambda:
# 5
# l=['Python', '3', '2', '4', '5', 'version']
# l=list(filter(lambda a: int(a.isdigit()),l))
# print(max(l))

# ************Question 30 ***************
# Write a Python program to sort a given matrix in ascending order according to the sum of its rows using lambda.  
# Original Matrix:
# [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# Sort the said matrix in ascending order according to the sum of its rows
# [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
# Original Matrix:
# [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
# Sort the said matrix in ascending order according to the sum of its rows
# [[-2, 4, -5], [1, -1, 1], [1, 2, 3]]

# l=[[1,2,3],[2,4,5],[1,1,1]]
# l1=sorted(l,key=lambda a:sum(a))
# print(l1)

# **************Question 31************
# Write a Python program to extract specified size of strings from a give list of string values using lambda.  
# Original list:
# ['Python', 'list', 'exercises', 'practice', 'solution']
# length of the string to extract:
# 8
# After extracting strings of specified length from the said list:
# ['practice', 'solution']

# l=['Python', 'list', 'exercises', 'practice', 'solution']
# n=int(input("Enter length:"))
# l1=list(filter(lambda a: len(a)==n,l))
# print(l1)

# ************Question 32***************
# Write a Python program to count float number in a given mixed list using lambda.  
# Original list:
# [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# Number of floats in the said mixed list:
# 3
c=0
# l=[1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# k=list(map(lambda x: isinstance(x, float),l))
# k1=k.count(True)
# print(k1)

# **************Question 33 ****************
# Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length using lambda.  
# Input the string: W3resource
# ['Valid string.']
# x='W3resource'
# n=10
# k=list(map(lambda a: a.isupper() or a.islower or a.isdigit or len(a)==n,x))
# if(k.count(False)>0):
#     print('inValid String....')
# else:
#     print('Valid String....')


# *************Question 34 ******************
# Write a Python program to filter the height and width of students, which are stored in a dictionary using lambda.  
# Original Dictionary:
# {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# Height> 6ft and Weight> 70kg:
# {'Cierra Vega': (6.2, 70)}

# d={'Cierra Vega': (6.2, 70),'Alden Cantrell': (5.9, 65),'Kierra Gentry': (6.0, 68),'Pierre Cox': (5.8, 66)}
# k=dict(filter(lambda x: x[1][0]>6 and x[1][1]>=70,d.items()))
# print(k)

# **************Question 35 ******************
# Write a Python program to check whether a specified list is sorted or not using lambda.  
# Original list:
# [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
# Is the said list is sorted!
# True
# Original list:
# [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
# Is the said list is sorted!
# False

# l = [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
# r = sorted(l, key=lambda x: x)
# print(l==r)

# ***************Question 36 ****************
# Write a Python program to extract the nth element from a given list of tuples using lambda.  
# Original list:
# [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
# Extract nth element ( n = 0 ) from the said list of tuples:
# ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
# Extract nth element ( n = 2 ) from the said list of tuples:
# [99, 96, 94, 98]

# l=[('Greyson Fulton', 98, 99),('Brady Kent', 97, 96),('Wyatt Knott', 91, 94),('Beau Turnbull', 94, 98)]
# n=1
# k=list(map(lambda a: a[n],l))
# print(k)

# ************Question 37 ***************
# Write a Python program to sort a list of lists by a given index of the inner list using lambda.  
# Original list:
# [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
# Sort the said list of lists by a given index ( Index = 0 ) of the inner list
# [('Beau Turnbull', 94, 98), ('Brady Kent', 97, 96), ('Greyson Fulton', 98, 99), ('Wyatt Knott', 91, 94)]
# Sort the said list of lists by a given index ( Index = 2 ) of the inner list
# [('Wyatt Knott', 91, 94), ('Brady Kent', 97, 96), ('Beau Turnbull', 94, 98), ('Greyson Fulton', 98, 99)]

# l=[('Greyson Fulton', 98, 99),('Brady Kent', 97, 96),('Wyatt Knott', 91, 94),('Beau Turnbull', 94, 98)]
# n=1
# k=sorted(l,key=lambda a: a[n])
# print(k)

# ***********Question 38 ***************
# Write a Python program to remove all elements from a given list present in another list using lambda.  
# Original lists:
# list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2: [2, 4, 6, 8]
# Remove all elements from 'list1' present in 'list2:
# [1, 3, 5, 7, 9, 10]

# l1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# l2= [2, 4, 6, 8]
# k=list(filter(lambda x: x not in l2,l1))
# print(k)

# ************Question 39 **************
# Write a Python program to find the elements of a given list of strings that contain specific substring using lambda.  
# Original list:
# ['red', 'black', 'white', 'green', 'orange']
# Substring to search:
# ack
# Elements of the said list that contain specific substring:
# ['black']
# Substring to search:
# abc
# Elements of the said list that contain specific substring:
# []

# l=['red', 'black', 'white', 'green', 'orange']
# n='ack'
# k=list(filter(lambda x: n in x,l))
# print(k)

# ************Question 40 **************
# Write a Python program to find the nested lists elements, which are present in another list using lambda.  
# Original lists: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
# Intersection of said nested lists:
# [[12], [7, 11], [1, 5, 8]]

# l1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# l2=[[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
# k= list(map(lambda x: list(filter(lambda y: y in l1, x)), l2))
# print(k)

# ************Question 41 *************
# Write a Python program to reverse strings in a given list of string values using lambda.  
# Original lists:
# ['Red', 'Green', 'Blue', 'White', 'Black']
# Reverse strings of the said given list:
# ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']

# l=['Red', 'Green', 'Blue', 'White', 'Black']
# k=list(map(lambda x: x[-1::-1],l))
# print(k)

# ************Question 42 **************
# Write a Python program to calculate the product of a given list of numbers using lambda.  
# list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Product of the said list numbers:
# 3628800
# list2: [2.2, 4.12, 6.6, 8.1, 8.3]
# Product of the said list numbers:
# 4021.8599520000007

# import functools as ft
# l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# k=ft.reduce(lambda a,b:a*b,l)
# print(k)

# *************Question 43 **************
# Write a Python program to multiply all the numbers in a given list using lambda.  
# Original list:
# [4, 3, 2, 2, -1, 18]
# Mmultiply all the numbers of the said list: -864
# Original list:
# [2, 4, 8, 8, 3, 2, 9]
# Mmultiply all the numbers of the said list: 27648

# import functools as ft
# l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# k=ft.reduce(lambda a,b:a*b,l)
# print(k)

# ************Question 44 ***************
# Write a Python program to calculate the average value of the numbers in a given tuple of tuples using lambda.  
# Original Tuple:
# ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
# Average value of the numbers of the said tuple of tuples:
# (30.5, 34.25, 27.0)
# Original Tuple:
# ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
# Average value of the numbers of the said tuple of tuples:
# (25.5, -18.0, 3.75)

# l = ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
# k = tuple(map(lambda i: sum(map(lambda x: x[i], l)) / len(l), range(3)))
# print(k)


# *************Question 45 ******************
# Write a Python program to convert string element to integer inside a given tuple using lambda.  
# Original tuple values:
# (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))
# New tuple values:
# ((233, 33), (1416, 55), (2345, 34))

# l = (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))
# k=tuple(map(lambda x: tuple(map(lambda y: int(y), filter(lambda y: y.isdigit(), x))), l))
# print(k)

# *************Question 46 ************incomplete...
# Write a Python program to find index position and value of the maximum and minimum values in a given list of numbers using lambda.  
# Original list:
# [12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]
# Index position and value of the maximum value of the said list:
# (5, 89)
# Index position and value of the minimum value of the said list:
# (3, 10.11)

# *************Question 47 *************
# Write a Python program to sort a given mixed list of integers and strings using lambda. Numbers must be sorted before strings.  
# Original list:
# [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
# Sort the said mixed list of integers and strings:
# [1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']

# l=[19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
# l1=list(filter(lambda a: str(a).isdigit(),l))
# l2=list(filter(lambda a: str(a).isalpha(),l))
# k=sorted(l1)
# k.extend(sorted(l2))
# print(k)

# *************Question 48 **************
# Write a Python program to sort a given list of strings(numbers) numerically using lambda.  
# Original list:
# ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
# Sort the said list of strings(numbers) numerically:
# ['-500', '-12', '0', '4', '7', '12', '45', '100', '200']

# l=['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
# k=sorted(l,key= lambda a: int(a))
# print(k)

# **************Question 49 *************
# Write a Python program to count the occurrences of the items in a given list using lambda.  
# Original list:
# [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
# Count the occurrences of the items in the said list:
# {3: 4, 4: 2, 5: 3, 8: 2, 0: 2, 1: 1, 2: 2}

# l = [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
# k=dict(map(lambda x: (x, l.count(x)),set(l)))
# print(k)

# *************Question 50 ****************
# Write a Python program to remove specific words from a given list using lambda.  
# Original list:
# ['orange', 'red', 'green', 'blue', 'white', 'black']
# Remove words:
# ['orange', 'black']
# After removing the specified words from the said list:
# ['red', 'green', 'blue', 'white']

# l1=['orange', 'red', 'green', 'blue', 'white', 'black']
# l2=['orange', 'black']
# k=list(filter(lambda x: x not in l2 ,l1))
# print(k)

# ************Question 51 *************
# Write a Python program to find the maximum and minimum values in a given list of tuples using lambda function.  
# Original list with tuples:
# [('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
# Maximum and minimum values of the said list of tuples:
# (74, 62)

# l=[('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
# k=list(map( lambda x: list(filter(lambda y: str(y).isdigit(),x)),l))
# print("Minimum",sorted(k[0]))
# print("Maximum",sorted(k[-2]))

# ************Question 52 *********
# Write a Python program to remove None value from a given list using lambda function.  
# Original list:
# [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
# Remove None value from the said list:
# [12, 0, 23, -55, 234, 89, 0, 6, -12]

l=[12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
k=list(filter(lambda x: x!=None,l))
print(k)