/*

CREATE TABLE movies (
    movie_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(120),
    year INTEGER,
    director_id INTEGER,
    FOREIGN KEY (director_id) REFERENCES directors(director_id)
);

CREATE TABLE directors (
    director_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    first VARCHAR(120),
    last VARCHAR(120),
    country VARCHAR(120)
);

Even though our database does not have entries in it, we can imagine that it does, and query it accordingly! 
    Referencing the table definitions above, write the SQL commands to carry out each of the queries described 
    below. Write your answers in a text/code editor.

*/

/* 1. List all the titles of the movies in the database. */
SELECT title FROM movies;

/* 2. List all the titles of the movies in the database in descending order of the year they were released. */
 SELECT title FROM movies ORDER BY year DESC;

/* 3. Insert a new record into the directors table for Jean-Pierre Jeunet whose country of origin is France. 
    (Note: Assume the column for director_id is auto incremented, so you don't need to put in a value 
    for that column.) */
INSERT INTO directors (first, last, country) VALUES ("Jean-Pierre", "Jeunet", "France");

/* 4. List the director_id for Jean-Pierre Jeunet. */
SELECT director_id FROM directors WHERE first = "Jean-Pierre" AND last = "Jeunet";

/* 5. Insert a new record into the movies table for Amelie which was released in 2001 and directed by Jean-
    Pierre Jeunet. (Hint: Assume the id you got from the last query was "2" and use that. And, like question 
    3, assume the movie_id column is auto incremented). */
INSERT INTO movies (title, year, director_id) VALUES ("Amelie", 2001, 2);

/* 6. List all columns for all records of the directors table in ascending alphabetical order of the 
    director's country of origin. */
SELECT * FROM directors ORDER BY country;

/* 7. List the country of origin of the director of Amelie. (You could do this using either a join or a subquery. 
    Use a join.) */
SELECT directors.country FROM directors 
    INNER JOIN movies 
    ON directors.director_id = movies.director_id 
    WHERE movies.title = "Amelie";
    
/* Doing the same thing with a subquery would be the following: */
SELECT country FROM directors
    WHERE director_id IN 
    (SELECT director_id FROM movies WHERE title = "Amelie");

/* 8. List all the movies in the database along with each movie's director, ordered by the director's last 
    name in ascending order. (Hint: you'll want to use a join and choose the columns title, first, and 
    last). */
SELECT movies.title, directors.first, directors.last 
    FROM directors
    JOIN movies
    ON directors.director_id = movies.director_id
    ORDER BY directors.last;