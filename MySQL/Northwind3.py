'''
# ************Question 1***********
How many current products cost less than $20?

    - select count(*) from products where products.UnitPrice<20

# ***********Question 2 ***********
which products is the expensive?

    - select ProductName, UnitPrice from products
where UnitPrice = (select max(UnitPrice) from products)

# *********Question 3 ***********
what is the average unit price for our products?

    - select avg(unitprice) from products

# ***********Question 4 *********
how many products are above the average unit price?

    - select count(*) from products where UnitPrice>(select avg(unitprice) from products)

# ***********Question 5 **********
how many products cost between $15 and $25?

    - select count(*) from products where Unitprice between 15 and 25

# ************Question 6 ************
what is the average number of products(not qty) per order?

    - select avg(product_count) as average from (select count(ProductID) as product_count from orders GROUP BY OrderID) as order_counts

# ************Question 7 ************
what is the order value in $ of open orders? (not shipped yet)

    - SELECT sum(orders.Total_Amount) from orders where orders.ShippedDate is NULL

# ************Question 8 ***********
how many orders are "single item" (only one product ordered)?

    - select count(*) from ( select OrderID from orders group by OrderID having count(ProductID) = 1) as x

# ************Question 9 ***********
avergae sales per transaction (orderId) for 'Romero y Tomillo'

    - select avg(sales) as avg_sales from (select sum(orders.Total_Amount) as sales from customers,orders where customers.CustomerID=orders.CustomerID and customers.CompanyName like 'Romero y Tomillo' group by orders.OrderID) as sales

# ************Question 10 *************
How many days since "Noth/South" last purchase?

    - select datediff('2026-09-27',max(orders.OrderDate)) from customers,orders 
where orders.CustomerID=customers.CustomerID and CompanyName='North/South'

# ************Question 11 **************
How many customers have ordered only once?

    - select count(*) from customers where customerid in ( select customers.CustomerID from customers,orders
where orders.CustomerID=customers.CustomerID group by customers.CustomerID
having count(orders.OrderID)=1)

# ************Question 12 **************
how many new customers (first purchase in current year) in 2022?

    - select count(*) as new_customers from (select CustomerID, min(OrderDate) as first_purchase from orders group by customerid) as first_purchase where year(first_purchase)=2022

# *************Question 13 **************
how many lost customers(no purchases in current year) in 2022?

    - select count(*) as new_customers from (select CustomerID, max(OrderDate) as last_purchase from orders group by customerid) as last_purchase where year(last_purchase)<2022

# *************Question 14 ***************
how many customers has NEVER puchased Queso Cabrales?

    - select count(*) from customers where CustomerID not in (select customers.CustomerID from customers,orders,products where 
customers.CustomerID=orders.CustomerID and orders.ProductID=products.ProductID and products.ProductName='Queso Cabrales'
group by customers.CustomerID)

# *************Question 15 ************
how many customers have purchased only Queso Cabrales (per OrderId)?

    - select count(*) from customers where CustomerID in (select customers.CustomerID from customers,orders,products where 
customers.CustomerID=orders.CustomerID and orders.ProductID=products.ProductID and products.ProductName='Queso Cabrales'
group by orders.OrderID)

# ***************Question 16 ***********
How many products are out of stock?

    - select count(products.ProductID) from products where products.UnitsInStock=0

# **************Question 17 *************
How many products need to be restocked? (based on restock levels).

    - select count(ProductId) from products where products.UnitsInStock<products.ReorderLevel

# **************Question 18 **************
How many products on order we need to restock?

    - select count(ProductId) from products where products.UnitsInStock<products.ReorderLevel and products.UnitsOnOrder>0

# ***************Question 19 ****************
what is the stocked value of the discountinued products?

    - select sum(products.UnitsInStock*products.UnitPrice) as 'Total stocke' from products
where products.Discontinued>0

# ****************Question 20 ***************
which vendor has the highest stock value?

    - select suppliers.ContactName,products.productname,sum(products.UnitsInStock * products.UnitPrice) as stockValue from suppliers,products where products.SupplierID=suppliers.SupplierID group by suppliers.SupplierID order by stockValue desc limit 1

# *****************Question 21 ****************
How many employees(%) are female?

    - select count(*) from employees where employees.Gender='Female'

# ****************Question 22 **************
how many employees are 60 years old or over?

    - select count(*) from employees where datediff('2026-09-27',employees.birthdate)>=60 

# *****************Question 23 *************
Which employee had the highest sales in 2022?

    - select employees.FullName,sum(orders.Total_Amount) as total_sale from orders,employees
where orders.EmployeeID=employees.EmployeeID and year(orders.OrderDate)=2022 group by orders.EmployeeID order by total_sale desc limit 1

# *****************Question 24 **************
how many employees sold over $100K in 2022

    - select employees.FullName,sum(orders.Total_Amount) as total_sale from orders,employees
where orders.EmployeeID=employees.EmployeeID and year(orders.OrderDate)=2022 group by orders.EmployeeID having sum(orders.Total_Amount)>=100000 order by total_sale desc

# *****************Question 25 **************
how many employees got hired in 1994?

    - select count(*) from employees where year(employees.HireDate)=1994 

'''