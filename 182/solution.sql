SELECT email AS Email 
FROM Person
HAVING COUNT(*) > 1 