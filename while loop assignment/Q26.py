# *******Question 26***********
# write a python program to check whether a number is prime number or not
# n=int(input('Enter number:'))
# if(n%2==0):
#     print("Its is prime number..")
# else:
#     print("Not a prime number...")

# *********Question 27 ***********
# def armstrong(num):
#     sum=0
#     for i in n:
#         m=1
#         for j in range(1,len(n)+1):
#             m=m*int(i)
#         sum=sum+m
#     if(sum==int(n)):
#         return True
#     else:
#         return False
# n=input("Enter number:")
# k=armstrong(n)
# print(k)

# *************Question 28 ***********
# def perfect(num):
#     sum=0
#     for i in range(1,num):
#         if(num%i==0):
#             sum=sum+i
#     if(sum==num):
#         return True
#     else:
#         return False
# n=int(input("Enter number:"))
# k=perfect(n)
# print(k)

# *************Question 29 ****************
# def strong(num):
#     sum=0
#     for i in num:
#         m=1
#         for j in range(1,int(i)+1):
#             m=m*j
#         sum=sum+m
#     if(sum==int(num)):
#         return True
#     else:
#         return False

# n=input("Enter number:")
# k=strong(n)
# print(k)

# **************Question 30 *****************
# n=int(input('Enter number:'))
# for i in range(1,n+1):
#     if(i%2==0):
#         print(f"{i},",end='')

# ***************Question 31***********
# write a python program to print all Armstrong numbers between 1 to n.
# n=input("Enter number:")
# for x in range(1,int(n)+1):
#     sum=0
#     for i in str(x):
#         m=1
#         for j in range(1,len(str(x))+1):
#             m=m*int(i)
#         sum=sum+m
#     if(sum==x):
#         print(f"{sum},",end='')

# ***************Question 32 **************
# Write a python program to print all the perfect numbers between 1 to n.
# n=int(input("Enter number:"))
# for j in range(1,n+1):
#     sum=0
#     for i in range(1,j):
#         if(j%i==0):
#             sum=sum+i
#     if(sum==j):
#         print(f"{j},",end='')

# ****************Question 33 *************
# Write a python program to print all the Strong numbers between 1 to n.
# n=input("Enter number:")
# for x in range(1,int(n)+1):
#     sum=0
#     for i in str(x):
#         m=1
#         for j in range(1,int(i)+1):
#             m=m*j
#         sum=sum+m
#     if(sum==int(x)):
#         print(f"{sum},",end='')

# *************Question 34 *****************
# Write a python program to enter any number and print its prime factors.
# n=int(input("Enter number:"))
# for i in range(2,n+1):
#     l=False
#     if(n%i==0):
#         for j in range(2,i):
#             if(i%j==0):
#                 l=True
#         if(l==False):
#             print(f"{i},",  end='')

# ************Question 35 **************
# write a python program to find the sum of all prime numbers between 1 to n.
# n=int(input("Enter number:"))
# total=0 
# for i in range(2,n+1):
#     l=False
#     if(i==2):
#         total=total+i
#     else:
#         for j in range(2,i):
#             if(i%j==0):
#                 l=True
#         if(l==False):
#             total=total+i
# print(total)

# *************Question 36 *************
# write a python program to print Fibonacci series up to n terms
# n=int(input("Enter number:"))
# l=[]
# for i in range(0,n+1):
#     if(i<2):
#         l.append(i)
#     else:
#         l.append(l[i-1]+l[i-2])
# print(l)

# ************Question 37 *************
# Write a python program to find one's complement of a binary number.
# x='10011'
# l=[]
# for i in x:
#     if(int(i)==1):
#         l.append('0')
#     else:
#         l.append('1')
# print(''.join(l))

# ************Question 38 ***********
# Write a python program to find two's complement of a binary number.
# x='10011'
# t=False
# l=[]
# for i in range(len(x)-1,-1,-1):
#     if(x[i]!='1' and t==False):
#         l.append(x[i])
#     elif(x[i]=='1' and t==False):
#         l.append(x[i])
#         t=True
#     elif(x[i]=='1' and t==True):
#         l.append('0')
#     elif(x[i]=='0'  and t==True):
#         l.append('1')
# x=''.join(l)
# print(x[-1::-1])

# ***********Question 39 **************
# Write a python program to convert Binary to Octal number system.
# x='11011'
# if(len(x)%3!=0):
#     t=True
#     while(len(x)%3!=0):
#         x=x.rjust(len(x)+1,'0')
# i=0
# l1=[]
# while(i<len(x)):
#     l2=[]
#     for j in range(i,i+3):
#         l2.append(x[j])
#         i+=1
#     if("".join(l2)=='000'):
#         l1.append('0')
#     elif("".join(l2)=='001'):
#         l1.append('1')
#     elif("".join(l2)=='010'):
#             l1.append('2')
#     elif("".join(l2)=='011'):
#             l1.append('3')
#     elif("".join(l2)=='100'):
#             l1.append('4')
#     elif("".join(l2)=='101'):
#             l1.append('5')
#     elif("".join(l2)=='110'):
#             l1.append('6')
#     elif("".join(l2)=='111'):
#             l1.append('7')
# print("".join(l1))

