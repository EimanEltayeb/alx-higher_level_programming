-- cities_by_state_join
SELECT id, name, name
FROM cities 
	NATURAL JOIN states
ORDER BY id ASC
