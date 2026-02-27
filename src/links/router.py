from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .crud import *
from .schemas import *
from ..database import get_session
from ..auth.utils import get_current_user

router = APIRouter(prefix="/links", tags=["links"])


@router.get("/", response_model=list[LinkSchema])
def read_links(session: Session = Depends(get_session), current_user: dict = Depends(get_current_user)):
    return get_links(session)


@router.get("/{movie_id}", response_model=LinkSchema)
def read_link(movie_id: int, session: Session = Depends(get_session), current_user: dict = Depends(get_current_user)):
    link = get_link(session, movie_id)
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    return link


@router.post("/", response_model=LinkSchema)
def create_link_endpoint(movieId: int, imdbId: str = None, tmdbId: str = None, session: Session = Depends(get_session), current_user: dict = Depends(get_current_user)):
    return create_link(session, movieId, imdbId, tmdbId)


@router.put("/{movie_id}", response_model=LinkSchema)
def update_link_endpoint(movie_id: int, imdbId: str = None, tmdbId: str = None, session: Session = Depends(get_session), current_user: dict = Depends(get_current_user)):
    link = get_link(session, movie_id)
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    return update_link(session, link, imdbId, tmdbId)


@router.delete("/{movie_id}")
def delete_link_endpoint(movie_id: int, session: Session = Depends(get_session), current_user: dict = Depends(get_current_user)):
    link = get_link(session, movie_id)
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    delete_link(session, link)
    return {"status": "success", "message": f"Link for movie {movie_id} deleted"}
