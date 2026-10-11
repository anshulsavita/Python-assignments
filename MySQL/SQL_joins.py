'''
incomplte --> 14th
need to check --> 25th

# **************Question 1 ***************
From the following tables write a SQL query to find the salesperson and customer who reside in the same city. Return Salesman, cust_name and city.
Sample table: salesman
Sample table: customer

    - select salesman.name,customer.cust_name,salesman.city from salesman,customer where salesman.city=customer.city

# *************Question 2 ************
From the following tables write a SQL query to find those orders where the order amount exists between 500 and 2000. Return ord_no, purch_amt, cust_name, city.
Sample table: customer
Sample table: orders

    - select orders.ord_no,orders.purch_amt,customer.cust_name,customer.city from orders,customer
    where orders.customer_id=customer.customer_id and orders.purch_amt between 500 and 2000

# *************Question 3 ***************
From the following tables write a SQL query to find the salesperson(s) and the customer(s) he represents. Return Customer Name, city, Salesman, commission.
Sample table: customer
Sample table: salesman

    - select customer.cust_name,customer.city,salesman.name,salesman.commission from customer,salesman
    where customer.salesman_id=salesman.salesman_id

# **************Question 4 ****************
From the following tables write a SQL query to find salespeople who received commissions of more than 12 percent from the company. Return Customer Name, customer city, Salesman, commission.  
Sample table: customer
Sample table: salesman

    - select customer.cust_name,customer.city,salesman.name,salesman.commission from customer,salesman
    where customer.salesman_id=salesman.salesman_id and salesman.commission>0.12

# *****************Question 5 ***************
From the following tables write a SQL query to locate those salespeople who do not live in the same city where their customers live and have received a commission of more than 12% from the company. Return Customer Name, customer city, Salesman, salesman city, commission.  
Sample table: customer
Sample table: salesman

    - select customer.cust_name,customer.city,salesman.name,salesman.commission from customer,salesman
    where customer.salesman_id=salesman.salesman_id and customer.city != salesman.city and salesman.commission>0.12 

# *******************Question 6 ****************
From the following tables write a SQL query to find the details of an order. Return ord_no, ord_date, purch_amt, Customer Name, grade, Salesman, commission.  
Sample table: orders
Sample table: customer
Sample table: salesman

    - select orders.ord_no,orders.ord_date,orders.purch_amt,customer.cust_name,customer.grade,salesman.name,salesman.commission from orders,customer,salesman
    where orders.customer_id=customer.customer_id and orders.salesman_id=salesman.salesman_id
    
# ******************Question 7 ****************
Write a SQL statement to join the tables salesman, customer and orders so that the same column of each table appears once and only the relational rows are returned. 
Sample table: orders
Sample table : salesman

    - select orders.ord_no,orders.purch_amt,orders.ord_date,customer.customer_id,customer.cust_name,customer.city,customer.grade,salesman.name,salesman.commission
    from orders,customer,salesman where orders.customer_id=customer.customer_id and orders.salesman_id=salesman.salesman_id

# ******************Question 8 ***************
From the following tables write a SQL query to display the customer name, customer city, grade, salesman, salesman city. The results should be sorted by ascending customer_id.  
Sample table: customer
Sample table: salesman

    - select customer.cust_name,customer.city,customer.grade,salesman.name,salesman.city
    from customer,salesman where salesman.salesman_id=customer.salesman_id order by customer.customer_id

# *****************Question 9 ***************
From the following tables write a SQL query to find those customers with a grade less than 300. Return cust_name, customer city, grade, Salesman, salesmancity. The result should be ordered by ascending customer_id. 
Sample table: customer
Sample table: salesman

    - select customer.cust_name,customer.city,customer.grade,salesman.name,salesman.city from customer,salesman
where customer.salesman_id=salesman.salesman_id and customer.grade<300 order by customer.customer_id

# ****************Question 10 **************
Write a SQL statement to make a report with customer name, city, order number, order date, and order amount in ascending order according to the order date to determine whether any of the existing customers have placed an order or not.
Sample table: orders
Sample table: customer

    - select customer.cust_name,customer.city,orders.ord_no,orders.ord_date,orders.purch_amt from orders,customer
    where orders.customer_id=customer.customer_id order by orders.ord_date

# **************Question 11 ***************
SQL statement to generate a report with customer name, city, order number, order date, order amount, salesperson name, and commission to determine if any of the existing customers have not placed orders or if they have placed orders through their salesman or by themselves.
Sample table: customer
Sample table: orders
Sample table: salesman

    - select customer.cust_name,customer.city, orders.ord_no,orders.ord_date,orders.purch_amt,salesman.name,salesman.commission from customer
left join orders on orders.customer_id=customer.customer_id
left join salesman on customer.salesman_id = salesman.salesman_id
    
# **************Question 12 **************
Write a SQL statement to generate a list in ascending order of salespersons who work either for one or more customers or have not yet joined any of the customers.
Sample table: customer
Sample table: salesman

    - select * from salesman
left join customer on customer.salesman_id=salesman.salesman_id
order by salesman.salesman_id 


# *************Question 13 ****************
From the following tables write a SQL query to list all salespersons along with customer name, city, grade, order number, date, and amount. Condition for selecting list of salesmen : 1. Salesmen who works for one or more customer or, 2. Salesmen who not yet join under any customer, Condition for selecting list of customer : 3. placed one or more orders, or 4. no order placed to their salesman.
Sample table: customer
Sample table: salesman
Sample table: orders

    - select salesman.name,cust_name,customer.city,grade,ord_no,ord_date,purch_amt from salesman
left join customer on customer.salesman_id=salesman.salesman_id
left join orders on orders.customer_id=customer.customer_id and orders.salesman_id=salesman.salesman_id

# *************Question 14 *****************incomplete
Write a SQL statement to make a list for the salesmen who either work for one or more customers or yet to join any of the customer. The customer may have placed, either one or more orders on or above order amount 2000 and must have a grade, or he may not have placed any order to the associated supplier.
Sample table: customer
Sample table: salesman
Sample table: orders

    - select salesman.*,customer.* from salesman
left join customer on salesman.salesman_id=customer.salesman_id 
left join orders on customer.customer_id=orders.customer_id and orders.salesman_id=salesman.salesman_id 
and orders.purch_amt >= 2000

# *************Question 15 ****************
For those customers from the existing list who put one or more orders, or which orders have been placed by the customer who is not on the list, create a report containing the customer name, city, order number, order date, and purchase amount
Sample table: customer
Sample table: orders

    - select customer.cust_name,customer.city,orders.ord_no,orders.ord_date,orders.purch_amt from orders
left join customer on customer.customer_id=orders.customer_id

# *************Question 16 **************
Write a SQL statement to generate a report with the customer name, city, order no. order date, purchase amount for only those customers on the list who must have a grade and placed one or more orders or which order(s) have been placed by the customer who neither is on the list nor has a grade.
Sample table: customer
Sample table: orders

    - select customer.cust_name,customer.city,orders.ord_no,orders.ord_date,orders.purch_amt from customer
left join orders on customer.customer_id=orders.customer_id
where customer.grade is not null or customer.customer_id is null

# ****************Question 17 *************
Write a SQL query to combine each row of the salesman table with each row of the customer table.
Sample table: salesman
Sample table: customer

    - select * from salesman,customer

# *************Question 18 *****************Check what is the difference between Q17 and 18
Write a SQL statement to create a Cartesian product between salesperson and customer, i.e. each salesperson will appear for all customers and vice versa for that salesperson who belongs to that city.
Sample table: salesman
Sample table: customer

    - select * from salesman,customer

# ***************Question 19 *************
Write a SQL statement to create a Cartesian product between salesperson and customer, i.e. each salesperson will appear for every customer and vice versa for those salesmen who belong to a city and customers who require a grade.
Sample table: salesman
Sample table: customer

    - select * from salesman,customer where salesman.city is not null and customer.grade is not null

# *****************Question 20 ************
Write a SQL statement to make a Cartesian product between salesman and customer i.e. each salesman will appear for all customers and vice versa for those salesmen who must belong to a city which is not the same as his customer and the customers should have their own grade.
Sample table: salesman
Sample table: customer

    - select * from salesman,customer where customer.grade is not null and salesman.city != customer.city 

# ***************Question 21 **************
From the following tables write a SQL query to select all rows from both participating tables as long as there is a match between pro_com and com_id.
Sample table: company_mast
Sample table: item_mast

    - select * from company_mast,item_mast where company_mast.COM_ID=item_mast.PRO_COM

# **************Question 22 ************
Write a SQL query to display the item name, price, and company name of all the products.
Sample table: company_mast
Sample table: item_mast

    - select item_mast.PRO_NAME,company_mast.COM_NAME,item_mast.PRO_PRICE from company_mast,item_mast where company_mast.COM_ID=item_mast.PRO_COM

# **************Question 23 ***********
From the following tables write a SQL query to calculate the average price of items of each company. Return average value and company name.
Sample table: company_mast
Sample table: item_mast

    - select company_mast.COM_NAME, avg(item_mast.PRO_PRICE) from company_mast,item_mast where company_mast.COM_ID=item_mast.PRO_COM group by company_mast.COM_ID

# *************Question 24 *************
From the following tables write a SQL query to calculate and find the average price of items of each company higher than or equal to Rs. 350. Return average value and company name.
Sample table: company_mast
Sample table: item_mast

    - select company_mast.COM_NAME, avg(item_mast.PRO_PRICE) as 'average_price' from company_mast,item_mast where company_mast.COM_ID=item_mast.PRO_COM group by company_mast.COM_ID having average_price>=350 

# **********Question 25 ***************check
From the following tables write a SQL query to find the most expensive product of each company. Return pro_name, pro_price and com_name.
Sample table: company_mast
Sample table: item_mast

    - select item_mast.PRO_NAME,max(item_mast.PRO_PRICE) as 'Maximum',company_mast.COM_NAME from company_mast,item_mast where company_mast.COM_ID=item_mast.PRO_COM group by company_mast.COM_ID  

# *************Question 26 **************
From the following tables write a SQL query to display all the data of employees including their department.
Sample table: emp_department
Sample table: emp_details

    - select * from emp_department,emp_details where emp_department.DPT_CODE=emp_details.EMP_DEPT

# *************Question 27 ***********
From the following tables write a SQL query to display the first and last names of each employee, as well as the department name and sanction amount.
Sample table: emp_department
Sample table: emp_details

    - select emp_details.EMP_FNAME,emp_details.EMP_LNAME,emp_department.DPT_NAME,emp_department.DPT_ALLOTMENT from emp_department,emp_details where emp_department.DPT_CODE=emp_details.EMP_DEPT

# *************Question 28 ***********
From the following tables write a SQL query to find the departments with budgets more than Rs. 50000 and display the first name and last name of employees.
Sample table: emp_department
Sample table: emp_details

    - select emp_details.EMP_FNAME,emp_details.EMP_LNAME,emp_department.DPT_NAME from emp_department,emp_details where emp_department.DPT_CODE=emp_details.EMP_DEPT and emp_department.DPT_ALLOTMENT>50000

# *************Question 29 **************
From the following tables write a SQL query to find the names of departments where more than two employees are employed. Return dpt_name.
Sample table: emp_department
Sample table: emp_details

    - select emp_department.DPT_NAME from emp_department,emp_details where emp_department.DPT_CODE=emp_details.EMP_DEPT group by emp_department.DPT_CODE having count(emp_details.EMP_IDNO)>2

'''