# *************Question 40 ***************
# write a python program to convert Binary to Decimal number system. 
# l1=[]
# t='00101101'
# for i in range(0,len(t)):
#     if(i==0):
#         l1.append(1)
#     else:
#         l1.append((2*l1[i-1]))
# l1.reverse()
# total=0
# for i in range(len(t)):
#     if(t[i]=='1'):
#         total=total+l1[i]
# print(total)

# ************Question 41 ******************
# write a python program to convert Binary to Hexadecimal number system.
# x='10110110'
# if(len(x)%4!=0):
#     t=True
#     while(len(x)%4!=0):
#         x=x.rjust(len(x)+1,'0')
# i=0
# l1=[]
# while(i<len(x)):
#     l2=[]
#     for j in range(i,i+4):
#         l2.append(x[j])
#         i+=1
#     if("".join(l2)=='0000'):
#         l1.append('0')
#     elif("".join(l2)=='0001'):
#         l1.append('1')
#     elif("".join(l2)=='0010'):
#             l1.append('2')
#     elif("".join(l2)=='0011'):
#             l1.append('3')
#     elif("".join(l2)=='0100'):
#             l1.append('4')
#     elif("".join(l2)=='0101'):
#             l1.append('5')
#     elif("".join(l2)=='0110'):
#             l1.append('6')
#     elif("".join(l2)=='0111'):
#             l1.append('7')
#     elif("".join(l2)=='1000'):
#             l1.append('8')
#     elif("".join(l2)=='1001'):
#             l1.append('9')
#     elif("".join(l2)=='1010'):
#             l1.append('A')
#     elif("".join(l2)=='1011'):
#             l1.append('B')
#     elif("".join(l2)=='1100'):
#             l1.append('C')
#     elif("".join(l2)=='1101'):
#             l1.append('D')
#     elif("".join(l2)=='1110'):
#             l1.append('E')
#     elif("".join(l2)=='1111'):
#             l1.append('F')
# print("".join(l1))

# ***************Question 42 ***************
# Write a python program to convert Octal to binary number system.
# x='57'
# t=''
# for j in x:
#     if(j=='0'):
#         t=t+'000'
#     elif(j=='1'):
#         t=t+'001'
#     elif(j=='2'):
#         t=t+'010'
#     elif(j=='3'):
#         t=t+'011'
#     elif(j=='4'):
#         t=t+'100'
#     elif(j=='5'):
#         t=t+'101'
#     elif(j=='6'):
#         t=t+'110'
#     elif(j=='7'):
#         t=t+'111'
# print(t)

# ****************Question 43 *************
# write a python program to convert Octal to Decimal number system.
# l1=[]
# t='246'
# for i in range(0,len(t)):
#     if(i==0):
#         l1.append(1)
#     else:
#         l1.append((8*l1[i-1]))
# l1.reverse()
# total=0
# for i in range(len(t)):
#         total=total+(l1[i]*int(t[i]))
# print(total)

# ******************Question 44 *************
# write a python program to convert Octal to Hexadecimal number system.
# x='57'
# t=''
# for j in x:
#     if(j=='0'):
#         t=t+'000'
#     elif(j=='1'):
#         t=t+'001'
#     elif(j=='2'):
#         t=t+'010'
#     elif(j=='3'):
#         t=t+'011'
#     elif(j=='4'):
#         t=t+'100'
#     elif(j=='5'):
#         t=t+'101'
#     elif(j=='6'):
#         t=t+'110'
#     elif(j=='7'):
#         t=t+'111'
# if(len(t)%4!=0):
#     while(len(t)%4!=0):
#         t=t.rjust(len(t)+1,'0')
# i=0
# l1=[]
# while(i<len(t)):
#     l2=[]
#     for j in range(i,i+4):
#         l2.append(t[j])
#         i+=1
#     if("".join(l2)=='0000'):
#         l1.append('0')
#     elif("".join(l2)=='0001'):
#         l1.append('1')
#     elif("".join(l2)=='0010'):
#         l1.append('2')
#     elif("".join(l2)=='0011'):
#         l1.append('3')
#     elif("".join(l2)=='0100'):
#         l1.append('4')
#     elif("".join(l2)=='0101'):
#         l1.append('5')
#     elif("".join(l2)=='0110'):
#         l1.append('6')
#     elif("".join(l2)=='0111'):
#         l1.append('7')
#     elif("".join(l2)=='1000'):
#         l1.append('8')
#     elif("".join(l2)=='1001'):
#         l1.append('9')
#     elif("".join(l2)=='1010'):
#         l1.append('A')
#     elif("".join(l2)=='1011'):
#         l1.append('B')
#     elif("".join(l2)=='1100'):
#         l1.append('C')
#     elif("".join(l2)=='1101'):
#         l1.append('D')
#     elif("".join(l2)=='1110'):
#         l1.append('E')
#     elif("".join(l2)=='1111'):
#         l1.append('F')
# print("".join(l1))

