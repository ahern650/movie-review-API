"""
Movie Review Generator | Angel Adrian Hernandez
    User inputs a movie title and the API retrieves
    relevant information such as rating, summary,
    audience scores, and IMDb ratings.
"""
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers.movies import router as movie_router

app = FastAPI()

@app.get("/")
def home():
    return RedirectResponse(url="/docs")

app.include_router(movie_router)