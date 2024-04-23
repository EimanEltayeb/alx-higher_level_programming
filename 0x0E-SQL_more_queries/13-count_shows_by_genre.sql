-- count_shows_by_genre.sql
SELECT tv_genres.name AS genre, COUNT(tv_shows.id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres
	ON tv_genres.id = show_genres.genre_id
JOIN tv_shows
	ON tv_show_genres.show_id = tv_shows.id
ORDER BY number_of_shows DESC;
