from pydantic import BaseModel
from typing import List

class Rating(BaseModel):
    Source: str
    Value: str

class Movie(BaseModel):
    title: str
    year: str
    genre: str
    plot: str
    imdb_rating: str
    ratings: List[Rating]