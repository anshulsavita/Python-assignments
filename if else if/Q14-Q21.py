# *****Question 14*****
# Write a program to input angles of a triangle and check whether triangle is valid or not.
# a=int(input("Enter angle a: "))
# b=int(input("Enter angle b: "))
# c=int(input("Enter angle c: "))
# if((a+b)>c and (a+c)>b and (b+c)>a):
#     print("It is a valid triangle.")
# else:
#     print("its not a valid triangle")

# *****Question 15*****
# Write a program to input sides of a triangle and check whether triangle is valid or not.
# a=int(input("Enter side a: "))
# b=int(input("Enter side b: "))
# c=int(input("Enter side c: "))
# if((a+b+c)==180):
#     print("It is a valid triangle.")
# else:
#     print("its not a valid triangle")

# ****Question 16****
# Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.
# Write a program to input sides of a triangle and check whether triangle is valid or not.
# a=int(input("Enter side a: "))
# b=int(input("Enter side b: "))
# c=int(input("Enter side c: "))
# if(a==b and b==c):
#     print("It is a Equilateral triangle.")
# elif(a==b or b==c or a==c):
#     print("it is a Isosceles triangle")
# elif(a!=b and b!=c):
#     print("It is a Scalene triangle")
# else:
#     print("Error....")

# ****Question 17*****
# Write a program to find all roots of a quadratic equation.
# from math import sqrt
# a=int(input("Enter value of a: "))
# b=int(input("Enter value of b: "))
# c=int(input("Enter value of c: "))
# d=(b*b)-4*a*c
# if(d>0):
#     r1=(-b+sqrt(d))/(2*a)
#     r2=(-b-sqrt(d))/(2*a)
#     print("Two real roots:",r1,r2)
# elif(d==0):
#     r=-b/(2*a)
#     print("Equal roots:",r)
# else:
#     r=-b/(2*a)
#     i=sqrt(-d)/(2*a)  #imaginary root
#     print("Complex roots:")
#     print(r,"+",i,"i")
#     print(r,"-",i,"i")

# ****Question 18****
# x=int(input("Enter Cost price:"))
# y=int(input("Enter selling price:"))
# if(x>y):
#     l=x-y
#     print("Loss:",l)
# else:
#     p=y-x
#     print("Profit:",p)

# ****Question 19****
# Write a program to input marks of five subjects physics,chemistry,biology,
# mathematics and computer. calculate percentage and grade according to following.
# p=int(input("Enter Physics marks:"))
# c=int(input("Enter Chemistry marks:"))
# m=int(input("Enter Maths marks:"))
# b=int(input("Enter Biology marks:"))
# com=int(input("Enter computer marks:"))

# t=p+c+m+b+com
# per=(t/500)*100
# print("Percentage:",per,"%")
# if(per>=90):
#     print("Grade: A")
# elif(per>=80):
#     print("Grade: B")
# elif(per>=70):
    # print("Grade: C")
# elif(per>=60):
#     print("Grade: D")
# elif(per>=40):
#     print("Grade: E")
# else:
#     print("Grade: F")

# ****Question 20****
# Write a program to input basic salary of an employee and caluculate its Gross salary according to following.
# salary=float(input("Enter salary:"))
# if(salary>=30000):
#     da=salary*95/100
#     hra=salary*30/100
#     gs=salary+da+hra
#     print("Da:",da,"Hra:",hra,"Gross salary",gs)

# elif(salary>= 20000and salary<=199999):
#     da=salary*90/100
#     hra=salary*25/100
#     gs=salary+da+hra
#     print("Da:",da,"Hra:",hra,"Gross salary",gs)

# elif(salary>=10000 and salary<=99999):
#     da=salary*95/100
#     hra=salary*20/100
#     gs=salary+da+hra
#     print("Da:",da,"Hra:",hra,"Gross salary",gs)

# else:
#     print("Invalid salary....")

# ****Question 21****
# Write a c program to input electricity unit charges and calculate total electricity bill according to the given condition.
i=float(input("Enter electricity unit:"))
if(i>=0 and i<=50):
    i=i*0.50
    print("Unit charge:",i)
elif(i>50 and i<=150):
    i=i*0.75
    print("Unit chaarge:",i)
elif(i>150 and i<=250):
    i=i*1.20
    print("Unit chaarge:",i)
else:
    i=i*1.50
    print("Unit chaarge:",i)

e=i*20/100
e=e+i
print("total charges:",e)