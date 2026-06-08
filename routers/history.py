from fastapi import APIRouter, HTTPException, Depends
import psycopg
from database.connection import get_db_connection
from models.history import History

router = APIRouter(prefix="/history", tags=["Search History"])

@router.get("/", response_model=list[History])
def get_search_history(conn: psycopg.Connection = Depends(get_db_connection)):
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT movie_title, searched_at
                FROM search_history
                ORDER BY searched_at DESC LIMIT 10
                """
            )
            return cur.fetchall()
    except psycopg.Error:
        raise HTTPException(
            status_code=400,
            detail="Database error"
        )