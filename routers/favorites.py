from fastapi import APIRouter, HTTPException, Depends
import psycopg
from database.connection import get_db_connection

router = APIRouter(prefix="/favorites", tags=["favorites"])

@router.post("/{movie_id}")
def add_favorite(movie_id: int, conn: psycopg.Connection = Depends(get_db_connection)):
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO favorites(movie_id)
                VALUES(%s)
                ON CONFLICT (movie_id) DO NOTHING
                """,
                (movie_id,)
            )
            conn.commit()
            return {"message": f"Movie {movie_id} added to favorites"}

    except psycopg.Error:
        conn.rollback()
        raise HTTPException(
            status_code=500,
            detail="Database error"
        )

@router.get("/")
def get_favorites(conn: psycopg.Connection = Depends(get_db_connection)):
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT m.id, m.title, m.year, m.genre, m.plot, m.imdb_rating, f.added_at
                FROM favorites f 
                INNER JOIN movies m ON f.movie_id = m.id
                ORDER BY f.added_at DESC;
                """
            )
            return cur.fetchall()

    except psycopg.Error:
        raise HTTPException(
            status_code=500,
            detail="Database error"
        )




