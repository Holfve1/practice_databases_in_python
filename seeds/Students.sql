DROP TABLE IF EXISTS students;
DROP SEQUENCE IF EXISTS student_id_sequence;
DROP TABLE IF EXISTS cohorts;
DROP SEQUENCE IF EXISTS cohort_id_sequence;

CREATE SEQUENCE IF NOT EXISTS student_id_sequence;
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    cohort_id INT,
    CONSTRAINT fk_cohort FOREIGN KEY (cohort_id)
        references cohorts(id)
        on delete cascade 
);

CREATE SEQUENCE IF NOT EXISTS cohort_id_sequence;
CREATE TABLE cohorts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    start_date DATE,
    student_id INT
);