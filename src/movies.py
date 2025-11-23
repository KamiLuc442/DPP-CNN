import csv
from pathlib import Path


class Movie:
    def __init__(self, id: str, title: str, genres: str):
        self.id = id
        self.title = title
        self.genres = genres


def load_movies():
    """Wczytuje filmy z pliku CSV i zwraca listę obiektów Movie"""
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

