from .database import session
from .models import Movie, Link, Rating, Tag

def load_movies():
    return session.query(Movie).all()

def load_links():
    return session.query(Link).all()

def load_ratings():
    return session.query(Rating).all()

def load_tags():
    return session.query(Tag).all()
