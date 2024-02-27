/*
# MySQL
SELECT query_name, round(avg(rating/position),2) quality, round(100*avg(if(rating<3,1,0)),2) poor_query_percentage
FROM Queries
WHERE query_name is not null
GROUP BY query_name
*/

-- # postgreSQL
SELECT query_name, round(avg(rating/position::numeric),2) quality, round(100*avg(CASE WHEN rating<3 THEN 1 ELSE 0 END)::numeric,2) poor_query_percentage
FROM Queries
WHERE query_name is not null
GROUP BY query_name