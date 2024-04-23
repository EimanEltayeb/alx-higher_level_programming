-- count_shows_by_genre.sql
SELECT tv_genres.names AS genre, COUNT(tv_shows.id) AS number_of_shows
LEFT JOIN tv_show_genres
	ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres
	ON tv_show_genres.genre_id = tv_genres.id
ORDER BY number_of_shows DESC;
