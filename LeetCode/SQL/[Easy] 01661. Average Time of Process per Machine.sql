/*
# MySQL
SELECT S.machine_id, round(avg(E.timestamp - S.timestamp),3) AS processing_time
FROM Activity S
    INNER JOIN Activity E
    ON S.machine_id = E.machine_id and S.process_id = E.process_id
WHERE S.activity_type = 'start' and E.activity_type = 'end'
GROUP BY S.machine_id
*/

-- postgreSQL
SELECT S.machine_id, round(avg(E.timestamp - S.timestamp)::numeric,3) AS processing_time
FROM Activity S
    INNER JOIN Activity E
    ON S.machine_id = E.machine_id and S.process_id = E.process_id
WHERE S.activity_type = 'start' and E.activity_type = 'end'
GROUP BY S.machine_id