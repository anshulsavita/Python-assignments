# --> 52,43
# *********Question 42***********incomplete
# Write a Python program to count repeated characters in a string.  
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2

# x=input("Enter string:")
# x=sorted(x)
# for i in x:
#     c=x.count(i)
#     if(c>1):
#         print("%s: %d"%(i,c))

# ***********Question 43 ***********incomplete
# Write a Python program to print the square and cube symbol in the area of a rectangle and volume of a cylinder.  
# Sample output:
# The area of the rectangle is 1256.66cm2
# The volume of the cylinder is 1254.725cm3

# ********Question 44 ***********
# Write a Python program to print the index of the character in a string.  
# Sample string: w3resource
# Expected output:
# Current character w position at 0
# Current character 3 position at 1
# Current character r position at 2
# Current character c position at 8
# Current character e position at 9

# x=input("Enter string:")
# for i,v in enumerate(x):
#     print('Current character %s position %d'%(v,i))

# *********Question 45********
# Write a Python program to check whether a string contains all letters of the alphabet.  
# x=input("Enter string:")
# x=x.lower()
# c=0
# for i in x:
#     if(i>='a' and i<='z'):
#         c+=1
# if(c==len(x)):
#     print("yes all letters are alphabet")
# else:
#     print("no all letters are not alphabet")

# ********Question 46 ********
# Write a Python program to convert a given string into a list of words.  
# Sample Output:
# ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
# ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']

# x=input("Enter string:")
# x=x.split(' ')
# print(x)

# **********Question 47 **********
# Write a Python program to lowercase first n characters in a string.
# x=input("Enter string:")
# n=int(input("Enter value of n:"))
# x=x.upper()
# t=''
# for i in range(len(x)):
#     if(i<=n):
#         t=t+x[i].lower()
#     else:
#         t=t+x[i]
# print(t)

# **********Question 48 **********
# Write a Python program to swap comma and dot in a string.  
# Sample string: "32.054,23"
# Expected Output: "32,054.23"

# x=input("Enter value:")
# t=''
# for i in range(len(x)):
#     if(x[i]==','):
#         t=t+x[i].replace(',','.')
#     elif(x[i]=='.'):
#         t=t+x[i].replace('.',',')
#     else:
#         t=t+x[i]
# print(t)

# *********Question 49***********
# Write a Python program to count and display the vowels of a given text.
# x=input("Enter string:")
# x=x.upper()
# for i in 'AEIOU':
#     if(i in x):
#         c=x.count(i)
#         print("%s: %d"%(i,c))

# ********Question 50 ***********
# Write a Python program to split a string on the last occurrence of the delimiter.
# x=input("Enter string:")
# x=x.rsplit(' ',1)
# print(x)

# ******** or ******
# x=input("Enter string:")
# n=input("What is delimeter:")
# x=x.rsplit(n,1)
# print(x)

# ********Question 51********
# Write a Python program to find the first non-repeating character in given string.
# x=input("Enter string:")
# for i in x:
#     if(x.count(i)==1):
#         print(i)
#         break
        

# *********Question 52 ***********incomplete
#  Write a Python program to print all permutations with given repetition number of characters of a given string.

# ********Question 53 ************
# Write a Python program to find the first repeated character in a given string. 
# x=input("Enter string:")
# for i in x:
#     if(x.count(i)>1):
#         print(i)
#         break

# ***********Question 54 *********
# Write a Python program to find the first repeated character of a given string where the index of first occurrence is smallest.
# x=input("Enter string:")
# for i in x:
#     if(x.count(i)>1):
#         print(i)
#         break

# **********Question 55*********
# Write a Python program to find the first repeated word in a given string.
# x=input("Enter sentence:")
# x=x.split(' ')
# for i in x:
#     if(x.count(i)>1):
#         print(i)
#         break

# ********Question 56 **********
# Write a Python program to find the second most repeated word in a given string.
# x=input("Enter sentence:")
# c=0
# x=x.split(' ')
# for i in x:
#     if(x.count(i)>1):
#         c+=1
#     if(c>1):
#         print(i)
#         break

# *********Question 57 *********
# Write a Python program to remove spaces from a given string.
# x=input("Enter a setence:")
# x=x.replace(" ",'')
# print(x)

# *********Question 58 ********
# Write a Python program to move spaces to the front of a given string.
# x=input("Enter sentence:")
# c=x.count(' ')
# x=x.replace(" ",'')
# print(c*' '+x)

# **********Question 59 ***********
# Write a Python program to find the maximum occurring character in a given string.
# x=input("Enter string:")
# x=x.replace(' ','')
# m=x.count(x[0])
# ch=x[0]
# for i in range(len(x)):
#     c=x.count(x[i])
#     if(c>m):
#         m=c
#         ch=x[i]
# print(ch)

# **********Question 60 ***********
# Write a Python program to capitalize first and last letters of each word of a given string.
# x=input("Enter string:")
# x=x.split(' ')
# t=''
# for i in x:
#     t=t+i[0].upper()+i[1:len(i)-1]+i[len(i)-1].upper()+' '
# print(t)

# *********Question 61*********
# Write a Python program to remove duplicate characters of a given string.
# x=input("Enter string:")
# t=''
# for i in range(len(x)):
#     if(x[i] not in t):
#         t=t+x[i]
# print(t)

# ********Question 62 **********
# Write a Python program to compute sum of digits of a given string.
# x=input("Enter string with numbers:")
# s=0
# for i in x:
#     if(i>='0' and i<='9'):
#         s=s+int(i)
# print(s)

# *********Question 63**********
# Write a Python program to remove leading zeros from an IP address.
# x="192.168.001.001"
# x=x.split('.')
# for i in range(len(x)):
#     x[i]=x[i].lstrip('0')
# print(".".join(x))

# ********Question 64**********
# Write a Python program to find maximum length of consecutive 0's in a given binary string.
# x="10000100100000"
# x=x.split('1')
# max=len(x[0])
# for i in range(len(x)):
#     if(len(x[i])>max):
#         max=len(x[i])
# print(max)

# *******Question 65**********
# Write a Python program to find all the common characters in lexicographical order from two given lower case strings. If there are no common letters print "No common characters".
x1=input("Enter first string:")
x2=input("Enter second string:")
x1=x1.lower()
x2=x2.lower()
i=97
while(i<=122):
    if(chr(i) in x1 and chr(i) in x2):
        print(chr(i))
    i=i+1


