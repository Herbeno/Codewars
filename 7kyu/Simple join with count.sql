-- For this challenge you need to create a simple SELECT statement that will return all columns from the people table, and join to the toys table so that you can return the COUNT of the toys.

SELECT 
    p.id,
    p.name,
    COUNT (t.name) AS toy_count
FROM people AS p
LEFT jOIN toys AS t 
    ON p.id = t.people_id
GROUP BY p.id, p.name;