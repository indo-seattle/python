# Create table DDL sample
# Create table Employee_Rajesh(Employee_ID int(5), First_Name varchar(20), Last_Name varchar(20), Job_Title varchar(20), DateofJoin DATE)

# Insert statements DML sample
# Insert into Employee_Rajesh(Employee_ID, First_Name, Last_Name, Job_Title, DateofJoin) values(1, 'John', 'Doe', 'Developer', '2019-05-01')
# Insert into Employee_Rajesh(Employee_ID, First_Name, Last_Name, Job_Title, DateofJoin) values(2, 'Matt', 'Kye', 'Tester', '2015-04-01')
# Insert into Employee_Rajesh(Employee_ID, First_Name, Last_Name, Job_Title, DateofJoin) values(3, 'Luke', 'Trent', 'Manager', '2012-12-01')
# Insert into Employee_Rajesh(Employee_ID, First_Name, Last_Name, Job_Title, DateofJoin) values(4, 'Sophia', 'Hung', 'Admin', '2015-07-01')
# Insert into Employee_Rajesh(Employee_ID, First_Name, Last_Name, Job_Title, DateofJoin) values(5, 'Larry', 'Kent', 'Tester', '2018-04-01')

# Select statements DML sample
# Select Employee_ID, First_Name, Last_Name, Job_Title, DateofJoin from Employee_Rajesh
# Select Employee_ID, First_Name, Last_Name, Job_Title, DateofJoin from Employee_Rajesh where Employee_ID = 1
# Select Employee_ID, First_Name, Last_Name, Job_Title, DateofJoin from Employee_Rajesh where Employee_ID > 2
# Select Employee_ID, First_Name, Last_Name, Job_Title, DateofJoin from Employee_Rajesh where First_Name = 'John'
# Select Employee_ID, First_Name, Last_Name, Job_Title, DateofJoin from Employee_Rajesh where DateofJoin > '2010-01-01'

# Alter table DDL sample
# Someimes first names are longer than 20 characters long, so let's increase to 50 characters.
# Alter table Employee_Rajesh Modify First_Name varchar(50)

# We realized all employees belong to a particular department, so let's add a new column
# Alter table Employee_Rajesh Add(Department varchar(50))

# Select statements DML sample
# Select Employee_ID, First_Name, Last_Name, Job_Title, DateofJoin, Department from Employee_Rajesh

