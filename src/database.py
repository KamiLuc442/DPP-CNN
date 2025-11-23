import csv
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, Movie, Link, Rating, Tag


engine = create_engine('sqlite:///movies.db', echo=False)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


DATA_DIR = Path(__file__).parent.parent / "files"


def load_movies_from_csv():
    movies_file = DATA_DIR / "movies.csv"
    movies = []
    with open(movies_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies.append(
                Movie(
                    id=int(row['movieId']),
                    title=row['title'],
                    genres=row['genres']
                )
            )
    session.add_all(movies)
    session.commit()


def load_links_from_csv():
    links_file = DATA_DIR / "links.csv"
    links = []
    with open(links_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            links.append(
                Link(
                    movieId=int(row['movieId']),
                    imdbId=row['imdbId'],
                    tmdbId=row['tmdbId']
                )
            )
    session.add_all(links)
    session.commit()


def load_ratings_from_csv():
    ratings_file = DATA_DIR / "ratings.csv"
    ratings = []
    with open(ratings_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ratings.append(
                Rating(
                    userId=int(row['userId']),
                    movieId=int(row['movieId']),
                    rating=float(row['rating']),
                    timestamp=row['timestamp']
                )
            )
    session.add_all(ratings)
    session.commit()


def load_tags_from_csv():
    tags_file = DATA_DIR / "tags.csv"
    tags = []
    with open(tags_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            tags.append(
                Tag(
                    userId=int(row['userId']),
                    movieId=int(row['movieId']),
                    tag=row['tag'],
                    timestamp=row['timestamp']
                )
            )
    session.add_all(tags)
    session.commit()


def initialize_database():
    if session.query(Movie).count() == 0:
        print("Loading data from files...")
        load_movies_from_csv()
        load_links_from_csv()
        load_ratings_from_csv()
        load_tags_from_csv()
    else:
        print("Data already loaded.")


initialize_database()
