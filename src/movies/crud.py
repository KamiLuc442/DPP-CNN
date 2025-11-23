from ..models import Movie


def get_movies(session):
    return session.query(Movie).all()


def get_movie(session, movie_id: int):
    return session.query(Movie).filter(Movie.id == movie_id).first()


def create_movie(session, title: str, genres: str):
    movie = Movie(title=title, genres=genres)
    session.add(movie)
    session.commit()
    session.refresh(movie)
    return movie


def update_movie(session, movie, title=None, genres=None):
    if title is not None:
        movie.title = title
    if genres is not None:
        movie.genres = genres
    session.commit()
    session.refresh(movie)
    return movie


def delete_movie(session, movie):
    session.delete(movie)
    session.commit()
