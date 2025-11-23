from fastapi import FastAPI
from .movies import load_movies, load_links, load_ratings, load_tags

app = FastAPI()


@app.get("/")
async def root():
    return {"hello": "world"}


@app.get("/movies")
async def get_movies():
    movies = load_movies()
    return [movie.__dict__ for movie in movies]


@app.get("/links")
async def get_links():
    links = load_links()
    return [link.__dict__ for link in links]


@app.get("/ratings")
async def get_ratings():
    ratings = load_ratings()
    return [rating.__dict__ for rating in ratings]


@app.get("/tags")
async def get_tags():
    tags = load_tags()
    return [tag.__dict__ for tag in tags]
