-- 10genre_id_by_show
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows 
JOIN tv_show_genres
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id  ASC;

