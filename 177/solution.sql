CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N = N-1; -- declaring variable before the return fuction  
  RETURN (
      # Write your MySQL query statement below.
      -- using IFNULL to catch output None to null
      IFNULL(( 
        SELECT salary as 'getNthHighestSalary(2)'
        FROM Employee 
        ORDER BY salary DESC
        LIMIT 1 OFFSET N),null
        )
  );
END