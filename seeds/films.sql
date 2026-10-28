DROP TABLE IF EXISTS films CASCADE;

CREATE TABLE films (
    id SERIAL PRIMARY KEY,
    title TEXT,
    release_year INT
);

INSERT INTO films(title, release_year) VALUES ('Tangled', 2011);