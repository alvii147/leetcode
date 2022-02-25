SELECT Scores.Score AS score, COUNT(DistinctScores.Score) AS `Rank` FROM
(SELECT DISTINCT Score FROM Scores) AS DistinctScores, Scores
WHERE Scores.Score <= DistinctScores.Score
GROUP BY Scores.Id, Scores.Score
ORDER BY Scores.Score DESC;
