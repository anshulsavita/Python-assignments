# ************Question 1************
# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and print the result.  
# k1= lambda a: a+15
# k2= lambda x,y: x*y
# c=k1(20)
# c2=k2(5,3)
# print(c,c2)

# ************Question 2**********
# Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.  
# Sample Output:
# Double the number of 15 = 30
# Triple the number of 15 = 45
# Quadruple the number of 15 = 60
# Quintuple the number 15 = 75

# def multiply(n):
#     return lambda x: x * n
# d = multiply(2)
# t = multiply(3)
# qua = multiply(4)
# qui = multiply(5)

# print("Double:", d(15))
# print("Triple:", t(15))
# print("Quadruple:", qua(15))
# print("Quintuple:", qui(15))

# *********Question 3 *************
# Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

# l=[('English', 88),('Science', 90),('Maths', 97),('Social sciences', 82)]
# R=sorted(l,key=lambda A:A[1])
# print(R)

# ************Question 4 ************
# Write a Python program to sort a list of dictionaries using Lambda.  
# Original list of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# Sorting the List of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]

# l=[{'make': 'Nokia', 'model': 216, 'color': 'Black'},
#    {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
#    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# R=sorted(l,key=lambda a: a['color'])
# print(R)

# **************Question 5 *************
# Write a Python program to filter a list of integers using Lambda.  
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Even numbers from the said list:
# [2, 4, 6, 8, 10]
# Odd numbers from the said list:
# [1, 3, 5, 7, 9]

# l=[1,2,3,4,5,6,7,8,9,10]
# r1=list(filter(lambda a:a%2==0,l))
# r2=list(filter(lambda a:a%2!=0,l))
# print(f"Even: {r1}\nOdd: {r2}")
# *************Question 6 **************
# Write a Python program to square and cube every number in a given list of integers using Lambda.  
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Square every number of the said list:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Cube every number of the said list:
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

# l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# r1=list(map(lambda a: a*a,l))
# r2=list(map(lambda a: a*a*a,l))
# print(f"Square: {r1}\nCube: {r2}")

# ****************Question 7 ***********
# Write a Python program to find if a given string starts with a given character using Lambda.  
# Sample Output:
# True
# False

# k=lambda a,n: 'True' if a.startswith(n) else 'False'
# r=k("Anshul","A")
# print(r)

# ***************Question 8 ***************
# Write a Python program to extract year, month, date and time using Lambda.  
# Sample Output:
# 2020-01-15 09:03:32.744178
# 2020
# 1
# 15
# 09:03:32.744178

# def dateTime(a):
#     l=[]
#     a=a.split('-')
#     for i in a:
#         if(" " in i):
#             l.extend(i.split(' '))
#         else:
#             l.append(i)
#     return l

# k=dateTime("2020-01-15 09:03:32.744178")
# print(k)

# *********************************
# date='12-07-2021 10:10:00'
# k=date.split()
# l=lambda T:T.split('-')
# D=l(k[0])
# print("Year:",D[2])
# print("Month:",D[1])
# print("Date:",D[0])

# **************Question 9 ****************
# Write a Python program to check whether a given string is number or not using Lambda. 
# k=lambda a:  'True' if a.isdigit() else 'False'
# r=k('anshul')
# print(r)

# ************Question 10**************incomplete....
# Write a Python program to create Fibonacci series upto n using Lambda.  
# Fibonacci series upto 2:
# [0, 1]
# Fibonacci series upto 5:
# [0, 1, 1, 2, 3]
# Fibonacci series upto 6:
# [0, 1, 1, 2, 3, 5]
# Fibonacci series upto 9:
# [0, 1, 1, 2, 3, 5, 8, 13, 21]
# x=[]
# for i in range(0,5):
#     if(i<2):
#         x.append(i)
#     else:
#         x.append(x[i-1]+x[i-2])
# print(x)

# *************************
# def feb(n):
#     x=[]
#     for i in range(0,n):
#         if(i<2):
#             x.append(i)
#         else:
#             x.append(x[i-1]+x[i-2])
#     return x
# k=feb(5)
# print(k)

# *************Question 11 *************
# Write a Python program to find intersection of two given arrays using Lambda.  
# Original arrays:
# [1, 2, 3, 5, 7, 8, 9, 10]
# [1, 2, 4, 8, 9]
# Intersection of the said arrays: [1, 2, 8, 9]

