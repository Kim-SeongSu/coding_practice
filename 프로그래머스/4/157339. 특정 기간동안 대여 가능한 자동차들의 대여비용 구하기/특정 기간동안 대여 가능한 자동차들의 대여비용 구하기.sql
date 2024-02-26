SELECT C.CAR_ID, C.CAR_TYPE, round(C.DAILY_FEE*30*(0.01*(100-ifnull(P.DISCOUNT_RATE,0)))) FEE
FROM (SELECT distinct CAR_ID, CAR_TYPE, DAILY_FEE
      FROM CAR_RENTAL_COMPANY_CAR
      WHERE CAR_ID NOT IN (SELECT CAR_ID
                           FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                           WHERE (start_date < '2022-11-01' AND end_date > '2022-11-30')
                                 OR start_date BETWEEN '2022-11-01' and '2022-11-30'
                                 OR end_date BETWEEN '2022-11-01' and '2022-11-30')) C
      INNER JOIN (SELECT CAR_TYPE, DISCOUNT_RATE 
                 FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
                 WHERE DURATION_TYPE = '30일 이상') P
      ON C.CAR_TYPE = P.CAR_TYPE
WHERE C.CAR_TYPE IN ('세단','SUV') 
      AND C.DAILY_FEE*0.3*(100-P.DISCOUNT_RATE) BETWEEN 500000 and 2000000
ORDER BY 3 DESC, 2, 1 DESC