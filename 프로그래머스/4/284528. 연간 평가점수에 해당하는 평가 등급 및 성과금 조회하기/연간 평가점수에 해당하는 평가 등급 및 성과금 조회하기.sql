select A.EMP_NO, 
       EMP_NAME, 
       case when B.S >= 96 then 'S'
            when B.S >= 90 then 'A'
            when B.S >= 80 then 'B'
            else 'C' end GRADE,
        case when B.S >= 96 then SAL*0.2
            when B.S >= 90 then SAL*0.15
            when B.S >= 80 then SAL*0.1
            else 0 end BONUS
from HR_EMPLOYEES A
    inner join (select EMP_NO, avg(SCORE) S
                from HR_GRADE 
                group by EMP_NO) B
    on A.EMP_NO = B.EMP_NO
order by EMP_NO