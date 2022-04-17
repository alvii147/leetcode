SELECT actor_id, director_id
FROM (
    SELECT actor_id, director_id, COUNT(*) AS cooperations
    FROM ActorDirector
    GROUP BY actor_id, director_id
) AS CooperationsCount
WHERE cooperations >= 3;
