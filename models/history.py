from pydantic import BaseModel
from datetime import datetime

class History(BaseModel):
    movie_title: str
    searched_at: datetime


