# 26,27
# ********Question 21**********
# Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters. 
# x=input("Enter string:")
# c=0
# for i in range(0,4):
#     if(x[i].isupper()==True):
#         c+=1
# if(c>=2):
#     x=x.upper()
# print(x)

# *********Question 22*********
# Write a Python program to sort a string lexicographically.
# x=input("Enter string:")
# x=sorted(x)
# print("".join(x))

# ********Question 23********
# Write a Python program to remove a newline in Python.
# x="xxxxx\nyyyyy"
# x=x.replace("\n",'')
# print(x)

# *********Question 24********
# Write a Python program to check whether a string starts with specified characters.
# x=input("Enter string:")
# n=input("Enter character:")
# if(x.startswith(n)):
#     print("Yes string starts with",n)
# else:
#     print("string does not starts with",n)

# ********Question 25******
# Write a Python program to create a Caesar encryption.  
# Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.
# x=input("Enter string:")
# for i in x:
#     if(i=='x'):
#         i=ord('a')
#     elif(i=='y'):
#         i=ord('b')
#     elif(i=='z'):
#         i=ord('c')
#     else:
#         i=ord(i)+3
#     print(chr(i),end='')

# ********Question 26*********incomplete
# Write a Python program to display formatted text (width=50) as output.
# x="Python is a very popular programming language used for web development, data science, artificial intelligence and automation"
# x=x.split(' ')
# for i in range(len(x)):
#     print(x[i]+" ",end='')
#     if(i%50==0 and i>1):
#         print()

# ********Question 27********incomplete
# Write a Python program to remove existing indentation from all of the lines in a given text.

# *******Question 28********
# Write a Python program to add a prefix text to all of the lines in a string.
# x='''Anshul
# rohit
# ashwini'''
# n=input("Enter prefix:")
# x=x.split("\n")
# for i in x:
#     print(n+i)

# ********Question 29*******
# x='''line 1
# line 2
# line 3'''
# n=input("Enter prefix:")
# x=x.split("\n")
# for i in range(len(x)):
#     if(i==0):
#         print(n+x[i])
#     else:
#         print(x[i])

# *********Question 30*******
# Write a Python program to print the following floating numbers upto 2 decimal places. 
# x = float(input("Enter a number: "))
# print("{:.2f}".format(x))

# ********Question 31 ********
# Write a Python program to print the following floating numbers upto 2 decimal places with a sign.  
# x = float(input("Enter a number: "))
# if(x>0):
#     print("+{:.2f}".format(x))
# else:
#     print("{:.2f}".format(x))

# *********Question 32 ********
# Write a Python program to print the following floating numbers with no decimal places. 
# x = float(input("Enter a number: "))
# print("{:.0f}".format(x))

# ********Question 33 *******
# Write a Python program to print the following integers with zeros on the left of specified width.  
# x=(input("Enter number: "))
# n=int(input("Enter width: "))
# t=x.rjust(n,"0")
# print(t)

# *******Question 34******
# Write a Python program to print the following integers with '*' on the right of specified width.
# x=(input("Enter number: "))
# n=int(input("Enter width: "))
# t=x.ljust(n,"*")
# print(t)

# *********Question 35*********
# Write a Python program to display a number with a comma separator.
# x = input("Enter a large number: ")
# j = len(x)
# for i in range(len(x)):
#     print(x[i], end='')
#     j -= 1
#     if(j>0 and j%3==0):
#         print(",", end='')

# **********Question 36********
# Write a Python program to format a number with a percentage.
# x=float(input("Enter number"))
# t=x*100
# print(t,"%")

# **********Question 37 ********
# Write a Python program to display a number in left, right and center aligned of width 10.
# x=input("Enter number:")
# n=int(input("Enter width:"))
# print(x.ljust(n,' '))
# print(x.rjust(n,' '))
# print(x.center(n,' '))

# *********Question 38 **********
#  Write a Python program to count occurrences of a substring in a string.
# x=input("Enter string:")
# n=input("Enter substring u want to count:")
# print(x.count(n))

# *******Question 39 **********
# Write a Python program to reverse a string.
# x=input("Enter string:")
# print(x[len(x)::-1])

# ********Question 40 *********
#  Write a Python program to reverse words in a string.
# x=input("Enter a sentence:")
# x=x.split(' ')
# t=x[len(x)::-1]
# print(" ".join(t))

# *******Question 41*******
# Write a Python program to strip a set of characters from a string.
# example --> #####anshul####
x=input("Enter string")
n=input("Enter u want to strip:")
print(x.strip(n))