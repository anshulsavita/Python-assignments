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

# **************Question 24***********incomplete...
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

# **************Question 25 ***********
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

# *************Question 26 *************
# Write a Python program to sort each sublist of strings in a given list of lists using lambda.  
# Original list:
# [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
# After sorting each sublist of the said list of lists:
# [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]


