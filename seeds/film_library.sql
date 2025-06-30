-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS directors;
DROP SEQUENCE IF EXISTS directors_id_seq;
DROP TABLE IF EXISTS films;
DROP SEQUENCE IF EXISTS films_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS directors_id_seq;
CREATE TABLE directors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS films_id_seq;
CREATE TABLE films (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    release_year INTEGER,
    director_id INTEGER
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO directors (name) VALUES ('Steven Spielberg');
INSERT INTO directors (name) VALUES ('Ken Loach');
INSERT INTO directors (name) VALUES ('Sofia Coppola');
INSERT INTO directors (name) VALUES ('Chinonye Chukwu');

INSERT INTO films (title, release_year, director_id) VALUES ('Jurassic Park', 1993, 1);
INSERT INTO films (title, release_year, director_id) VALUES ('The Color Purple', 1986, 1);
INSERT INTO films (title, release_year, director_id) VALUES ('Looking for Eric', 2009, 2);
INSERT INTO films (title, release_year, director_id) VALUES ('Kes', 1969, 2);
INSERT INTO films (title, release_year, director_id) VALUES ('Lost in Translation', 2003, 3);
INSERT INTO films (title, release_year, director_id) VALUES ('A Very Murray Christmas', 2015, 3);
INSERT INTO films (title, release_year, director_id) VALUES ('Till', 2022, 4);