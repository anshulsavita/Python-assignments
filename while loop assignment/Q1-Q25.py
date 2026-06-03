# ****Question 4
# write a program to print all even numbers between 1 to 100.
# t=1
# while(t<=100):
#     if(t%2==0):
#         print(t,end=",")
#     t+=1

# ****Question 5
# write a program to print all odd numbers between 1 to 100.
# t=1
# while(t<=100):
#     if(t%2!=0):
#         print(t,end=",")
#     t+=1

# *****Question 6
# n=int(input("Enter number:"))
# i=1
# s=0
# while(i<=n):
#     if(i%2==0):
#         s=s+i
#     i+=1
# print("sum:",s)

# ****Question 8
# n=int(input("Enter number:"))
# i=1
# while(i<=10):
#     t=n*i
#     print(t,end=",")
#     i+=1

# ****Question 9
# n=int(input("Enter number:"))
# i=1
# s=0
# while(i<=n):
#     s=s+i
#     i+=1
# print("sum",s)

# ****Question 10
# n=int(input("Enter number:"))
# r=n%10
# while(n>10):
#     n=n//10
# print("Last num:",r,"First num:",n)

# ****Question 11
# n=int(input("Enter number:"))
# c=0
# while(n):
#     n=n//10
#     c+=1
# print(c)

# ****Question 12
# n=int(input("Enter number:"))
# s=0
# while(n):
#     r=n%10
#     s=s+r
#     n=n//10
# print(s)

# ****Question 13****
# n=int(input("Enter number:"))
# p=1
# while(n):
#     r=n%10
#     p=p*r
#     n=n//10
# print(p)

# ****Question 14***incomplete
# n=int(input("Enter number:"))
# p=1000
# r=n%10
# while(n):
#     r=n%10
#     s=s+(p*r)
#     n=n//10
#     p=p//10
# print(s)

# ****Question 15
# n=int(input("Enter number:"))
# r=n%10
# while(n>10):
#     n=n//10
# s=r+n
# print(s)

# ****Questipn 16
# n=int(input("Enter number:"))
# s=0
# while(n):
#     r=n%10
#     s=s*10+r
#     n=n//10
# print(s)
 
 # ****Questipn 17
# n=int(input("Enter number:"))
# t=n
# s=0
# while(n):
#     r=n%10
#     s=s*10+r
#     n=n//10
# if(t==s):
#     print("its palindrom number:")
# else:
#     print("its not..")

# ****Question 21****
# n1=int(input("Enter number:"))
# n2=int(input("Enter power:"))
# i=1
# t=n1
# while(i<n2):
#     n1=n1*t
#     i+=1
# print(n1)

# Question 22
# n=int(input("Enter number:"))
# i=1
# while(i<=n):
#     if(n%i==0):
#         print(i)
#     i+=1

# Question 23
# n=int(input("Enter number:"))
# p=1
# while(n):
#     p=p*n
#     n-=1
# print(p)

# Question 24
# n=int(input("Enter number:"))
# n2=int(input("Enter number:"))
# i=1
# hcf=1
# while(i<=n and i<=n2):
#     if(n%i==0 and n2%i==0):
#         hcf=i
#     i+=1
# print(hcf)

# ******Question 25
n=int(input("Enter number:"))
n2=int(input("Enter number:"))
i=1
hcf=1
while(i<=n and i<=n2):
    if(n%i==0 and n2%i==0):
        hcf=i
    i+=1
lcm=(n*n2)//hcf
print(lcm)
