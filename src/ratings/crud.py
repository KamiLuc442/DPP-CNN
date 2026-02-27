from sqlalchemy.orm import Session
from ..models import Rating


def get_ratings(session: Session):
    return session.query(Rating).all()


def get_rating(session: Session, rating_id: int):
    return session.query(Rating).filter(Rating.id == rating_id).first()


def create_rating(session: Session, userId: int, movieId: int, rating: float = None, timestamp: str = None):
    r = Rating(userId=userId, movieId=movieId, rating=rating, timestamp=timestamp)
    session.add(r)
    session.commit()
    session.refresh(r)
    return r


def update_rating(session: Session, rating_obj, rating: float = None, timestamp: str = None):
    if rating is not None:
        rating_obj.rating = rating
    if timestamp is not None:
        rating_obj.timestamp = timestamp
    session.commit()
    session.refresh(rating_obj)
    return rating_obj


def delete_rating(session: Session, rating_obj):
    session.delete(rating_obj)
    session.commit()
