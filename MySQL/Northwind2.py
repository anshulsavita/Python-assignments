'''
# ***************Question 1 ***************
Show all the orderid,customername which ordered ‘Tofu’ product

    - select orders.OrderID,customers.ContactName from orders,customers,products
where orders.CustomerID=customers.CustomerID and orders.ProductID=products.ProductID
and products.ProductName='Tofu'

# **************Question 2 ***************
Show all the supplier names which supplies ‘Tofu’ & ‘Ipoh Coffiee’

    - select suppliers.SupplierID,suppliers.ContactName from suppliers
where suppliers.SupplierID in (select supplierid from products where products.ProductName in ('tofu','ipoh coffee'))

# ***************Question 3
# list all the customers of city ‘London’ who ordered  products more then one time

    - select customers.ContactName from customers,orders
where customers.CustomerID=orders.CustomerID and customers.City='London' group by customers.CustomerID
having count(orders.OrderID)>1

# ***************Question 4
Show all the customer name & employee name having same cities

    - select customers.ContactName,employees.FullName from employees,customers
where customers.City=employees.city

# **************Question 5 ************
Show all the customer who are owner of  company
    - select customers.ContactName from customers where customers.ContactTitle='Owner'

# **************Question 6 *************
Show all orders which sale by employee ‘Anne’

    - select orders.OrderID,products.ProductName from orders,products,employees
where orders.ProductID=products.ProductID and orders.EmployeeID=employees.EmployeeID and employees.FirstName='Anne'

# ***************Question 7 ***************
Show Most productive employee of NorthwindSale
    - select employees.FullName,count(*) as SalesCount from employees,orders
where orders.EmployeeID=employees.EmployeeID group by employees.EmployeeID limit 1 

# ***************Question 8 **************
8.	Show all the product sale by company ‘Tokyo Traders’

    - select products.ProductName from products,suppliers
where products.SupplierID=suppliers.SupplierID 
and suppliers.CompanyName='Tokyo Traders' group by products.ProductID

# ****************Question 9 ****************
9.	Show Total Sale of each Month

    - select MonthName(orders.OrderDate) as 'Month' ,sum(orders.Total_Amount) as 'Total Sale' from orders group by Month

# ***************Question 10**************
Show Total sale of each Sunday. Show Date  WeekName TotalSale

    - select orders.OrderDate,dayName(orders.OrderDate) as 'Week day' ,sum(orders.Total_Amount) as 'Total Sale' from orders
where dayName(orders.OrderDate)='Sunday' group by orders.OrderDate

'''