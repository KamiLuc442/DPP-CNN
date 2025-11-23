from ..models import Link

def get_links(session):
    return session.query(Link).all()


def get_link(session, movie_id: int):
    return session.query(Link).filter(Link.movieId == movie_id).first()


def create_link(session, movieId: int, imdbId: str = None, tmdbId: str = None):
    link = Link(movieId=movieId, imdbId=imdbId, tmdbId=tmdbId)
    session.add(link)
    session.commit()
    session.refresh(link)
    return link


def update_link(session, link, imdbId: str = None, tmdbId: str = None):
    if imdbId is not None:
        link.imdbId = imdbId
    if tmdbId is not None:
        link.tmdbId = tmdbId
    session.commit()
    session.refresh(link)
    return link


def delete_link(session, link):
    session.delete(link)
    session.commit()
