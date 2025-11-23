import csv
from pathlib import Path


class Movie:
    def __init__(self, id: str, title: str, genres: str):
        self.id = id
        self.title = title
        self.genres = genres


class Link:
    def __init__(self, movieId: str, imdbId: str, tmdbId: str):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId


class Rating:
    def __init__(self, userId: str, movieId: str, rating: str, timestamp: str):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp


class Tag:
    def __init__(self, userId: str, movieId: str, tag: str, timestamp: str):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp


def load_movies():
    movies = []
    movies_file = Path("files/movies.csv")
    
    with open(movies_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            movie = Movie(
                id=row['movieId'],
                title=row['title'],
                genres=row['genres']
            )
            movies.append(movie)
    
    return movies


def load_links():
    links = []
    links_file = Path("files/links.csv")
    
    with open(links_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            link = Link(
                movieId=row['movieId'],
                imdbId=row['imdbId'],
                tmdbId=row['tmdbId']
            )
            links.append(link)
    
    return links


def load_ratings():
    ratings = []
    ratings_file = Path("files/ratings.csv")
    
    with open(ratings_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            rating = Rating(
                userId=row['userId'],
                movieId=row['movieId'],
                rating=row['rating'],
                timestamp=row['timestamp']
            )
            ratings.append(rating)
    
    return ratings


def load_tags():
    tags = []
    tags_file = Path("files/tags.csv")
    
    with open(tags_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            tag = Tag(
                userId=row['userId'],
                movieId=row['movieId'],
                tag=row['tag'],
                timestamp=row['timestamp']
            )
            tags.append(tag)
    
    return tags
