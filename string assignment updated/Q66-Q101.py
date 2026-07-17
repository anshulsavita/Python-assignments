# 69 74 75 76 77 80 83 85 92 95
# *********Question 66 *********incomplete
#  Write a Python program to make two given strings (lower case, may or may not be of the same length) anagrams removing any characters from any of the strings.
# x1=input("Enter first string:")
# x2=input("Enter second string:")
# t=''

# for i in x1:
#     if(i not in t):
#         t=t+i
#         if(i in x2):
#             c1=x1.count(i)
#             c2=x2.count(i) 
#             if(c1 > c2):    
#                 x1=x1.replace(i,'',c1-c2)
#             elif(c2>c1):
#                 x2=x2.replace(i,'',c2-c1)
#         else:
#             x1=x1.replace(i,'')
# for i in x2:
#      if (i not in x1):
#           x2=x2.replace(i,'')
# print(x1)
# print(x2)

# ***********Question 67 ************
# Write a Python program to remove all consecutive duplicates of a given string.
# x=input("Enter string:")
# t=''
# for i in range(len(x)-1):
#     if(x[i]!=x[i+1]):
#         t=t+x[i]
# t=t+x[i]
# print(t)

# ***********Question 68 ************
# Write a Python program to create two strings from a given string. Create the first string using those character which occurs only once and create the second string which consists of multi-time occurring characters in the said string.
# x=[]
# l=[]
# y=''
# z=''
# for i in range(2):
#     v=input(f"Enter string @ {i}:")
#     x.append(v)
# t="".join(x)
# for i in range(len(t)):
#     if(t.count(t[i])==1):
#         y=y+t[i]
#     else:
#         z=z+t[i]
# l.append(y)
# l.append(z)
# print(l)

# *********Question 69 **********incomplete
# Write a Python program to find the longest common sub-string from two given strings.
# x1=input("Enter string:")
# x2=input("Enter string:")
# t=''
# l=[]
# for i in range(len(x1)-1):
#     if(x1[i] in x2):
#         c=x2.find(x1[i])
#         if(c==len(x2)): break
#         if (x1[i+1]==x2[c+1]):
#             t=t+x1[i]
#             l.append(t)
# m=max(l)
# print(m)



# *********Question 70 ************
# Write a Python program to create a string from two given strings concatenating uncommon characters of the said strings.
# x1=input("Enter string:")
# x2=input("Enter string:")
# t=''
# for v in x1:
#     if(v not in x2):
#         t=t+v
# for v in x2:
#     if(v not in x1):
#         t=t+v
# print(t)

# ************Question 71 **********
# Write a Python program to move all spaces to the front of a given string in single traversal.
# x=input("Enter a string with spaces:")
# c=x.count(' ')
# x=x.replace(' ','')
# print(c*' '+x)

# *********Question 72 **********
# Write a Python code to remove all characters except a specified character in a given string.  
# Original string: google
# Remove all characters except g in the said string: gg
# x=input("Enter string:")
# x1=input("Enter chr u want to keep:")
# t=''
# for v in x:
#     if(v==x1):
#         t=t+v
# print(t)

# **********Question 73 **********
# Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string.
# x=input("Enter string:")
# u=0
# l=0
# n=0
# s=0
# for v in x:
#     if(v.isupper()):
#         u+=1
#     elif(v.islower()):
#         l+=1
#     elif(v.isnumeric()):
#         n+=1
#     else:
#         s+=1
# print(f"Uppercase: {u}\nLowercase: {l}\nNumeric: {n}\nSpecial chr: {s}")

# ***********Question 74 *********incomplete
# Write a Python program to find the minimum window in a given string which will contain all the characters of another given string.  
# Example 1
# Input : str1 = " PRWSOERIUSFK "
# str2 = " OSU "
# Output: Minimum window is "OERIUS"

# x1=input("Enter str 1:")
# x2=input("Enter str 2:")
# c=0
# t=''
# for v in x1:
#     if((v in x2 or c<=len(x2))or c==1):
#         t=t+v
#         if (v in x2):
#             c+=1
# print(t)

# ***********Question 75 ***********incomplete
# Write a Python program to find smallest window that contains all characters of a given string. 

