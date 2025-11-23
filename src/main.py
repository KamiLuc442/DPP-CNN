from fastapi import FastAPI
from .movies import load_movies, load_links, load_ratings, load_tags

app = FastAPI()


def orm_to_dict(obj):
    return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}


@app.get("/")
async def root():
    return {"hello": "world"}


@app.get("/movies")
async def get_movies():
    movies = load_movies()
    return [orm_to_dict(movie) for movie in movies]


@app.get("/links")
async def get_links():
    links = load_links()
    return [orm_to_dict(link) for link in links]


@app.get("/ratings")
async def get_ratings():
    ratings = load_ratings()
    return [orm_to_dict(rating) for rating in ratings]


@app.get("/tags")
async def get_tags():
    tags = load_tags()
    return [orm_to_dict(tag) for tag in tags]
