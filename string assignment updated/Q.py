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

x=input("Enter string:")
x=x.split(' ')
max=len(x[0])
for i in x:
    if(len(i)>max):
        max=len(i)
k="Longest word: %s\nLength of the longest word: %d"%(i,max)
print(k)

