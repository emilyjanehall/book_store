CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title TEXT,
    author TEXT
);

CREATE table users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);
