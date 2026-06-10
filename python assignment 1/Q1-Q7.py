# ******Question 1****
# The cover price of a book is $24.95, but bookstores get a 40 percent discount. Shipping
# costs $3 for the first copy and 75 cents for each additional copy. Calculate the total wholesale costs for 60 copies.

# bp=24.95
# print("BOOK PRICE: $",bp,sep='')
# dis=40/100 # to convert into decimal number
# dis=bp*dis
# dp=bp-dis 
# print("Discount per copy:",dis)
# print("Discount Price per copy:",dp)
# c=dp*60
# print("Cost of 60 copies: $",c,sep='')
# i=1
# while(i<=60):
#     if(i==1):
#         c=c+3
#     else:
#         c=c+0.75
#     i+=1
# print("Total wholesale cost:",c)

# ******Question 2******
# You look at the clock and see that it is currently 14.00h. You set an alarm to go off 535 
# hours later. At what time will the alarm go off? Write a program that prints the answer. 
# Hint: for the best solution, you will need the modulo operator

# ct=14
# ft= 535+ct 
# t=ft%24
# print("Time:",t,)

# ******Quetstion 3******
# Write code that can compute the surface of circle, using the variables radius and pi = 3.14159. 
# The formula, in case you do not know, is radius times radius times pi. Print the 
# outcome of your program as follows: “The surface area of a circle with radius ...is ...”

# r=int(input("Enter radius of circle:"))
# pi=3.14159
# sa=pi*r*r 
# print("The surface area of a circle with radius",r,"is",sa)

# *******Question 4*****
# Write code that classifies a given amount of money (which you store in a variable named amount),
#  specified in cents, as greater monetary units. Your code lists the monetary equivalent 
# in dollars (100 ct), quarters (25 ct), dimes (10 ct), nickels (5 ct), and pennies (1 ct).
#  Your program should report the maximum number of dollars that fit in the amount, then the 
# maximum number of quarters that fit in the remainder after you subtract the dollars, 
# then the maximum number of dimes that fit in the remainder after you subtract the dollars and 
# quarters, and so on for nickels and pennies. The result is that you express the amount as the 
# minimum number of coins needed.

# amt=int(input("Enter amount of money in cents:"))
# if(amt>=100):
#     d=amt//100
#     r=amt%100
#     q=r//25
#     r=r%25
#     di=r//10
#     r=r%10
#     n=r//5
#     r=r%5
#     p=r//1
# elif(amt>=25):
#     q=amt//25
#     r=r%25
#     di=r//10
#     r=r%10
#     n=r//5
#     r=r%5
#     p=r//1
# elif(amt>=10):
#     di=amt//10
#     r=r%10
#     n=r//5
#     r=r%5
#     p=r//1
# elif(amt>=5):
#     n=amt//5
#     r=r%5
#     p=r//1
# else:
#     p=r//1

# print(d,"Dollars,",q,"Quarters,",di,"Dime,",n,"Nickels,",p,"Pennies")

# *******Question 5*****
# Ask the user to enter three numbers. Then print the largest, the smallest,
#  and their average, rounded to 2 decimals
# x=int(input("Enter number 1:"))
# y=int(input("Enter number 2:"))
# z=int(input("Enter number 3:"))
# avg=(x+y+z)/3
# if(x>y and x>z):
#     print("Largest:",x)
#     if(y>z):
#         print("Smallest:",z)
#     else:
#         print("Smallest:",y)
# elif(y>x and y>z):
#     print("Largest:",y)
#     if(x>z):
#         print("Smallest:",z)
#     else:
#         print("Smallest:",x)
# elif(z>x and z>y):
#     print("largest:",z)
#     if(y>x):
#         print("Smallest:",x)
#     else:
#         print("Smallest:",y)
# print("Average:",avg)

# *******Question 6******
# Grades are values between zero and 10 (both zero and 10 included), and are always
#  rounded to the nearest half point. To translate grades to the American style,
#  8.5 to 10 become an “A,” 7.5 and 8 become a “B,” 6.5 and 7 become a “C,” 5.5 and 6 become a “D,”
#  and other grades become an “F.” Implement this translation, whereby you ask the user for a grade,
#  and then give the American translation. If the user enters a grade lower than zero or higher than 10,
#  just give an error message. You do not need to handle the user entering grades that do not end in .0 or .5,
#  though you may do that if you like – in that case, if the user enters such an illegal grade, give an
#  appropriate error message.

# g=float(input("Enter a grade: "))
# if(g<0 or g>10):
#     print("Error...Invalid grade")
# else:
#     if(g>=8.5 and g<=10):
#         print("Grade: A")
#     elif(g>=7.5 and g<8.5):
#         print("Grade: B")
#     elif(g>=6.5 and g<7.5):
#         print("Grade: C")
#     elif(g>=5.5 and g<6.5):
#         print("Grade: D")
#     elif(g<5.5):
#         print("Grade: F")

# ********Question 7******
# Ask the user to supply a string. Print how many different vowels there are in the string.
#  The capital version of a lower case vowel is considered to be the same vowel.
#  y is not considered a vowel. Try to print nice output (e.g., printing “There are
#  1 different vowels in the string” is ugly). Example: When the user enters the string 
# “It’s Owl Stretching Time,” the program should say that there are 3 different vowels in the string.

# ch=input("Enter a string: ")
# i=0
# if('a' in ch or 'A' in ch):
#     print("a")
#     i+=1
# if('e' in ch or 'E' in ch):
#     print("e")
#     i+=1
# if('i' in ch or 'I' in ch):
#     print("i")
#     i+=1
# if('o' in ch or 'O' in ch):
#     print("o")
#     i+=1
# if('u' in ch or 'U' in ch):
#     print("u")
#     i+=1
# print("There are",i,"different vowels in the string")

# *******or**********may be correct.
ch=input("Enter a string: ")
t=ch.upper()
c=0
for i in ['A','E','I','O','U']:
    if(i in t):
        print(i)
        c+=1
print("There are",c,"different vowels in the string")

