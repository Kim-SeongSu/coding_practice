/*
# MySQL
SELECT LEFT(A.trans_date,7) month, A.country, count(A.id) trans_count, count(B.id) approved_count , sum(A.amount) trans_total_amount, ifnull(sum(B.amount),0) approved_total_amount
FROM Transactions A
    LEFT JOIN (SELECT * FROM Transactions WHERE state = 'approved') B
    ON A.id = B.id
GROUP BY 1, 2
*/

-- # postgreSQL
SELECT TO_CHAR(trans_date, 'YYYY-MM') AS month, 
       country, COUNT(state) AS trans_count, 
       COUNT(state) FILTER(WHERE state='approved') AS approved_count,   
       SUM(amount) AS trans_total_amount, 
       SUM(CASE WHEN state='approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM Transactions
GROUP BY 1, 2