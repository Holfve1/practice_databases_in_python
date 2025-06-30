DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_sequence;
DROP TABLE IF EXISTS users; -- DROP TABLE IF EXISTS users CASCADE; will drop all child tables when it is dropped (drop any table connected beneath it)
DROP SEQUENCE IF EXISTS users_id_sequence;


CREATE SEQUENCE IF NOT EXISTS users_id_sequence;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    email VARCHAR (255)
);

CREATE SEQUENCE IF NOT EXISTS posts_id_sequence;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    content VARCHAR(255),
    views INT,
    user_id INT,
    CONSTRAINT fk_users FOREIGN KEY (user_id)
        references users(id)
        on delete cascade
);

-- users
INSERT INTO users (username, email) VALUES ('Jeff19', 'jeffbloom@email.com');
INSERT INTO users (username, email) VALUES ('Chris1', 'chrisd17@email.com');

-- posts;
INSERT INTO posts (title, content, views, user_id) VALUES ('My first post', 'This is the content', 7, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('My second post', 'There is no content', 13, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('chris post', 'I am the best', 1, 2);