# k=lambda a,b: a.intersection(b)
# a={1, 2, 3, 5, 7, 8, 9, 10}
# b={1, 2, 4, 8, 9}
# i=k(a,b)
# print(i)

# **************Question 12 ****************
# . Write a Python program to rearrange positive and negative numbers in a given array using Lambda.  
# Original arrays:
# [-1, 2, -3, 5, 7, 8, 9, -10]
# Rearrange positive and negative numbers of the said array:
# [2, 5, 7, 8, 9, -10, -3, -1]

# a = [-1,2,-3,5,7,8,9,-10]
# k= sorted(a, key=lambda x: x < 0)
# print(k)

# ****************Question 13 **************
# Write a Python program to count the even, odd numbers in a given array of integers using Lambda.  
# Original arrays:
# [1, 2, 3, 5, 7, 8, 9, 10]
# Number of even numbers in the above array: 3
# Number of odd numbers in the above array: 5

# x = [1,2,3,5,7,8,9,10]
# e = sum(map(lambda a: a % 2 == 0, x))
# o = len(x) - e
# print(e,o)

# **************Question 14 ************
# Write a Python program to find the values of length six in a given list using Lambda.  
# Sample Output:
# Monday
# Friday
# Sunday

# L=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
# k=list(filter(lambda a: len(a)==6,L))
# print(k)

# **************Question 15 **************
# Write a Python program to add two given lists using map and lambda.  
# Original list:
# [1, 2, 3]
# [4, 5, 6]
# Result: after adding two list
# [5, 7, 9]

# l1=[1,2,3]
# l2=[4,5,6]
# k=list(map(lambda a,b: a+b,l1,l2))
# print(k)

# **********Question 16************
# Write a Python program to find the second lowest grade of any student(s) from the given names and grades of each student using lists and lambda. Input number of students, names and grades of each student.  
# Input number of students: 5
# Name: S ROY
# Grade: 1
# Name: B BOSE
# Grade: 3
# Name: N KAR
# Grade: 2
# Name: C DUTTA
# Grade: 1
# Name: G GHOSH
# Grade: 1
# Names and Grades of all students:
# [['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]
# Second lowest grade: 2.0
# Names:
# N KAR

# l=[['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]
# grade=sorted(set(map(lambda a:a[1],l)))
# print(f"Grade: {grade[-2]}")
# for i in l:
#     if(i[1]==grade[-2]):
#         print(f"Name: {i[0]}")

# print("Second lowest grade:", sl)
# print("Names:")

# for v in l:
#     if(v[1] == sl):
#         print(v[0])

# ***************Question 17 ***********
# Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.  
# Orginal list:
# [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
# Numbers of the above list divisible by nineteen or thirteen:
# [19, 65, 57, 39, 152, 190]

# l=[19,65,57,39,152,639,121,44,90,190]
# k=list(filter(lambda a: a%19==0 or a%13==0,l))
# print(k)

# **************Question 18 **************
# . Write a Python program to find palindromes in a given list of strings using Lambda.  
# Orginal list of strings:
# ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
# List of palindromes:
# ['php', 'aaa']

# l=['php','w3r','Python','abcd','Java','aaa']
# k=list(filter(lambda a: a==a[::-1],l))
# print(k)

# ************Question 19 *************
# Write a Python program to find all anagrams of a string in a given list of strings using lambda.  
# Orginal list of strings:
# ['bcda', 'abce', 'cbda', 'cbea', 'adcb']
# Anagrams of 'abcd' in the above string:
# ['bcda', 'cbda', 'adcb']

# l=['bcda','abce','cbda','cbea','adcb']
# k=list(filter(lambda a: sorted(a)==sorted('abcd'),l))
# print(k)

# ************Question 20*************
# Write a Python program to find the numbers of a given string and store them in a list, display the numbers which are bigger than the length of the list in sorted form. Use lambda function to solve the problem.  
# Original string: sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5
# Numbers in sorted form:
# 20 23 56

s="sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"
s=s.split(' ')
k=list(filter(lambda a: a.isdigit(),s))
l=len(k)
t=list(filter(lambda a: int(a)!=l,k))
print(t)