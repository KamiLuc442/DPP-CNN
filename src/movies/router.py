from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .crud import *
from .schemas import *
from ..database import get_session

router = APIRouter(prefix="/movies", tags=["movies"])


@router.get("/", response_model=list[MovieSchema])
def read_movies(session: Session = Depends(get_session)):
    return get_movies(session)


@router.get("/{movie_id}", response_model=MovieSchema)
def read_movie(movie_id: int, session: Session = Depends(get_session)):
    movie = get_movie(session, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@router.post("/", response_model=MovieSchema)
def create_movie_endpoint(movie: MovieCreate, session: Session = Depends(get_session)):
    return create_movie(session, movie.title, movie.genres)


@router.put("/{movie_id}", response_model=MovieSchema)
def update_movie_endpoint(movie_id: int, movie_data: MovieUpdate, session: Session = Depends(get_session)):
    movie = get_movie(session, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return update_movie(session, movie, title=movie_data.title, genres=movie_data.genres)


@router.delete("/{movie_id}")
def delete_movie_endpoint(movie_id: int, session: Session = Depends(get_session)):
    movie = get_movie(session, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    delete_movie(session, movie)
    return {"status": "success", "message": f"Movie {movie_id} deleted"}
