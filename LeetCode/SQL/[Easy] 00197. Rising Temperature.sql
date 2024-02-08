-- # datediff는 MySQL에서 가능
-- SELECT w1.id
-- FROM Weather w1, Weather w2
-- WHERE datediff(w2.recordDate, w1.recordDate) = 1 AND w2.temperature > w1.temperature;

-- # postgreSQL
SELECT w1.id
FROM Weather w1, Weather w2
WHERE w1.recordDate - w2.recordDate = 1 AND w1.temperature > w2.temperature;