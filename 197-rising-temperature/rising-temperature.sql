# Write your MySQL query statement below
SELECT w1.Id
FROM Weather as w1, Weather as w2
WHERE dateDiff(w1.recordDate,w2.recordDate) = 1 AND w1.Temperature > w2.Temperature;