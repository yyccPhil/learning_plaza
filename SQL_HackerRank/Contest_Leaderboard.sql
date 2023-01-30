SELECT h_id, name, total
FROM (
    SELECT h.hacker_id AS h_id, name, sum(ms) AS total
    FROM (
        SELECT hacker_id, challenge_id, max(score) AS ms
        FROM Submissions
        GROUP BY hacker_id, challenge_id) s
    LEFT JOIN Hackers h ON s.hacker_id = h.hacker_id
    GROUP BY h.hacker_id, name
) t1
WHERE total > 0
ORDER BY total DESC, h_id
