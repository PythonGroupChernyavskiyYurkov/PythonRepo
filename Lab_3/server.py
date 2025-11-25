from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Movie(BaseModel):
    id: int
    title: str
    year: int
    genre: str

movies = []
next_id = 1

@app.get("/")
def home():
    return {"message": "Добро пожаловать в наш кинотеатр!"}

@app.get("/movies")
def get_all_movies():
    return {"movies": movies}

@app.get("/movies/{movie_id}")
def get_one_movie(movie_id: int):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    return {"error": "Фильм не найден"}

@app.post("/movies")
def add_movie(movie: Movie):
    global next_id
    new_movie = {
        "id": next_id,
        "title": movie.title,
        "year": movie.year,
        "genre": movie.genre
    }
    movies.append(new_movie)
    next_id += 1
    return {"message": "Фильм добавлен", "movie": new_movie}

@app.put("/movies/{movie_id}")
def update_movie(movie_id: int, updated_movie: Movie):
    for i in range(len(movies)):
        if movies[i]["id"] == movie_id:
            movies[i]["title"] = updated_movie.title
            movies[i]["year"] = updated_movie.year
            movies[i]["genre"] = updated_movie.genre
            return {"message": "Фильм обновлен", "movie": movies[i]}
    return {"error": "Фильм не найден"}

@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    for i in range(len(movies)):
        if movies[i]["id"] == movie_id:
            deleted_movie = movies.pop(i)
            return {"message": "Фильм удален", "movie": deleted_movie}
    return {"error": "Фильм не найден"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    