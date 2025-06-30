DROP TABLE IF EXISTS countries;
DROP SEQUENCE IF EXISTS country_id_sequence;
DROP TABLE IF EXISTS cities;
DROP SEQUENCE IF EXISTS cities_id_sequence;

CREATE SEQUENCE IF NOT EXISTS countries_id_sequence;
CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    country VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS cities_id_sequence;
CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    city VARCHAR(255),
    country_id INT
);

INSERT INTO countries (country) VALUES ('United Kingdom');
INSERT INTO countries (country) VALUES ('France');
INSERT INTO countries (country) VALUES ('USA');

INSERT INTO cities (city, country_id) VALUES ('London', 1);
INSERT INTO cities (city, country_id) VALUES ('Manchester', 1);
INSERT INTO cities (city, country_id) VALUES ('Liverpool', 1);
INSERT INTO cities (city, country_id) VALUES ('Paris', 2);
INSERT INTO cities (city, country_id) VALUES ('Washington', 3);
INSERT INTO cities (city, country_id) VALUES ('New York', 3);
