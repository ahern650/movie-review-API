# Movie Review API

A backend movie review API built with FastAPI and the OMDb API.

This project allows users to search for movie information including:

* title
* genre
* plot summary
* IMDb rating
* audience ratings

The API retrieves and formats movie data into clean JSON responses using FastAPI and Pydantic models.

---

## Features

* FastAPI backend
* RESTful API endpoints
* Pydantic response models
* OMDb API integration
* Automatic Swagger documentation
* HTTP error handling
* Modular project structure

---

## Technologies Used

* Python
* FastAPI
* Pydantic
* Requests
* Uvicorn
* OMDb API

---

## Project Structure

```text
movie-review-api/
│
├── models/
│   └── movie.py
│
├── routers/
│   └── movies.py
│
├── services/
│   └── omdb_service.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <your-github-repo>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
uvicorn main:app --reload
```

---

## API Documentation

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

## Example Endpoint

```text
GET /movie/interstellar
```

Example Response:

```json
{
  "title": "Interstellar",
  "year": "2014",
  "genre": "Adventure, Drama, Sci-Fi",
  "plot": "A team of explorers travel through a wormhole in space...",
  "imdb_rating": "8.7"
}
```

---

## Future Improvements

* Search endpoint
* Async requests with httpx
* Database integration
* User favorites
* Caching
* Deployment
* Frontend interface

---

## Author

Angel Adrian Hernandez
