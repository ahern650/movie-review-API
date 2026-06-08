from pydantic import BaseModel
from datetime import datetime

class Favorite(BaseModel):
    id: int
    title: str
    year: str
    genre: str
    plot: str
    imdb_rating: str
    added_at: datetime