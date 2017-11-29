/*
Even though our database does not have entries in it, we can imagine that it does, and query it accordingly! 
    Referencing the table definitions above, write the SQL commands to carry out each of the queries described 
    below. Write your answers in a text/code editor.

1. List all the titles of the movies in the database.

2. List all the titles of the movies in the database in descending order of the year they were released.

3. Insert a new record into the directors table for Jean-Pierre Jeunet whose country of origin is France. 
    (Note: Assume the column for director_id is auto incremented, so you don't need to put in a value 
    for that column.)

4. List the director_id for Jean-Pierre Jeunet.

5. Insert a new record into the movies table for Amelie which was released in 2001 and directed by Jean-
    Pierre Jeunet. (Hint: Assume the id you got from the last query was "2" and use that. And, like question 
    3, assume the movie_id column is auto incremented).

6. List all columns for all records of the directors table in ascending alphabetical order of the 
    director's country of origin.

7. List the country of origin of the director of Amelie. (You could do this using either a join or a subquery. 
    Use a join.)

8. List all the movies in the database along with each movie's director, ordered by the director's last 
    name in ascending order. (Hint: you'll want to use a join and choose the columns title, first, and 
    last).
*/