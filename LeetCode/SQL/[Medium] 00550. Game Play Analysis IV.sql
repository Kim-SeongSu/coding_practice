/*
# MySQL
with frac as (select * 
             from Activity 
             where (player_id, event_date) in (select player_id, date_add(min(event_date), INTERVAL 1 DAY) 
                                               from Activity 
                                               group by player_id))

select round((select count(*) from frac)/count(distinct A.player_id),2) fraction
from Activity A


or


SELECT ROUND(COUNT(*) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM Activity
WHERE (player_id, event_date) IN   (SELECT player_id, DATE_ADD(MIN(event_date), INTERVAL 1 DAY)
                                    FROM Activity
                                    GROUP BY player_id)
*/

-- # postgreSQL
SELECT ROUND(COUNT(DISTINCT player_id)::numeric / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM Activity
WHERE (player_id, event_date - INTERVAL '1 DAY') IN (SELECT player_id, MIN(event_date) AS first_login FROM Activity GROUP BY player_id)