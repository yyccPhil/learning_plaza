SELECT algorithm,
    round(sum(CASE WHEN quarter(dt) = 1 AND year(dt) = "2020" THEN volume END), 6) AS "Q1",
    round(sum(CASE WHEN quarter(dt) = 2 AND year(dt) = "2020" THEN volume END), 6) AS "Q2",
    round(sum(CASE WHEN quarter(dt) = 3 AND year(dt) = "2020" THEN volume END), 6) AS "Q3",
    round(sum(CASE WHEN quarter(dt) = 4 AND year(dt) = "2020" THEN volume END), 6) AS "Q4"
FROM transactions t
LEFT JOIN coins c ON t.coin_code = c.code
GROUP BY algorithm
ORDER BY algorithm

-- transform column to row
