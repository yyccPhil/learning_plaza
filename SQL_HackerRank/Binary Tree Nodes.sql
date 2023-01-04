-- Debug experience~
-- 1. is null, not = null
-- 2. 'column to array'
-- 3. 'not in' cannot work

-- select N, case when P is null then 'Root'
--                when N not in (select distinct P from BST where P is not null) then 'Leaf'
--                else 'Inner' end
-- from BST
-- order by N

select N, case when P is null then 'Root' -- is null, not = null!
               when N in (select distinct P from BST) then 'Inner' -- distinct can save resource
               else 'Leaf' end
from BST
order by N

-- 1. The basic 'column to row', that is, a single column is converted into 'an array' to use 'in', we can just use the subquery 'select'.
-- 2. When I tried to use subquery for 'not in' like line 2 (I didn't add 'where' first), I cannot get the output. It confused me for a long time.
-- Then I used 'left join' and found the target data. But why 'not in' cannot work. After search, I found that 'not in' of MySQL cannot include 'null', otherwise it will interpret for 'not in null'. But all of the data which is not null can satisfy 'not in null', so there is no output. 
-- Therfore, we need to use 'where' first to exclude null values.
