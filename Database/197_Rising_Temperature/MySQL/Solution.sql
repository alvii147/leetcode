SELECT w2.Id FROM
Weather AS w1, Weather AS w2
WHERE w1.RecordDate = SUBDATE(w2.RecordDate, 1)
AND w1.Temperature < w2.Temperature;