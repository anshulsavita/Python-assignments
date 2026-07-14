# 15,26,27,43,52,66,69,74,75,76,80,82,83,85,92,95
# *********Question 1*******
# Write a python program to calculate the length of a string.
# x=input("Enter string:")
# print(len(x))

# **********Question 2*****
# write a python program to count the number of characters (character frequency) in a string. simple string: 'google.com'
# x='google.com'
# t=x.lower()
# for i in t:
#     if(i in t):
#         c=t.count(i)
#         print(i,": ",c,sep='')

# x='google.com'
# t=[]
# for v in x:
#     if(v not in t):
#         t.append(v)
# for v in t:
#     print(v,":",x.)
# *********Question 3********
# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.  Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String

# x=input("Enter string:")
# l=len(x)
# if(l>=2):
#     print(x[:2]+x[l-2:])
# else:
#     print("Empty string....")

# **********Question 4********
# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.  Sample String : 'restart'
# Expected Result : 'resta$t'

# x=input("Enter string:")
# i=x.replace(x[0],'$')
# i=i.replace('$',x[0],1)
# print(i)

# *************Question 5*******
# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.  
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

# x=input("Enter first string:")
# y=input("Enter second string:")
# i=y[:2]+x[2:]
# j=x[:2]+y[2:]
# c=i+" "+j 
# print(c)

# ************Question 6 ***********
# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.  
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

# x=input("Enter string:")
# if(len(x)<3):
#     print(x)
# else:
#     if(x.endswith('ing')):
#         x=x+'ly'
#     else:
#         x=x+'ing'
#     print(x)

# ***********Question 7**********
# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.  
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

# x=input("Enter string:")
# t1=x.find('not')
# t2=x.find('poor',t1)
# if(t1<t2):
#     x=x.replace(x[t1:t2+4],"good")
# print(x)

# **********Question 8********
# Write a Python function that takes a list of words and return the longest word and the length of the longest one.  
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9

# x=input("Enter string:")
# x=x.split(' ')
# max=len(x[0])
# strmax=x[0]
# for i in x:
#     if(len(i)>max):
#         max=len(i)
#         strmax=x[i]

# k="Longest word: %s\nLength of the longest word: %d"%(i,max)
# print(k)

# *********Question 9*******
# write a python program to remove the nth index character from a nonempty string.
# x=input("Enter string:")
# n=int(input("Enter nth index:"))
# i=0
# t=''
# while(i<len(x)):
#     if(i!=n):
#         t=t+x[i]
#     i=i+1
# print(t)


# **********Question 10*******
# Write a Python program to change a given string to a new string where the first and last chars have been exchanged. 
# x=input("Enter string:")
# t=x[len(x)-1]+x[1:len(x)-1]+x[0]
# print(t)

# *********Question 11********
# Write a Python program to remove the characters which have odd index values of a given string.
# x=input("Enter string:")
# i=0
# t=''
# while(i<len(x)):
#     if(i%2==0):
#         t=t+x[i]
#     i=i+1
# print(t)

# *********Question 12********
# Write a Python program to count the occurrences of each word in a given sentence. 
# x=input("Enter string:")
# x=x.split(' ')
# x=sorted(x)
# t=0
# for i in x:
#     if(t==0):
#         c=x.count(i)
#         print(i,": ",c,sep='')
#         t=1
#     else:
#         t=0

# **********Question 13********
# Write a Python script that takes input from the user and displays that input back in upper and lower cases. 
# x=input("Enter string:")
# print(x.upper())
# print(x.lower())

# ********Question 14******
# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).  
# Sample Words : red, white, black, red, green, black
# x=input("Enter comma separeted string:")
# if(' ' in x):
#     x=x.replace(' ','')
# x=x.split(',')
# x=sorted(x)
# i=0
# t=''
# while(i<len(x)-1):
#     if(x[i]!=x[i+1]):
#         t=t+x[i]+' '
#     i=i+1
# t=t+x[i]
# print(t)

# ***********Question 15********incomplete
# Write a Python function to create the HTML string with tags around the word(s).  
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'

# ************Question 16******
# Write a Python function to insert a string in the middle of a string.  
# Sample function and result :
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
# x="[[]]"
# t='Python'
# t=x[:len(x)//2]+t+x[len(x)//2:]
# print(t)

# ***********Question 17*********
# Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).  
# Sample function and result :
# insert_end('Python') -> onononon
# insert_end('Exercises') -> eseseses

# x=input("Enter string:")
# if(len(x)>=2):
#     x=x[len(x)-2:]*4
# print(x)

# ***********Question 18********
# Write a Python function to get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string.  
# Sample function and result :
# first_three('ipy') -> ipy
# first_three('python') -> pyt

# x=input("Enter string:")
# if(len(x)>=3):
#     x=x[:3]
# print(x)

# *********Question 19 *********
# Write a Python program to get the last part of a string before a specified character.  
# https://www.w3resource.com/python-exercises
# https://www.w3resource.com/python

# x=input("Enter a sentence:")
# n=input("Enter chr where after you want to remove:")
# n=x.find(n)
# print(x[:n])

# *********Question 20 **********
# Write a Python function to reverses a string if it's length is a multiple of 4.
# x=input("Enter string:")
# if(len(x)%4==0):
#     x=x[len(x)-1::-1]
#     print(x)
# else:
#     print("length of string is not a multiple of 4...")

