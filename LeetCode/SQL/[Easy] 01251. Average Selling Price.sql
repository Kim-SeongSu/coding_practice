/*
# MySQL
SELECT P.product_id, IFNULL(round(sum(P.price*U.units)/sum(U.units),2),0) AS average_price
FROM Prices P
    LEFT JOIN UnitsSold U
    ON P.product_id = U.product_id
        # AND U.purchase_date >= P.start_date
        # AND P.end_date >= U.purchase_date
        AND U.purchase_date BETWEEN P.start_date and P.end_date
GROUP BY P.product_id
*/

-- # postgreSQL
SELECT P.product_id, COALESCE(ROUND(cast(sum(P.price * U.units) as numeric) /sum(U.units),2),0) AS average_price
FROM Prices P
    LEFT JOIN UnitsSold U
    ON P.product_id = U.product_id
    AND U.purchase_date BETWEEN P.start_date and P.end_date
GROUP BY P.product_id