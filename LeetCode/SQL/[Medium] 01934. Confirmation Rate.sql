/*
# MySQL
SELECT S.user_id,
        round(avg(if(C.action = 'confirmed',1,0)),2) AS confirmation_rate 
FROM Signups S
    LEFT JOIN Confirmations C
    ON S.user_id = C.user_id
GROUP BY S.user_id
*/

-- # postgreSQL
SELECT S.user_id, round(avg(case when c.action = 'confirmed' then 1 else 0 end),2) AS confirmation_rate 
FROM Signups S
    LEFT JOIN Confirmations C
    ON S.user_id = C.user_id
GROUP BY S.user_id