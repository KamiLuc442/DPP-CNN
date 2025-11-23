from fastapi import FastAPI
from movies import load_movies

app = FastAPI()


@app.get("/")
async def root():
    return {"hello": "world"}


@app.get("/movies")
async def get_movies():
    movies = load_movies()
    return [movie.__dict__ for movie in movies]
