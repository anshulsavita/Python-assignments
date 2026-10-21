'''
*****Exercise simple Queries.

1.)
select customers.*,orders.*,suppliers.* from customers,orders,suppliers 

2.)
select * from customers order by customers.Country,customers.ContactName

3.)
select * from orders order by orders.OrderDate

4.)
select count(*) from orders where Year(orders.OrderDate)='1997'

5.)
select contactName from customers where contactTitle like '%manager' order by contactName

6.)
select * from orders where orders.OrderDate = '1997-5-19'


*****Exercise SQL Queries for JOINS

1.)
select * from orders,customers where Year(orders.OrderDate)='1996' and orders.CustomerID=customers.CustomerID

2.)
select employees.city,count(employees.EmployeeID),count(customers.CustomerID) from employees
left join customers on employees.city=customers.city group by employees.city 

3.)
select customers.city,count(distinct employees.EmployeeID),count(distinct customers.CustomerID) from customers
left join employees on employees.city=customers.city group by customers.city 

4.)incomplete...

*********Exercise SQL Queries for having.

1.)
select orders.OrderID,employees.FullName from orders,employees
where orders.EmployeeID=employees.EmployeeID and orders.ShippedDate > orders.RequiredDate

2.)
select products.ProductID,sum(orders.Quantity) from orders,products 
where orders.ProductID=products.ProductID group by products.ProductID 
having sum(orders.Quantity)<200

3.)
select customers.CustomerID,count(*) from orders,customers where orders.CustomerID=customers.CustomerID 
and orders.OrderDate>='1996-12-31' group by customers.CustomerID 
having count(*)>15

********Exercise SQL Inserting Recors

1.)
insert into employees(LastName,FirstName,Title,TitleofCourtesy,Birthdate,
HireDate,City,Region,PostalCode,Country,HomePhone,ReportsTo) 
values('Savita','Anshul','President','Mr.','2006-09-29','2026-08-27','Gwalior',
'WA',474001,'India','9301579572',2)

2.)
insert into orders(CustomerID,EmployeeID,OrderDate,RequiredDate) 
values('AROUT',1,'2023-12-04','2024-01-05')

3.)
insert into order_Details(OrderId,ProductId,UnitPrice,Quantity,Discount) 
values(11077,1,7,2,0)

*********Exercise SQL Updating Records

1.)
update employees 
set HomePhone=9039290305
where employees.EmployeeID=10

2.)
update order_details
set Quantity=2*Quantity
where OrderId=11077 and productId=1

3.)
update order_details
set Quantity = 2 * Quantity
where OrderID IN (select OrderID from Orders where EmployeeID = 10)

Exercise SQL Deleting Records

1.)
delete from employees
where employeeid=10

**********Exercise Advances SQL queries

1.)
select sum(orders.Total_Amount) from orders where year(orders.OrderDate)=1997

2.)
select customers.CustomerID,customers.ContactName,sum(orders.Total_Amount) from orders,customers
where orders.CustomerID=customers.CustomerID group by customers.CustomerID

3.)
select products.ProductID,products.ProductName,sum(orders.Total_Amount) from products,orders
where orders.ProductID=products.ProductID group by products.ProductID order by sum(orders.Total_Amount) desc limit 1

4.) incomplte...query cumplete hai bas view nahi banaya hai, kaise banate hai nahi pata.
select customers.CustomerID,customers.ContactName,sum(orders.Total_Amount) from orders,customers
where orders.CustomerID=customers.CustomerID group by customers.CustomerID

5.)
select customers.CustomerID,customers.ContactName,sum(orders.Total_Amount) from orders,customers
where orders.CustomerID=customers.CustomerID and customers.Country='UK' group by customers.CustomerID having sum(orders.Total_Amount)>1000

6.)
select customers.CustomerID,customers.ContactName,customers.Country,sum(orders.Total_Amount),
sum(case when year(orders.OrderDate) = 1997 then orders.Total_Amount ELSE 0 END) AS TotalIn1997 
from orders,customers where orders.CustomerID=customers.CustomerID group by customers.CustomerID

*********Querying the database - part 1

1.)
select categories.CategoryName,categories.Description from categories

2.)
select customers.ContactName,customers.CustomerID,customers.CompanyName from customers 
where customers.city='London'

3.)
select * from suppliers where suppliers.Fax is not null

4.)
select orders.CustomerID from orders where orders.RequiredDate between '1997-1-1' and '1998-1-1' and orders.Freight<100

5.)
select customers.CompanyName,customers.ContactName from customers 
where customers.ContactTitle='Owner' and customers.Country in ('Mexico','Sweden','Germany')

6.)
select products.ProductID,products.ProductName from products where products.Discontinued=1

7.)
select categories.CategoryName,categories.Description from categories 
where categories.CategoryName like 'Co%'

8.)
select CompanyName,City,Country,PostalCode from suppliers 
where suppliers.Address like '%rue%' order by suppliers.CompanyName

9.)
select products.ProductID,sum(products.UnitsInStock) from products group by products.ProductID

10.) ...incomplete 
select customers.ContactName,customers.Address from customers,orders 
where orders.CustomerID=customers.CustomerID and orders.ShipName='Speedy Express'

11.)
select suppliers.CompanyName,suppliers.ContactName,suppliers.ContactTitle,suppliers.Region from suppliers

12.)
select products.ProductName from products,categories where products.CategoryID=categories.CategoryID and
categories.CategoryName='condiments'

13.)
select customers.ContactName from customers where customers.CustomerID not in 
(select orders.CustomerID from orders)

14.)
insert into orders value('10688', 'VAFFE', '4', '2024-03-16', '2024-03-30', '2024-03-22', '3', '299.09', 'Amazon', 'Smagsloget 45', 'rhus', NULL, '8200', 'Denmark', '34', '14', '14', '0', '196')

15.)
update orders
set Shipname='Amazon Prime Shipping'
where shipname='Amazon'

16.)
incomplete because i dont have shippers table..

17.)
select employees.FirstName,employees.LastName,concat(employees.FirstName,' ',employees.LastName) as 'full name' from employees

18.)
insert into customers value('AGSKB', 'Alfreds Futterkiste', 'Anshul Davits', 'Sales Representative', 'Golpahadiya', 'Gwalior', NULL, '474001', 'India', '9301959572', '030-0076545')
insert into orders value('11077', 'AGSKB', '1', '2024-10-19', '2024-11-16', NULL, '2', '8.53', 'Rattlesnake Canyon Grocery', '2817 Milton Dr.', 'Albuquerque', 'NM', '87110', 'USA', '6', '7', '2', '0', '14')

19.)
delete from orders where ProductID=6 and CustomerID='AGSKB'

20.)
select sum(products.UnitsInStock) as TotalUnits from products group by products.ProductID
having TotalUnits>100 

*************Querying the database - part 2

1.)
select employees.FullName,employees.Address,employees.city,employees.Region from employees

2.)
select employees.FullName,employees.Address,employees.city,employees.Region
from employees where employees.Country='USA'

3.)
select employees.FullName,employees.Address,employees.city,employees.Region
from employees where DATEDIFF(now(),employees.BirthDate)>50

4.)
    i.)
select employees.FullName,employees.Address,employees.city,employees.Region
from employees,orders where orders.ShipCountry='Belgium' and orders.EmployeeID=employees.EmployeeID group by employees.EmployeeID

    ii.)
select employees.FullName,employees.Address,employees.city,employees.Region
FROM employees
inner join orders
on orders.EmployeeID=employees.EmployeeID
where  orders.ShipCountry='Belgium' group by employees.EmployeeID

5.)















'''