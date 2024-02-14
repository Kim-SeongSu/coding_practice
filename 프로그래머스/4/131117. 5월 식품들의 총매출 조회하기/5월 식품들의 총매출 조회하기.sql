SELECT P.PRODUCT_ID, P.PRODUCT_NAME, P.PRICE*sum(O.AMOUNT) TOTAL_SALES
FROM FOOD_PRODUCT P 
    INNER JOIN FOOD_ORDER O
    ON P.PRODUCT_ID = O.PRODUCT_ID
WHERE O.PRODUCE_DATE like '2022-05%'
GROUP BY P.PRODUCT_NAME
ORDER BY TOTAL_SALES DESC, P.PRODUCT_ID