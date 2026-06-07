-- Movies Table
CREATE TABLE IF NOT EXISTS movies (
    id SERIAL   PRIMARY KEY,

    title       VARCHAR(255) UNQUE NOT NULL,
    year        INTEGER,
    genre       VARCHAR(100),
    plot        TEXT,
    imdb_rating NUMERIC(3,1),
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Favorites Table
CREATE TABLE IF NOT EXISTS favorites (
    id          SERIAL PRIMARY KEY,
    movie_id    INT REFERENCES movies(id) ON DELETE CASCADE UNIQUE,
    added_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- History Table
CREATE TABLE search_history (
    id          SERIAL PRIMARY KEY,
    movie_title VARCHAR(255) NOT NULL,
    searched_at TIMESTAMP DEFAULT  CURRENT_TIMESTAMP
);