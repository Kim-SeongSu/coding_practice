select year(A.DIFFERENTIATION_DATE) YEAR, B.ms - SIZE_OF_COLONY YEAR_DEV, A.ID
from ECOLI_DATA A
    left join (select year(DIFFERENTIATION_DATE) YEAR, max(SIZE_OF_COLONY) ms
               from ECOLI_DATA
               group by 1) B
    on year(A.DIFFERENTIATION_DATE) = B.YEAR
order by 1, 2