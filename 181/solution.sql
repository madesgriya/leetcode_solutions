SELECT name AS Employee 
FROM Employee AS e1
WHERE managerId IS NOT NULL
AND SALARY > (SELECT salary FROM Employee WHERE id=e1.managerId)