# MySQL & PostgreSQL
select product_id, year first_year, quantity, price
from Sales
where (product_id, year) in (select product_id, min(year) from Sales group by product_id)


# PostgreSQL
SELECT product_id, year AS first_year, quantity, price
FROM (SELECT product_id,
             year,
             quantity,
             price,
             RANK() OVER (PARTITION BY product_id ORDER BY year) as year_no
      FROM Sales)
WHERE year_no = 1
