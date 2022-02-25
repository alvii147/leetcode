SELECT id - 1 AS id, student FROM seat WHERE MOD(id, 2) = 0
UNION SELECT IF(id = max_seat.max_id, id, id + 1) AS id,
student FROM seat, (SELECT max(id) AS max_id FROM seat) AS max_seat
WHERE MOD(id, 2) = 1 ORDER BY id;
