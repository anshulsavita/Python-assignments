'''
Question left --> 3
# *****************Question 1 **************
From the following table, write a SQL query to calculate total purchase amount of all orders. Return total purchase amount.
Sample table: orders

    - SELECT sum(purch_amt) as 'sum' FROM orders

# *****************Question 2 **************
From the following table, write a SQL query to calculate the average purchase amount of all orders. Return average purchase amount. 
Sample table: orders

    - SELECT avg(purch_amt) as 'avg' FROM orders

# ****************Question 3 *************incomplete...
From the following table, write a SQL query that counts the number of unique salespeople. Return number of salespeople.  
Sample table: orders

    - 

# **************Question 4 *****************
From the following table, write a SQL query to count the number of customers. Return number of customers.  
Sample table: customer

    - SELECT count(*) FROM  customer

# *************Question 5 **************
From the following table, write a SQL query to determine the number of customers who received at least one grade for their activity.  
Sample table: customer

    - SELECT count(grade) FROM  customer

# *************Question 6 *************
From the following table, write a SQL query to find the maximum purchase amount.  
Sample table: orders

    - SELECT max(purch_amt) FROM  orders

# ************Question 7 ***********
From the following table, write a SQL query to find the minimum purchase amount. 
Sample table: orders

    - SELECT min(purch_amt) FROM  orders

# *************Question 8 ************
From the following table, write a SQL query to find the highest grade of the customers in each city. Return city, maximum grade.  
Sample table: customer

    - SELECT city,max(grade) FROM  customer group by city

# *************Question 9 **************
From the following table, write a SQL query to find the highest purchase amount ordered by each customer. Return customer ID, maximum purchase amount. 
Sample table: orders

    - SELECT customer_id,max(purch_amt) FROM  orders group by customer_id

# ************Question 10 ****************
From the following table, write a SQL query to find the highest purchase amount ordered by each customer on a particular date. Return, order date and highest purchase amount.
Sample table: orders

    - select customer_id,ord_date,max(purch_amt) from orders group by customer_id,ord_date
    
# ************Question 11 ***********
From the following table, write a SQL query to determine the highest purchase amount made by each salesperson on '2012-08-17'. Return salesperson ID, purchase amount 
Sample table: orders

    - select salesman_id,max(purch_amt) from orders where ord_date='2012-08-17' group by salesman_id

# ************Question 12 ***********
From the following table, write a SQL query to find the highest order (purchase) amount by each customer on a particular order date. Filter the result by highest order (purchase) amount above 2000.00. Return customer id, order date and maximum purchase amount.
Sample table: orders

    - select customer_id,ord_date,max(purch_amt) from orders where purch_amt>=2000 group by ord_date

# ***********Question 13 ************
From the following table, write a SQL query to find the maximum order (purchase) amount in the range 2000 - 6000 (Begin and end values are included.) by combination of each customer and order date. Return customer id, order date and maximum purchase amount.
Sample table: orders

    - select customer_id,ord_date,max(purch_amt) from orders where purch_amt between 2000 and 6000 group by ord_date

# **************Question 14 **************
From the following table, write a SQL query to find the maximum order (purchase) amount based on the combination of each customer and order date. Filter the rows for maximum order (purchase) amount is either 2000, 3000, 5760, 6000. Return customer id, order date and maximum purchase amount.
Sample table: orders

    - select customer_id,ord_date,max(purch_amt) from orders where purch_amt in (2000,3000,5760,6000) group by ord_date

# **************Question 15 ************
From the following table, write a SQL query to determine the maximum order amount for each customer. The customer ID should be in the range 3002 and 3007(Begin and end values are included.). Return customer id and maximum purchase amount.
Sample table: orders

    - select customer_id,max(purch_amt) from orders where customer_id between 3002 and 3007 group by customer_id

# ***************Question 16 *********
From the following table, write a SQL query to find the maximum order (purchase) amount for each customer. The customer ID should be in the range 3002 and 3007(Begin and end values are included.). Filter the rows for maximum order (purchase) amount is higher than 1000. Return customer id and maximum purchase amount.
Sample table: orders

    - select customer_id,max(purch_amt) from orders where customer_id between 3002 and 3007 and purch_amt>1000 group by customer_id

# ****************Question 17 ************
From the following table, write a SQL query to determine the maximum order (purchase) amount generated by each salesperson. Filter the rows for the salesperson ID is in the range 5003 and 5008 (Begin and end values are included.). Return salesperson id and maximum purchase amount.
Sample table: orders

    - select salesman_id,max(purch_amt) from orders where salesman_id between 5003 and 5008 group by salesman_id

# ****************Question 18 ***********
From the following table, write a SQL query to count all the orders generated on '2012-08-17'. Return number of orders.
Sample table: orders

    - select count(*) from orders where ord_date='2012-08-17'

# ****************Question 19 *****************
From the following table, write a SQL query to count the number of salespeople in a city. Return number of salespeople.
Sample table: salesman

    - select count(*) from salesman 

# ******************Question 20 ************
From the following table, write a SQL query to count the number of orders based on the combination of each order date and salesperson. Return order date, salesperson id.
Sample table: orders

    - select ord_date,salesman_id,count(*) from orders group by ord_date,salesman_id

# *****************Question 21 ***************
From the following table, write a SQL query to calculate the average product price. Return average product price.
Sample table: item_mast

    - select avg(pro_price) from item_mast

# *****************Question 22 ***************
From the following table, write a SQL query to count the number of products whose price are higher than or equal to 350. Return number of products.
Sample table: item_mast

    - select count(*) from item_mast where pro_price>=350

# ****************Question 23 ***************
From the following table, write a SQL query to compute the average price for unique companies. Return average price and company id.
Sample table: item_mast

    - select avg(pro_price),pro_com from item_mast group by pro_com

# ***************Question 24 *****************
From the following table, write a SQL query to compute the sum of the allotment amount of all departments. Return sum of the allotment amount.
Sample table: emp_department

    - select sum(Dpt_Allotment) from emp_department

# ***************Question 25 *****************
From the following table, write a SQL query to count the number of employees in each department. Return department code and number of employees.
Sample table: emp_details

    - select emp_dept,count(*) from emp_details group by Emp_dept

'''