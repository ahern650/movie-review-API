from fastapi import APIRouter, HTTPException

from services.omdb_service import fetch_movie, format_movie
from models.movie import Movie

router = APIRouter()

@router.get("/movie/{movie_name}", response_model=Movie)
def get_movie(movie_name: str):
    raw_data = fetch_movie(movie_name)

    if raw_data.get("Response") == "False":
        raise HTTPException(
            status_code=404,
            detail="Movie not found" )

    return format_movie(raw_data)
