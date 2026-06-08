from fastapi import APIRouter, HTTPException, Depends
import psycopg

from services.omdb_service import fetch_movie, format_movie
from models.movie import Movie
from database.connection import get_db_connection

router = APIRouter()

@router.get("/movie/{movie_name}", response_model=Movie)
def get_movie(movie_name: str, conn: psycopg.Connection = Depends(get_db_connection)):
    try:
        with conn.cursor() as cur:
            # log search query into search history table
            cur.execute(
                "INSERT INTO search_history(movie_title) VALUES(%s);",
                (movie_name,)
            )
            conn.commit()

            # check postgreSQL cache
            cur.execute(
                """
                SELECT id, title, year, genre, plot, imdb_rating
                FROM movies
                WHERE title ILIKE %s;
                """,
            (movie_name,)
            )

            db_movie = cur.fetchone()

            # cache hit
            if db_movie:
                print(f"Cache Hit: Loaded '{db_movie['title']}' from PostgreSQL")
                db_movie['ratings'] = []
                return db_movie

            # cache miss --> get from OMDb
            print(f"Cache Miss: Fetching '{movie_name}' from OMDb API...")
            raw_data = fetch_movie(movie_name)

            if raw_data.get("Response") == "False":
                raise HTTPException(
                    status_code=404,
                    detail="Movie not found"
                )

            formatted = format_movie(raw_data)

            # save movie into PostgreSQL
            cur.execute(
                """
                INSERT INTO movies(title, year, genre, plot, imdb_rating)
                VALUES(%s, %s, %s, %s, %s)
                ON CONFLICT (title) DO NOTHING
                RETURNING id, title, year, genre,plot, imdb_rating;
                """,
                (
                    formatted["title"],
                    formatted["year"],
                    formatted["genre"],
                    formatted["plot"],
                    formatted["imdb_rating"],
                )
            )

            new_movie = cur.fetchone()
            conn.commit()

            # conflict due to movie
            if not new_movie:
                cur.execute(
                    """
                    SELECT id, title, year, genre, plot, imdb_rating
                    FROM movies
                    WHERE title = %s;
                    """,
                    (formatted["title"],)
                )

                new_movie = cur.fetchone()

            new_movie["ratings"] = []
            return new_movie
    except psycopg.Error:
        conn.rollback()

        raise HTTPException(
            status_code=500,
            detail="Database error"
        )
