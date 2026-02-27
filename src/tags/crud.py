from sqlalchemy.orm import Session
from ..models import Tag

def get_tags(session: Session):
    return session.query(Tag).all()


def get_tag(tag_id: int, session: Session):
    return session.query(Tag).filter(Tag.id == tag_id).first()


def create_tag(userId: int, movieId: int, session: Session, tag: str = None, timestamp: str = None):
    t = Tag(userId=userId, movieId=movieId, tag=tag, timestamp=timestamp)
    session.add(t)
    session.commit()
    session.refresh(t)
    return t


def update_tag(tag_obj, session: Session, tag: str = None, timestamp: str = None):
    if tag is not None:
        tag_obj.tag = tag
    if timestamp is not None:
        tag_obj.timestamp = timestamp
    session.commit()
    session.refresh(tag_obj)
    return tag_obj


def delete_tag(tag_obj, session: Session):
    session.delete(tag_obj)
    session.commit()
