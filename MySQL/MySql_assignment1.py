'''
# *************Question 1 ************ 
Write a SQL statement that displays all the information about all salespeople.

create table salesman(salesman_id int primary key,name varchar(40) not null,city varchar(40) not null,commission varchar(40) )
insert into salesman value(5001,'James Hoog','New York','0.15')
insert into salesman value(5002,'Nail Knite','Paris','0.13')
insert into salesman value(5003,'Pit Alex','London','0.11')
insert into salesman value(5004,'Mc Lyon','Paris','0.14')
insert into salesman value(5005,'Paul Adam','Rome','0.13')
insert into salesman value(5006,'Lauson Hen','San Jose','0.12')
select * from salesman

# ************Question 2 **************
Write a SQL statement to display a string "This is SQL Exercise, Practice and Solution".

    - select 'This is SQL Exercise, Practice and Solution' as string;

# ************Question 3 **************
Write a SQL query to display three numbers in three columns. 

    - select 3 as number1,2 as number2,1 as number3;

# *************Question 4 *************
Write a SQL query to display the sum of two numbers 10 and 15 from the RDBMS server.

# *************Question 5 ************
Write an SQL query to display the result of an arithmetic expression. 

    - select 3 + 2 as sum

# *************Question 6 *************
Write a SQL statement to display specific columns such as names and commissions for all salespeople.  
Sample table: salesman

    - select name,commission from salesman

# *************Question 7 ***********
Write a query to display the columns in a specific order, such as order date, salesman ID, order number, and purchase amount for all orders.  
Sample table: orders

    - select ord_date,salesman_id,ord_no,purch_amt from orders

# *************Question 8 ************
From the following table, write a SQL query to identify the unique salespeople ID. Return salesman_id. 

    - select salesman_id from orders group by salesman_id

# ************Question 9 **************
From the following table, write a SQL query to locate salespeople who live in the city of 'Paris'. Return salesperson's name, city.

    - select name from salesman where city = 'paris'

# ************Question 10 *************
From the following table, write a SQL query to find customers whose grade is 200. Return customer_id, cust_name, city, grade, salesman_id.  
Sample table: customer

    - select * from customer where grade=200

# **************Question 11 **************
From the following table, write a SQL query to find orders that are delivered by a salesperson with ID. 5001. Return ord_no, ord_date, purch_amt.    
    
    - select ord_no,ord_date,purch_amt from orders where salesman_id=5001

# **************Question 12 **************
From the following table, write a SQL query to find the Nobel Prize winner(s) for the year 1970. Return year, subject and winner. 

    - select YEAR,SUBJECT,WINNER from nobel_win where YEAR=1970

#*************Question 13 ***************
From the following table, write a SQL query to find the Nobel Prize winner in ‘Literature’ for 1971. Return winner

    - select winner from nobel_win where Year=1971 and Subject='Literature'

# ************Question 14 ***************
From the following table, write a SQL query to locate the Nobel Prize winner ‘Dennis Gabor'. Return year, subject. 
Sample table: nobel_win

    - select Year,Subject from nobel_win where winner='Dennis Gabor'

# *************Question 15 *************
From the following table, write a SQL query to find the Nobel Prize winners in the field of ‘Physics’ since 1950. Return winner. 
Sample table: nobel_win

    - select winner from nobel_win where Subject='Physics' and year>=1950

# *************Question 16 *************
From the following table, write a SQL query to find the Nobel Prize winners in ‘Chemistry’ between the years 1965 and 1975. Begin and end values are included. Return year, subject, winner, and country.  
Sample table: nobel_win

    - select Year,Subject,winner,Country from nobel_win where Subject='Chemistry' and Year between 1965 and 1975

# *************Question 17 *************
Write a SQL query to display all details of the Prime Ministerial winners after 1972 of Menachem Begin and Yitzhak Rabin.

    - select * from nobel_win where Category='Prime Minister' and Year>1972

# ***********Question 18 ***************
From the following table, write a SQL query to retrieve the details of the winners whose first names match with the string ‘Louis’. Return year, subject, winner, country, and category.  
Sample table: nobel_win

    - select * from nobel_win where winner like 'Louis%'  

# ************Question 19 *************
From the following table, write a SQL query that combines the winners in Physics, 1970 and in Economics, 1971. Return year, subject, winner, country, and category. 
Sample table: nobel_win

    - select Year,Subject,Winner,country,category from nobel_win where Subject ='Physics' and year =1970 or Subject ='Economics' and year=1971

# *************Question 20 ************
From the following table, write a SQL query to find the Nobel Prize winners in 1970 excluding the subjects of Physiology and Economics. Return year, subject, winner, country, and category. 
Sample table: nobel_win

    - select Year,Subject,Winner,country,category from nobel_win where Year =1970 and Subject !='Physiology' and Subject !='Economics'

# ***********Question 21 *************
From the following table, write a SQL query to combine the winners in 'Physiology' before 1971 and winners in 'Peace' on or after 1974. Return year, subject, winner, country, and category. 
Sample table: nobel_win

    - select Year,Subject,Winner,country,category from nobel_win where Subject ='Physiology' and year <1971 or Subject ='Peace' and year>=1974

# ************Question 22 ************
From the following table, write a SQL query to find the details of the Nobel Prize winner 'Johannes Georg Bednorz'. Return year, subject, winner, country, and category.
Sample table: nobel_win

    - select Year,Subject,Winner,country,category from nobel_win where winner='Johannes Georg Bednorz'

# **************Question 23 ************
From the following table, write a SQL query to find Nobel Prize winners for the subject that does not begin with the letter 'P'. Return year, subject, winner, country, and category. Order the result by year, descending and winner in ascending.  
Sample table: nobel_win

    - select Year,Subject,Winner,country,category from nobel_win where Subject not like 'P%' order by year desc,winner

# **************Question 24 *************
From the following table, write a SQL query to find the details of 1970 Nobel Prize winners. Order the results by subject, ascending except for 'Chemistry' and ‘Economics’ which will come at the end of the result set. Return year, subject, winner, country, and category.  
Sample table: nobel_win

    - 
















'''