# ************Question 45 *************
# write a python program to convert Decimal to Binary number system.
# x=25
# l1=[]
# while(x>0):
#     r=x%2
#     x=x//2
#     l1.append(str(r))
# l1.reverse()
# print(''.join(l1))

# **************Question 46 **************
# write a python program to convert Decimal to Octal number system.
# x=125
# l1=[]
# while(x>0):
#     r=x%8
#     x=x//8
#     l1.append(str(r))
# l1.reverse()
# print(''.join(l1))

# **************Question 47 ************
# write a python program to convert Decimal to Hexadecimal number system.
# x=254
# l1=[]
# while(x>0):
#     r=x%16
#     x=x//16
#     l1.append(str(r))
# l1.reverse()
# t=''
# for i in l1:
#     if(int(i)>=0 and int(i)<=9):
#         t=t+i
#     elif(int(i)==10):
#         t=t+'A'
#     elif(int(i)==11):
#         t=t+'B'
#     elif(int(i)==12):
#         t=t+'C'
#     elif(int(i)==13):
#         t=t+'D'
#     elif(int(i)==14):
#         t=t+'E'
#     elif(int(i)==15):
#         t=t+'F'
# print(t)

# ***************Question 48 *************
# write a python program to convert Hexadecimal to binary number system.
# x='2F'
# l=[]
# for i in x:
#     if(i=='0'):
#         l.append('0000')
#     elif(i=='1'):
#         l.append('0001')
#     elif(i=='2'):
#         l.append('0010')
#     elif(i=='3'):
#         l.append('0011')
#     elif(i=='4'):
#         l.append('0100')
#     elif(i=='5'):
#         l.append('0101')
#     elif(i=='6'):
#         l.append('0110')
#     elif(i=='7'):
#         l.append('0111')
#     elif(i==8):
#         l.append('1000')
#     elif(i==9):
#         l.append('1001')
#     elif(i=='A'):
#         l.append('1010')
#     elif(i=='B'):
#         l.append('1011')
#     elif(i=='C'):
#         l.append('1100')
#     elif(i=='D'):
#         l.append('1101')
#     elif(i=='E'):
#         l.append('1110')
#     elif(i=='F'):
#         l.append('1111')
# print("".join(l))

# ****************Question 49 ************
# Write a python program to convert Hexadecimal to octal number system.
# x='2F'
# l=[]
# for i in x:
#     if(i=='0'):
#         l.append('0000')
#     elif(i=='1'):
#         l.append('0001')
#     elif(i=='2'):
#         l.append('0010')
#     elif(i=='3'):
#         l.append('0011')
#     elif(i=='4'):
#         l.append('0100')
#     elif(i=='5'):
#         l.append('0101')
#     elif(i=='6'):
#         l.append('0110')
#     elif(i=='7'):
#         l.append('0111')
#     elif(i==8):
#         l.append('1000')
#     elif(i==9):
#         l.append('1001')
#     elif(i=='A'):
#         l.append('1010')
#     elif(i=='B'):
#         l.append('1011')
#     elif(i=='C'):
#         l.append('1100')
#     elif(i=='D'):
#         l.append('1101')
#     elif(i=='E'):
#         l.append('1110')
#     elif(i=='F'):
#         l.append('1111')
# x="".join(l)
# if(len(x)%3!=0):
#     t=True
#     while(len(x)%3!=0):
#         x=x.rjust(len(x)+1,'0')
# i=0
# l1=[]
# while(i<len(x)):
#     l2=[]
#     for j in range(i,i+3):
#         l2.append(x[j])
#         i+=1
#     if("".join(l2)=='000'):
#         l1.append('0')
#     elif("".join(l2)=='001'):
#         l1.append('1')
#     elif("".join(l2)=='010'):
#             l1.append('2')
#     elif("".join(l2)=='011'):
#             l1.append('3')
#     elif("".join(l2)=='100'):
#             l1.append('4')
#     elif("".join(l2)=='101'):
#             l1.append('5')
#     elif("".join(l2)=='110'):
#             l1.append('6')
#     elif("".join(l2)=='111'):
#             l1.append('7')
# print("".join(l1))

# ************Question 50 ****************
# write a python program to convert Hexadecimal to Decimal number system.
# l1=[]
# t='1A3'
# for i in range(0,len(t)):
#     if(i==0):
#         l1.append(1)
#     else:
#         l1.append((16*l1[i-1]))
# l1.reverse()
# total=0
# for i in range(len(t)):
#         if(t[i]>='0' and t[i]<='9'):
#             total=total+(l1[i]*int(t[i]))
#         elif(t[i]=='A'):
#               total=total+(l1[i]*10)
#         elif(t[i]=='B'):
#             total=total+(l1[i]*11)
#         elif(t[i]=='C'):
#             total=total+(l1[i]*12)
#         elif(t[i]=='D'):
#             total=total+(l1[i]*13)
#         elif(t[i]=='E'):
#             total=total+(l1[i]*14)
#         elif(t[i]=='F'):
#             total=total+(l1[i]*15)
# print(total)

# **************Question 51 ****************
# write a python program to print pascal triangle upto n rows.