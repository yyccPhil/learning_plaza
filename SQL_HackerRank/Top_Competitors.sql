SELECT h.hacker_id, name
FROM Hackers h
JOIN (
    SELECT hacker_id, count(hacker_id) AS full_num
    FROM Submissions s
    JOIN (
        SELECT challenge_id, score
        FROM Challenges cha
        LEFT JOIN Difficulty d ON cha.difficulty_level = d.difficulty_level
    ) t1 ON s.challenge_id = t1.challenge_id
    WHERE t1.score = s.score  ------ cannot use an aggregation amount as a condition in current "WHERE" clause
    GROUP BY hacker_id
) t2 ON h.hacker_id = t2.hacker_id
WHERE full_num > 1
ORDER BY full_num DESC, h.hacker_id
