-- SELECT CEIL(AVG(salary)-AVG(CAST(REPLACE(CONVERT(salary, CHAR), "0", "") AS UNSIGNED)))
-- FROM employees;

SELECT CEIL(AVG(salary)-AVG(REPLACE(salary,0,'')))
FROM employees;



-- Tips learned from this problem:
-- 1. In MySQL, UNSIGNED number can be replaced like string directly, do not need to transform to string first!
-- 2. To transform data type, use CAST (https://dev.mysql.com/doc/refman/8.0/en/cast-functions.html#function_cast).
-- 3. Format number to 2 decimal places -- FORMAT(num, 2)
-- 4. 2 Ways to Check a Column’s Data Type in MySQL (from https://database.guide/4-ways-to-check-a-columns-data-type-in-mysql/)
--   a. The SHOW COLUMNS Statement
-- The SHOW COLUMNS statement displays information about the columns in a given table or view. We can pass the name of the table or view to return information on its columns:

-- SHOW COLUMNS FROM Pets;
-- Result:

-- +-----------+-------------+------+-----+---------+-------+
-- | Field     | Type        | Null | Key | Default | Extra |
-- +-----------+-------------+------+-----+---------+-------+
-- | PetId     | int         | NO   | PRI | NULL    |       |
-- | PetTypeId | int         | NO   |     | NULL    |       |
-- | OwnerId   | int         | NO   |     | NULL    |       |
-- | PetName   | varchar(60) | NO   |     | NULL    |       |
-- | DOB       | date        | YES  |     | NULL    |       |
-- +-----------+-------------+------+-----+---------+-------+
-- We can narrow it down to just one column if required:

-- SHOW COLUMNS FROM Pets
-- WHERE Field = 'PetName';
-- Result:

-- +---------+-------------+------+-----+---------+-------+
-- | Field   | Type        | Null | Key | Default | Extra |
-- +---------+-------------+------+-----+---------+-------+
-- | PetName | varchar(60) | NO   |     | NULL    |       |
-- +---------+-------------+------+-----+---------+-------+

--   b. The DESCRIBE / DESC Statement
-- The DESCRIBE statement is a shortcut for the SHOW COLUMNS FROM syntax:

-- DESCRIBE Pets;
-- Result:

-- +-----------+-------------+------+-----+---------+-------+
-- | Field     | Type        | Null | Key | Default | Extra |
-- +-----------+-------------+------+-----+---------+-------+
-- | PetId     | int         | NO   | PRI | NULL    |       |
-- | PetTypeId | int         | NO   |     | NULL    |       |
-- | OwnerId   | int         | NO   |     | NULL    |       |
-- | PetName   | varchar(60) | NO   |     | NULL    |       |
-- | DOB       | date        | YES  |     | NULL    |       |
-- +-----------+-------------+------+-----+---------+-------+
-- Just append the column name to narrow it to one column:

-- DESCRIBE Pets PetName;
-- Result:

-- +---------+-------------+------+-----+---------+-------+
-- | Field   | Type        | Null | Key | Default | Extra |
-- +---------+-------------+------+-----+---------+-------+
-- | PetName | varchar(60) | NO   |     | NULL    |       |
-- +---------+-------------+------+-----+---------+-------+
-- You can also use wildcards:

-- DESCRIBE Pets 'Pet%';
-- Result:

-- +-----------+-------------+------+-----+---------+-------+
-- | Field     | Type        | Null | Key | Default | Extra |
-- +-----------+-------------+------+-----+---------+-------+
-- | PetId     | int         | NO   | PRI | NULL    |       |
-- | PetTypeId | int         | NO   |     | NULL    |       |
-- | PetName   | varchar(60) | NO   |     | NULL    |       |
-- +-----------+-------------+------+-----+---------+-------+
-- You can also shorten it to DESC:

-- DESC Pets PetName;
-- Result:

-- +---------+-------------+------+-----+---------+-------+
-- | Field   | Type        | Null | Key | Default | Extra |
-- +---------+-------------+------+-----+---------+-------+
-- | PetName | varchar(60) | NO   |     | NULL    |       |
-- +---------+-------------+------+-----+---------+-------+

