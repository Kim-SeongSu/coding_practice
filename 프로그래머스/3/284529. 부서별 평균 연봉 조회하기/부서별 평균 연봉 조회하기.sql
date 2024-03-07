select HD.DEPT_ID, DEPT_NAME_EN, HE.AVG_SAL
from HR_DEPARTMENT HD
    inner join (select DEPT_ID, round(avg(SAL)) AVG_SAL from HR_EMPLOYEES group by DEPT_ID) HE
    on HD.DEPT_ID = HE.DEPT_ID
group by 1
order by 3 desc