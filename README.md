# Movie-recommendation-system-using-python-and-my-sql
the mysql query is given below
CREATE DATABASE MovieDB;

USE MovieDB;

CREATE TABLE Movies (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255),
    language VARCHAR(50),
    genre VARCHAR(50),
    release_year INT
);

INSERT INTO Movies (title, language, genre, release_year) VALUES
('Inception', 'English', 'Sci-Fi', 2010),
('Parasite', 'Korean', 'Thriller', 2019),
('Dangal', 'Hindi', 'Drama', 2016),
('Spirited Away', 'Japanese', 'Animation', 2001),
('Amélie', 'French', 'Romance', 2001),
('3 Idiots', 'Hindi', 'Comedy', 2009),
('Mad Max: Fury Road', 'English', 'Action', 2015);