# **********Quetion 76 ***********incomplete
# Write a Python program to count number of substrings from a given string of lowercase alphabets with exactly k distinct (given) characters. 

# *********Question 77 *********recheck
# Write a Python program to count number of non-empty substrings of a given string.
# x=input("Enter string:")
# l=len(x)
# t=l*(l+1)//2
# print(t)

# ********* Question 78 ********
# Write a Python program to count characters at same position in a given string (lower and uppercase characters) as in English alphabet.
# x=input("Enter string:")
# x=x.lower()
# t='abcdefghijklmnopqrstuvwxyz'
# c=0
# for i in range(len(x)):
#     if(x[i]==t[i]):
#         c+=1
# print(c)

# ************Question 79 *********
# Write a Python program to find smallest and largest word in a given string.
# x=input("Enter sentence:")
# x=x.split(' ')
# max=x[0]
# min=x[0]
# for v in range(1,len(x)):
#     if(len(x[v])>len(max)):
#         max=x[v]
#     if(len(x[v])<len(min)):
#         min=x[v]
# print(max)
# print(min)

# ***********Question 80************incomplte
# Write a Python program to count number of substrings with same first and last characters of a given string.

# ***********Question 81 ***********
# Write a Python program to find the index of a given string at which a given substring starts. If the substring is not found in the given string return 'Not found'. 
# x=input("Enter sentence:")
# n=input("Enter string u want to find:")
# t=x.find(n)
# if(t>=0):
#     print(t)
# else:
#     print("Not found...")

# **********Question 82 **********
# Write a Python program to wrap a given string into a paragraph of given width.  
# Sample Output:
# Input a string: The quick brown fox.
# Input the width of the paragraph: 10
# Result:
# The quick

# x=input("Enter string:")
# n=int(input("Enter width:"))
# i=0
# while(i<=len(x)):
#     j=0
#     while(j<=n):
#         if(i<len(x)):
#             print(x[i],end='')
#         j=j+1
#         i=i+1
#     print()
    
# **********Question 83 **********incompelte
#  Write a Python program to print four values decimal, octal, hexadecimal (capitalized), binary in a single line of a given integer.  
# Sample Output:
# Input an integer: 25
# Decimal Octal Hexadecimal (capitalized), Binary
# 25 31 19 11001

# ********Question 84 ************
# Write a Python program to swap cases of a given string.  
# Sample Output:
# pYTHON eXERCISES
# jAVA
# nUMpY

# x=input("Enter string:")
# t=''
# for v in x:
#     if(v.isupper()==True):
#         v=v.lower()
#     elif(v.islower()==True):
#         v=v.upper()
#     t=t+v
# print(t)

# *********Question 85***********incomplete..
# Write a Python program to convert a given Bytearray to Hexadecimal string.  
# Sample Output:
# Original Bytearray :
# [111, 12, 45, 67, 109]
# Hexadecimal string:
# 6f0c2d436d

# l=[111,12,45,67,109]
# t=''
# for i in l:
#     c=hex(i)
#     t=t+str(c)
#     t=t.replace('x','')
# print(t)

# **********Qyestion 86 ***********
# Write a Python program to delete all occurrences of a specified character in a given string. 

# x=input("Enter string:")
# n=input("Enter u want to del:")
# t=''
# for v in x:
#     if(v!=n):
#         t=t+v
# print(t)

# **********Question 87 *************
# Write a Python program find the common values that appear in two given strings.  
# Sample Output:
# Original strings:
# Python3
# Python2.7
# Intersection of two said String:
# Python

# x=input("Enter string:")
# x2=input("Enter string:")
# t=''
# for v in x:
#     if(v in x2):
#         t=t+v
# for v in x2:
#     if(v in x):
#         if(v not in t):
#             t=t+v
# print(t)

# **********Question 88 *******
# Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length.  
# Sample Output:
# Input the string: W3resource
# ['Valid string.']

