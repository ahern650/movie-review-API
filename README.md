# 🎬 Movie Review API

A backend movie review API built with FastAPI and the OMDb API.

This project allows users to search for movie information including:

- title  
- genre  
- plot summary  
- IMDb rating  
- audience ratings  

The API retrieves and formats movie data into clean JSON responses using FastAPI and Pydantic models.

---

## ✨ Features

- FastAPI backend  
- RESTful API endpoints  
- Pydantic response models (Movie, Favorites, History)  
- OMDb API integration  
- Automatic Swagger documentation (`/docs`)  
- HTTP error handling  
- Modular project structure  
- User favorites system (add/remove movies)  
- Search history tracking (recent queries)  

---

## 📊 Data Models

The API uses Pydantic models to ensure structured and validated responses:

- **Movie Model** → Standard movie data returned from OMDb  
- **Favorite Model** → Stores user-saved favorite movies  
- **History Model** → Tracks previously searched movies  

These models ensure consistent API responses and improve type safety across the application.

---

## 🛠️ Technologies Used

- Python  
- FastAPI  
- Pydantic  
- Requests  
- Uvicorn  
- OMDb API  

---

## 📁 Project Structure

```text
movie-review-api/
│
├── models/
│   └── movie.py
│
├── routers/
│   ├── movies.py
│   ├── favorites.py
│   └── history.py
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
cd  movie_review_api
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

## API Endpoints

Movies:
```text
GET /movie/{title} --> Get movie details
```
Favorites:
```text
POST /favorites/ --> Add movie to favorites
GET  /favorites/ --> Get all favorite movies
```
History:
```text
GET /history/ --> Retrieve search history
```

---

## Future Improvements

* Async requests with httpx
* User authentication (JWT)
* Deployment (Render / Railway / AWS)
* Frontend interface (React or Next.js)

---

## Author

Angel Adrian Hernandez
