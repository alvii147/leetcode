SELECT * FROM Cinema
WHERE MOD(Cinema.id, 2) = 1
AND Cinema.description <> 'boring'
ORDER BY Cinema.rating DESC;