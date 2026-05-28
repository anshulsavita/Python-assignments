# ****Question 1****
# Write a program to find maximum between two numbers.
# x=int(input("Enter first number:"))
# y=int(input("Enter second number:"))
# if(x>y):
#     print(x,"is grater then",y)
# else:
#     print(y,"Is grater then",x)

# *****Question 2*****
# Write a program to find Maximum between three numbers.
# x=int(input("Enter first number:"))
# y=int(input("Enter second number:"))
# z=int(input("Enter third number:"))

# if(x>y and x>z):
#     print(x,"is grater then",y,"and",z)
# elif(y>x and y>z):
#     print(y,"Is grater then",x,"and",z)
# else:
#     print(z,"is grater then",x,"and",y)

# ****Question 3****
# Write a program to check whether a number is even or odd.
# x=int(input("Enter number:"))
# if(x%2==0):
#     print("It is a even number.")
# else:
#     print("It is a odd number.")

# ****Question 4****
# Write a c program to check whether a year is leap year or not.
# x=int(input("Enter Year:"))
# if(x%4==0 or x%400==0):
#     print("It is a leap year")
# else:
#     print("It is not a leap year....")

# ****Question 5****
# x=int(input("Enter number:"))
# if(x>0):
#     print("Its positive...")
# elif(x<0):
#     print("Its negative...")
# else:
#     print("Its Zero...")

# ****Question 6****
# x=int(input("Enter number:"))
# if(x%5==0 and x%11==0):
#     print("Yes,it is divisible by 5 and 11.")
# else:
#     print("not divisible by 5 and 11.")

# ****Question 7****
# x=int(input("Enter amount:"))
# if(x>=1000):
#     th=x//1000
#     r=x%1000
#     f=r//500
#     r=r%500
#     h=r//100
#     r=r%100
#     ft=r//50
#     r=r%50
#     ten=r//10
# elif(x>=500 and x<1000):
#     f=x//500
#     r=x%500
#     h=r//100
#     r=r%100
#     ft=r//50
#     r=r%50
#     ten=r//10
# elif(x>=100 and x<500):
#     h=x//100
#     r=x%100
#     ft=r//50
#     r=r%50
#     ten=r//10
# elif(x>=50 and x<100):
#     ft=x//50
#     r=x%50
#     ten=r//10
# elif(x>=50 and x<100):
#     ten=r//10

# print("1000:",th)
# print("500:",f)
# print("100:",h)
# print("50:",ft)
# print("10:",ten)

# ****Question 8****
# Write a program to check whether a character is alphabet or not.
# x=(input("Enter a character:"))
# if((x>='A' and x<='Z') or (x>='a' and x<='z')):
#     print("It is a alphabet...")
# else:
#     print("its not a aplhabet")

# ****Question 9****
# Write a program to input any alphabet and check whether it is vowel or consonant.
# x=(input("Enter a character:"))
# if((x>='A' and x<='Z') or (x>='a' and x<='z')):
#     if(x=='a' or x=='e' or x=='i' or x=='o' or x=='u' or x=='A' or x=='E' or x=="I" or x=='O' or x=='U'):
#         print("Its a vowel...")
#     else:
#         print("Its consonent...")
# else:
#     print("its not a aplhabet")

# ****Question 10****
# Write a program to input any character and check whether it is alphabet,digit,space or special character.
# x=(input("Enter a character:"))
# if((x>='A' and x<='Z') or (x>='a' and x<='z')):
#     print("It is a alphabet...")
# elif(x>='0' and x<='9'):
#     print("its a digit...")
# elif(x==' '):
#     print("its space...")
# else:
#     print("it is a special character...")

# ****Question 11****
# Write a program to check whether a character is uppercase or lowercase alphabet.
# x=(input("Enter a character:"))
# if(x>='a' and x<='z'):
#     print("Its a lowercase alphabet..")
# elif(x>='A' and x<='Z'):
#     print("Its a uppercase alphabet...")
# else:
#     print("Its not a alphabet...")

# ****Question 12****
# Write a program to input week number and print week day.
# x=int(input("Enter a character:"))
# if(x==1):
#     print("Monday")
# elif(x==2):
#     print("Tuesday")
# elif(x==3):
#     print("Wednesday")
# elif(x==4):
#     print("Thrusday")
# elif(x==5):
#     print("Friday")
# elif(x==6):
#     print("Saturday")
# elif(x==7):
#     print("Sunday")
# else:
#     print("incorrect number...")

# ****Question 13****
# Write a program to input month number and print number of days in that month.
x=int(input("Enter month number:"))
if(x==1):
    print("jan has 31 days.")
elif(x==2):
    print("Feb has 28 days.")
elif(x==3):
    print("March has 31 days")
elif(x==4):
    print("April has 30 days")
elif(x==5):
    print("May has 31 days")
elif(x==6):
    print("Jun has 30 days")
elif(x==7):
    print("July has 31 days")
elif(x==8):
    print("August has 31 days")
elif(x==9):
    print("Sep has 30 days.")
elif(x==10):
    print("Oct has 31 days.")
elif(x==11):
    print("Nov has 30 days.")
elif(x==12):
    print("Dec has 31 days")
else:
    print("incorrect number")
