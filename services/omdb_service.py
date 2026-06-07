import requests

api_key = "d12cfda7"

# fetch movie data
def fetch_movie(movie_name):
    url = f"https://www.omdbapi.com/?t={movie_name}&apikey={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()

        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return {"Response": "False"}

# format function
def format_movie(raw_data):
    return {
        "title": raw_data.get("Title", "N/A"),
        "year": raw_data.get("Year", "N/A"),
        "genre": raw_data.get("Genre", "N/A"),
        "plot": raw_data.get("Plot", "No summary available."),
        "imdb_rating": raw_data.get("imdbRating", "N/A"),
        "ratings": raw_data.get("Ratings", [])
    }