SELECT max(salary) as SecondHighestSalary 
FROM Employee
WHERE salary <> (SELECT max(salary) FROM Employee) -- returns to the one record after the max