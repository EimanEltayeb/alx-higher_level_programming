-- count_shows_by_genre.sql
SELECT tv_genres.name AS genre, COUNT(tv_shows.id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres
	ON tv_show_genres.genre_id = tv_genres.id
JOIN tv_shows
	ON tv_shows.id = tv_show_genres.show_id
ORDER BY number_of_shows DESC;
