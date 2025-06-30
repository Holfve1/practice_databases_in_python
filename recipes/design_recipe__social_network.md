## describe the problem

As a social network user,
So I can have my information registered,
I'd like to have a user account with my email address.

As a social network user,
So I can have my information registered,
I'd like to have a user account with my username.

As a social network user,
So I can write on my timeline,
I'd like to create posts associated with my user account.

As a social network user,
So I can write on my timeline,
I'd like each of my posts to have a title and a content.

As a social network user,
So I can know who reads my posts,
I'd like each of my posts to have a number of views.

Nouns - user account, email, username, post, title, content, views

## Table example

|records | properties |
|--------|------------|
|  user  | id, email, username |
|  post  | id, title, content, views, user_id

## column types 

Table: users
id SERIAL
username TEXT
email TEXT

Table: posts
id SERIAL
title TEXT
content TEXT
views INT
user_id INT

## Tables relationship

this will be one to many the one being users and posts being many as each user can have many posts connection to the account 

## SQL

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    email VARCHAR (255)
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,,
    title VARCHAR(255),
    content VARCHAR(255),
    views INT,
    user_id INT,
    CONSTRAINT fk_users FOREIGN KEY (user_id)
        references users(id)
        on delete cascade
);

