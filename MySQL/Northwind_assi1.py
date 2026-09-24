'''
# *************Question 1 **************
Show  all the orders of customer HANNA MOOS?

    - select orders.OrderID,orders.OrderDate,customers.CustomerID from orders,customers where customers.CustomerID=orders.CustomerID and customers.ContactName='Hanna Moos'

# *************Question 2 **************
Show all the products which purchase under 11011?

    - select products.ProductName from products,orders where products.ProductID=orders.ProductID and orders.OrderID=11011

# ************Question 3 ****************
Show total amount of order 11011?

    - select orders.Total_Amount from orders where orders.OrderID=11011

# ************Question 4 *************
    - select orders.OrderID,orders.OrderDate,customers.ContactName,employees.FullName from orders,customers,employees
    where orders.CustomerID=customers.CustomerID and orders.EmployeeID=employees.EmployeeID and 
    orders.OrderDate between '2024-03-30' and '2024-10-19'

# ************Question 5 ***************
Count Orders of each country?

    - select customers.Country,count(orders.orderid) from customers,orders where
    orders.CustomerID=customers.CustomerID group by customers.Country

# ************Question 6 ***************incomplete...
Max category sale in whole database?

# ***********Question 7 *****************incomplete...
Max Product Sale in Whole Database?

# ***********Question 8 **************
Total Sale in whole Database?

    - select sum(orders.Total_Amount) from orders

# *************Question 9 *************
Show total amout of particuler order include productname,qtysale,price & total amount?

    - select products.ProductName,orders.Quantity,orders.UnitPrice,orders.Total_Amount from orders,products
    where products.ProductID=orders.ProductID and orders.OrderID=10851

# **************Question 10 ************
Show all the orders made by Laura?

    - select orders.OrderID,orders.OrderDate,customers.CustomerID from orders,customers,employees
    where orders.CustomerID=customers.CustomerID and orders.EmployeeID=employees.EmployeeID
    and employees.FirstName='Laura'
    
'''