-- cities_by_state_join
SELECT cities.id, cities.name, states.name
FROM cities 
	NATURAL JOIN states
ORDER BY cities.id ASC;
