select
    case when a = b and a = c then 'Equilateral' 
         when a + b <= c or a + c <= b or b + c <= a then 'Not A Triangle'
         when a = b or a = c or b = c then 'Isosceles'
         when a != b and a != c and b != c then 'Scalene' end
from TRIANGLES
