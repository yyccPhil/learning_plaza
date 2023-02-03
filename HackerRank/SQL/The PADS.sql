select concat(Name, '(', left(Occupation, 1), ')')
from occupations
order by Name;
-- select concat('There are a total of ', cnt, ' ', lower(left(O, 1)), substr(O,2,(length(O)-1)), 's.')     -- Capital letter
-- from (
--     select Occupation as O, count(1) as cnt
--     from occupations
--     group by Occupation
--     ) t1
-- order by cnt, O
select concat('There are a total of ', count(1), ' ', lower(Occupation), 's.')
from occupations
group by Occupation
order by count(1), Occupation
