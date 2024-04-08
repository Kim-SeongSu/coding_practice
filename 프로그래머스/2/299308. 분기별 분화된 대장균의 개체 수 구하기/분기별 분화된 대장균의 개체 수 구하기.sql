select QUARTER, count(QUARTER) ECOLI_COUNT
from (select case when month(DIFFERENTIATION_DATE) in (1,2,3) then '1Q' 
            when month(DIFFERENTIATION_DATE) in (4,5,6) then '2Q'
            when month(DIFFERENTIATION_DATE) in (7,8,9) then '3Q'
            else '4Q' end QUARTER
from ECOLI_DATA) A
group by 1
order by 1