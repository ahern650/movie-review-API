CREATE TABLE IF NOT EXISTS movies (
    id          SERIAL PRIMARY KEY,

    title       VARCHAR(255) UNIQUE NOT NULL,
    year        VARCHAR(10),
    genre       VARCHAR(100),
    plot        TEXT,
    imdb_rating VARCHAR(10)
);