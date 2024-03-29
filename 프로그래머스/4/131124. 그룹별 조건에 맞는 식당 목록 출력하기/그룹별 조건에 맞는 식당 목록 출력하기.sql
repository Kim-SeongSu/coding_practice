SELECT MP.MEMBER_NAME, RR.REVIEW_TEXT, LEFT(RR.REVIEW_DATE,10) REVIEW_DATE
FROM REST_REVIEW RR
    LEFT JOIN MEMBER_PROFILE MP
    ON RR.MEMBER_ID = MP.MEMBER_ID
WHERE RR.MEMBER_ID in (
    SELECT RRRank.MEMBER_ID
    FROM (SELECT MEMBER_ID, rank() over (ORDER BY count(MEMBER_ID) DESC) ranking
          FROM REST_REVIEW
          GROUP BY MEMBER_ID
         ) RRRank
    WHERE RRRank.ranking = 1)
ORDER BY 3, 2