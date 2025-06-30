## descibing the problem:

As a coach
So I can get to know all students
I want to see a list of students' names.

As a coach
So I can get to know all students
I want to see a list of cohorts' names.

As a coach
So I can get to know all students
I want to see a list of cohorts' starting dates.

As a coach
So I can get to know all students
I want to see a list of students' cohorts.


Noun - students, names, cohort names, start_dates, list

## infer table Name and columns

| records | properties |
|_________|____________|
| student | name
| cohort  | name, start date

1. name of table will be: students

2. name of table will be: cohorts

## column types

Table: students
    id SERIAL,
    name text
    cohort_id int

Table: cohorts
    id SERIAL
    name text
    start_date date
    student_id int


## table relationship

1 cohort can have many students but 1 student can only have 1 cohort

## write the SQL

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    cohort_id (FK) INT,
);

CREATE TABLE cohorts (
    id SERIAL PRIMARY KEY
    name VARCHAR(255),
    start_date DATE,
);

## setting up the classes

Class cohort():
    #__init__
        #arguments - id, name, start date
        # returns - None
        # Side effects - None
    #__eq__
        #arguments - other
        # returns - None
        # Side effects - ensures our object is what it expects based on the database
    #__repr__
        #arguments - None 
        # returns - None
        # Side effects - structures data into a readable string when printed in terminal

class student():
    #__init__
        # arguments - id, name, cohort id
        # returns - None
        # Side effects - None
    #__eq__
         # rguments - other
        # returns - None
        # Side effects - ensures our object is what it expects based on the database
    #__repr__
        # arguments - None 
        # returns - None
        # Side effects - structures data into a readable string when printed in terminal

## repo classes

class CohortRepository():
    #__init__
        # argumenmts - connection # connect to db_connection
        # returns - None
        # side effects - None 
    # all
        # arguments - none
        # returns - everything in the table 
        # Side effects - None
    # find
        # arguments - 1 - id
        # returns - everything relating to the arguments (row)
        # Side effects - none
    # create
        # arguments - 1 - id
        # returns - None
        # Side effects - creates an entry into the table
    # delete
        # arguments - 1 - id
        # returns - None
        # Side effects - deletes and entry from the table 

class StudentRepository():

## test examples for repo