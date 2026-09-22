'''
# ***************Question 1 **********
From the following table, write a SQL query to find the details of those salespeople who come from the 'Paris' City or 'Rome' City. Return salesman_id, name, city, commission.
Sample table: salesman

    - SELECT * FROM salesman where city='Paris' or city='Rome'

# ***************Question 2 ***********
From the following table, write a SQL query to find the details of the salespeople who come from either 'Paris' or 'Rome'. Return salesman_id, name, city, commission. 
Sample table: salesman

    - SELECT * FROM salesman where city='Paris' or city='Rome'

# **************Question 3 ***************
From the following table, write a SQL query to find the details of those salespeople who live in cities other than Paris and Rome. Return salesman_id, name, city, commission.  
Sample table: salesman

    - SELECT * FROM salesman where not (city='Paris' or city='Rome')

# ***************Question 4 **************
From the following table, write a SQL query to retrieve the details of all customers whose ID belongs to any of the values 3007, 3008 or 3009. Return customer_id, cust_name, city, grade, and salesman_id.  
Sample table: customer

    - SELECT * FROM customer where customer_id in (3007,3008,3009)

# ****************Question 5 ***************
From the following table, write a SQL query to find salespeople who receive commissions between 0.12 and 0.14 (begin and end values are included). Return salesman_id, name, city, and commission.  
Sample table: salesman

    - SELECT * FROM salesman where commission between 0.12 and 0.14

# **************Question 6 **************
From the following table, write a SQL query to select orders between 500 and 4000 (begin and end values are included). Exclude orders amount 948.50 and 1983.43. Return ord_no, purch_amt, ord_date, customer_id, and salesman_id. 
Sample table: orders

    - SELECT * FROM orders where ((purch_amt between 500 and 4000) and purch_amt not in (948.50,1983.43))

# *************Question 7 **************
From the following table, write a SQL query to retrieve the details of the salespeople whose names begin with any letter between 'A' and 'L' (not inclusive). Return salesman_id, name, city, commission. 
Sample table: salesman

    - SELECT * FROM salesman where name between 'B%' and 'k%'

# **************Question 8 **************
From the following table, write a SQL query to find the details of all salespeople except those whose names begin with any letter between 'A' and 'M'. Return salesman_id, name, city, commission.  
Sample table: salesman

    - SELECT * FROM salesman where not name between 'A%' and 'M%'

# ***************Question 9 ***************
From the following table, write a SQL query to retrieve the details of the customers whose names begins with the letter 'B'. Return customer_id, cust_name, city, grade, salesman_id.. 
Sample table: customer

    - SELECT * FROM customer where cust_name like 'B%'

# ***************Question 10 ****************
From the following table, write a SQL query to find the details of the customers whose names end with the letter 'n'. Return customer_id, cust_name, city, grade, salesman_id.
Sample table: customer

    - SELECT * FROM customer where cust_name like '%n'

# ****************Question 11 ***************
From the following table, write a SQL query to find the details of those salespeople whose names begin with ‘N’ and the fourth character is 'l'. Rests may be any character. Return salesman_id, name, city, commission. 
Sample table : salesman

    - SELECT * FROM salesman where name like 'n__l%'

# *****************Question 12 ***************
From the following table, write a SQL query to find those rows where col1 contains the escape character underscore ( _ ). Return col1.
Sample table: testtable

    - SELECT * FROM testtable where col1 like '%\_%'

# ****************Question 13 **************
From the following table, write a SQL query to identify those rows where col1 does not contain the escape character underscore ( _ ). Return col1.
Sample table: testtable

    - SELECT * FROM testtable where col1 not like '%\_%'

# ***************Question 14 **************
From the following table, write a SQL query to find rows in which col1 contains the forward slash character ( / ). Return col1.
Sample table: testtable

    - SELECT * FROM testtable where col1 like '%/%'

# **************Question 15 **************
From the following table, write a SQL query to identify those rows where col1 does not contain the forward slash character ( / ). Return col1.
Sample table: testtable

    - SELECT * FROM testtable where col1 not like '%/%'

# ****************Question 16 ************
From the following table, write a SQL query to find those rows where col1 contains the string ( _/ ). Return col1.
Sample table: testtable

    - SELECT * FROM testtable where col1 like '%\_/%'

# ****************Question 17 *************
From the following table, write a SQL query to find those rows where col1 does not contain the string ( _/ ). Return col1.
Sample table: testtable

    - SELECT * FROM testtable where col1 not like '%\_/%'

# *****************Question 18 **************
From the following table, write a SQL query to find those rows where col1 contains the character percent ( % ). Return col1.
Sample table: testtable

    - SELECT * FROM testtable where col1 like '%\%%'

# *****************Question 19 ***************
From the following table, write a SQL query to find those rows where col1 does not contain the character percent ( % ). Return col1.
Sample table: testtable

    - SELECT * FROM testtable where col1 not like '%\%%'

# ****************Question 20 ***************
From the following table, write a SQL query to find all those customers who does not have any grade. Return customer_id, cust_name, city, grade, salesman_id.
Sample table: customer

    - SELECT * FROM customer where grade is null

# ****************Question 21 ***************
From the following table, write a SQL query to locate all customers with a grade value. Return customer_id, cust_name,city, grade, salesman_id.
Sample table: customer

    - SELECT * FROM customer where grade is not null

# ****************Question 22 ***************
From the following table, write a SQL query to locate the employees whose last name begins with the letter 'D'. Return emp_idno, emp_fname, emp_lname and emp_dept.  
Sample table: emp_details

    - SELECT * FROM emp_details where emp_lname like 'D%'

'''