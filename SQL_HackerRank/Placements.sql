SELECT S_Name
FROM (
    SELECT S_Name, S_ID, Salary AS S_Salary, Friend_ID
    FROM (
        SELECT name AS S_Name, s.ID AS S_ID, Friend_ID
        FROM Friends f
        LEFT JOIN Students s ON f.ID = s.ID
    ) t1
    LEFT JOIN Packages p ON t1.S_ID = p.ID
) t2
LEFT JOIN Packages p ON t2.Friend_ID = p.ID
WHERE Salary > S_Salary
ORDER BY Salary


SELECT res
FROM(
    SELECT distinct(S_Name) AS res, Salary
    FROM (
        SELECT S_Name, S_ID, Salary AS S_Salary, Friend_ID
        FROM (
            SELECT name AS S_Name, s.ID AS S_ID, Friend_ID
            FROM Friends f
            LEFT JOIN Students s ON f.ID = s.ID
        ) t1
        LEFT JOIN Packages p ON t1.S_ID = p.ID
    ) t2
    LEFT JOIN Packages p ON t2.Friend_ID = p.ID
    WHERE Salary > S_Salary
    ORDER BY Salary   -- ORDER BY clause is not in SELECT list, references column 'p.Salary' which is not in SELECT list; this is incompatible with DISTINCT
) t3

