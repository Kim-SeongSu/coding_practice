/*
# MySQL
SELECT R.contest_id, round(100*count(user_id)/(SELECT count(U.user_id) FROM Users U) ,2) percentage 
FROM Register R
GROUP BY R.contest_id
ORDER BY percentage DESC, R.contest_id
*/

-- # postgreSQL
SELECT R.contest_id, round(100*count(user_id)/(SELECT count(U.user_id) FROM Users U) :: numeric ,2) percentage 
FROM Register R
GROUP BY R.contest_id
ORDER BY percentage DESC, R.contest_id