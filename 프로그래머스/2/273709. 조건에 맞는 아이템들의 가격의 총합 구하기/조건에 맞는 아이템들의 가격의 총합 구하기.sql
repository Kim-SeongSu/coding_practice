SELECT sum(PRICE) TOTAL_PRICE
FROM ITEM_INFO
WHERE RARITY = 'LEGEND'
GROUP BY RARITY