# x=input("Enter string:")
# m=int(input("Enter Minimum length:"))
# l=False
# u=False
# num=False
# length=False
# for v in x:
#     if(v.islower()):
#         l=True
#     elif(v.isupper()):
#         u=True
#     elif(v >= '1' and v <= '9'):
#         num=True
# if(len(x)>=m):
#     length=True
# if((l==True) and (u==True) and (num==True) and (length==True)):
#     print("Valid string...")
# else:
#     print("Invalid string...")

# *********Question 89 ************
# Write a Python program to remove unwanted characters from a given string.
# x=input("Enter string:")
# t=''
# for v in x:
#     if((v>='a' and v<='z') or (v>='A' and v<='Z')):
#         t=t+v
#     elif(v==' '):
#         t=t+v
# print(t)

# **********Question 90 *********
# Write a Python program to remove duplicate words from a given string.
# x=input("Enter string:")
# y=[]
# x=x.split(' ')
# t=''
# for v in x:
#     if(v not in y):
#         t=t+v+' '
#         y.append(v)
# print(t)

# **********Question 91 ********
# Write a Python program to convert a given heterogeneous list of scalars into a string.
# l=['Red',100,-50,'green','w,3,r',12.12,False]
# t=[]
# for v in l:
#     t.append(str(v))
# k=",".join(t)
# print(k)

# **********Question 92 ***********recheck.
# Write a Python program to find the string similarity between two given strings.
# x=input("Enter first string:")
# x2=input("Enter second string:")
# t=''
# for i in x:
#     if(i in x2):
#         t=t+i
# print(t)



# *********Question 93 **********
# Write a Python program to extract numbers from a given string.
# x=input("Enter string with numbers:")
# l=[]
# for v in x:
#     if(v>='0' and v<='9'):
#         l.append(v)
# print(l)

# *******Question 94 *********
# Write a Python program to convert a hexadecimal color code to a tuple of integers corresponding to its RGB components.
# x = input("Enter hexadecimal color code (#RRGGBB): ")
# r = int(x[1:3], 16)
# g = int(x[3:5], 16)
# b = int(x[5:7], 16)
# print((r, g, b))

# ********Question 95 **********incomplete
#  Write a Python program to convert the values of RGB components to a hexadecimal color code. 
# r = int(input("Enter red color value: "))
# g = int(input("Enter green color value:"))
# b = int(input("Enter blue color value:"))

# r = r//16
# g = g//16
# b = b//16
# RGB= '#'+str(r)+str(g)+str(b)
# print(RGB)

# **********Question 96 **********
# Write a Python program to convert a given string to camelcase.
# x=input("Enter string:")
# t=''
# x=x.split(' ')
# for i in range(len(x)):
#     for j in range(len(x[i])):
#         if(i==0 and j==0):
#             k=x[i][j].lower()
#             t=t+k
#         else:
#             if(j==0):
#                 k=x[i][j].upper()
#                 t=t+k
#             else:
#                 t=t+x[i][j]
# print(t)

# **********Question 97 **********
# Write a Python program to convert a given string to snake case. 
# x=input("Enter string:")
# x=x.lower()
# x=x.replace(' ','_')
# print(x)

# *********Question 98 **********
# Write a Python program to decapitalize the first letter of a given string.
# x=input("Enter string:")
# t=''
# for i in range(len(x)):
#     if(i==0):
#         k=x[i].lower()
#         t=t+k
#     else:
#         t=t+x[i]
# print(t)

# **********Question 99 **********
# Write a Python program to split a given multiline string into a list of lines.
# x='''This
# is a
# multiline
# string.'''
# print(x.split('\n'))

# *********Question 100******
# Write a Python program to check whether any word in a given sting contains duplicate characrters or not. Return True or False.
# x=input("Enter string:")
# x=x.split(' ')
# co=True
# for v in x:
#     c=0
#     for i in range(len(v)):
#         c=v.count(v[i])
#         if(c!=1):
#             co=False
# if(co==True):
#     print("True")
# else:
#     print("False")

# **********Question 101********
# Write a Python program to add two strings as they are numbers (Positive integer values). Return a message if the numbers are string.

# x = input("Enter string 1: ")
# x1 = input("Enter string 2: ")

# if x.isnumeric() and x1.isnumeric():
#     s = int(x) + int(x1)
#     print(s)
# else:
#     print("Error in input!")