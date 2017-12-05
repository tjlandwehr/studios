/* Your Task: */

/* Sarah created these tables and inserted all the data into them, but she needs your help to run some queries. 
    You can use the SQL tab in the movie-buff database to run queries. Just type your SQL statement(s) in the 
    box and press the Go button. */

/* As an example, say Sarah wants to know the first and last names of any of her friends who borrowed one of 
    her movies before 2010. */

/* We know we'll want to use the viewings table, since that has the dates of when people have viewed her 
    DVDs as well as their ids. And we know we want to use the viewers table since that has the first and last 
    names of her friends. Since we want data from two tables, we know we'll likely need to use a join. We also 
    know that the column in common between the two tables is the viewer_id column, so that will be what 
    we join on. Our SQL statement will be: */

SELECT DISTINCT viewers.first, viewers.last
FROM viewers
JOIN viewings
ON viewers.viewer_id = viewings.viewer_id
WHERE viewings.date_viewed < '2010-01-01';

/* Here are some of the things Sarah needs your help with: */

/* 1. Find out which countries the directors in her collection are from (and make sure your result set only 
    lists each country only once). */
SELECT DISTINCT country
FROM directors;

/* 2. Who are the French directors in her database? */
SELECT DISTINCT directors.first, directors.last
FROM directors
WHERE country = "France";

/* 3. What is the date of the first time someone viewed one of Sarah's movies? */
SELECT DISTINCT date_viewed AS first_viewing
FROM viewings
ORDER BY date_viewed LIMIT 1;

/* 4. How many movies in her collection were directed by people born in the USA? */
SELECT COUNT(country) AS USA_directors
FROM directors
WHERE country = "USA";

/* 5. What are the titles of the movies in her collection that were directed by Akira Kurosawa? */
SELECT title AS Akira_Kurosawa_movies
FROM movies
JOIN directors
ON movies.director_id = directors.director_id
WHERE directors.first = "Akira" AND directors.last = "Kurosawa";

/* 6. How many times has the movie "Talk to Me" been viewed? */
SELECT COUNT(date_viewed) AS Talk_to_Me_Viewings
FROM viewings
JOIN movies
ON viewings.movie_id = movies.movie_id
WHERE movies.title = "Talk to Me";

/* 7. When was the last time someone viewed one of her movies? */
SELECT date_viewed AS last_viewing
FROM viewings
ORDER BY date_viewed DESC LIMIT 1;

/* OR */
SELECT MAX(date_viewed) FROM viewings;

/* 8. What is the id of the last-viewed movie? */
SELECT movies.movie_id AS last_viewed_movie_id
FROM movies
JOIN viewings
ON movies.movie_id = viewings.movie_id
ORDER BY viewings.date_viewed DESC LIMIT 1;

/* 9. What is the title of the first movie she loaned to a friend for viewing? */
SELECT movies.title AS first_movie_viewed
FROM movies
JOIN viewings
ON movies.movie_id = viewings.movie_id
ORDER BY viewings.date_viewed LIMIT 1;

/* 10. What is the first and last name of the person who viewed the last-viewed movie? */
SELECT viewers.first, viewers.last
FROM viewers
JOIN viewings
ON viewers.viewer_id = viewings.viewer_id
ORDER BY viewings.date_viewed DESC LIMIT 1;


/* BONUS MISSIONS */

/* 11. Write the SQL query to display the DVDs that others have watched in order of most viewed to least 
    viewed. What's the title of the most-viewed movie(s) in Sarah's collection? */
SELECT movies.title
FROM movies
JOIN viewings
ON movies.movie_id = viewings.movie_id
GROUP BY viewings.viewing_id
ORDER BY COUNT(viewings.date_viewed) DESC;

/* OR */
SELECT COUNT(viewing_id) AS viewNum, movies.title
FROM viewings
JOIN movies
ON movies.movie_id = viewings.movie_id
WHERE viewNum IN (
    SELECT COUNT(viewing_id) AS viewNum, movies.title
    FROM viewings
    GROUP BY movies.movie_id
    ORDER BY viewNum DESC;
    LIMIT 1
)
GROUP BY movies.movie_id
ORDER BY viewNum DESC;

/* OR */

SELECT COUNT(viewing_id) AS viewNum, movies.title
FROM viewings
JOIN movies
ON movies.movie_id = viewings.movie_id
GROUP BY movies.movie_id
HAVING viewNum = (
    SELECT COUNT(viewing_id) AS viewNum
    FROM viewings
    JOIN movies
    ON movies.movie_id = viewings.movie_id
    GROUP BY movies.movie_id
    ORDER BY viewNum DESC
    LIMIT 1
);

/* 12. Find the email of everyone who has watched "The Tango Lesson", so Sarah can email them and ask 
    what they thought of it. */
SELECT viewers.email
FROM viewers
JOIN viewings
ON viewers.viewer_id = viewings.viewer_id
JOIN movies
ON viewings.movie_id = movies.movie_id
WHERE movies.title = "The Tango Lesson";

/* 13. Sarah is hosting a Kurosawa film festival soon and needs an email list to send out invites. What are the 
    full names and emails of all her friends who have watched any movie by Akira Kurosawa? */
SELECT DISTINCT viewers.first, viewers.last, viewers.email
FROM viewers
JOIN viewings
ON viewers.viewer_id = viewings.viewer_id
JOIN movies
ON viewings.movie_id = movies.movie_id
JOIN directors
ON movies.director_id = directors.director_id
WHERE directors.first = "Akira" AND directors.last = "Kurosawa";

/* OR */
SELECT DISTINCT viewers.first, viewers.last, viewers.email
FROM viewings
JOIN movies
ON movies.movie_id = viewings.movie_id
JOIN viewers
ON viewers.viewer_id = viewings.viewer_id
JOIN directors
ON directors.director_id = movies.director_id
WHERE directors.first = 'Akira' AND directors.last = 'Kurosawa';