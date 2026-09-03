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
# for i in range(len(x),0,-1):
    