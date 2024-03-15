# MySQL
-- with pids as (
-- select pid
-- from (select pid 
--       from Insurance 
--       where tiv_2015 in (select tiv_2015 
--                          from Insurance 
--                          group by tiv_2015 having count(tiv_2015) > 1)
-- union all
--       select pid
--       from Insurance
--       where concat(lat,'-',lon) not in (select concat(lat,'-',lon) ll
--                                         from Insurance
--                                         group by ll having count(ll) > 1)) pids
-- group by pid having count(pid) >1)

-- select round(sum(tiv_2016),2) tiv_2016 
-- from Insurance
-- where pid in (select * from pids)

SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
)
AND (lat, lon) IN (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
)


#  PostgreSQL
SELECT ROUND(SUM(tiv_2016)::numeric, 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1)
AND (lat, lon) IN (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1)


# 다른 풀이
select ROUND(sum(tiv_2016)::numeric,2) as tiv_2016 
from (select
    tiv_2016,
    Count(*) Over (partition by lat,lon) as cnt1,
    Count(*) Over (partition by tiv_2015) as cnt2
    from Insurance 
) as c 
where c.cnt1 = 1 and c.cnt2 > 1;