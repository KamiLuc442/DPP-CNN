from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .crud import *
from .schemas import *
from ..database import get_session
from ..auth.utils import get_current_user

router = APIRouter(prefix="/ratings", tags=["ratings"])


@router.get("/", response_model=list[RatingSchema])
async def read_ratings(session: Session = Depends(get_session), current_user: dict = Depends(get_current_user)):
    return get_ratings(session)


@router.get("/{rating_id}", response_model=RatingSchema)
async def read_rating(rating_id: int, session: Session = Depends(get_session), current_user: dict = Depends(get_current_user)):
    rating = get_rating(session, rating_id)
    if not rating:
        raise HTTPException(status_code=404, detail="Rating not found")
    return rating


@router.post("/", response_model=RatingSchema)
async def create_rating_endpoint(rating: RatingCreate, session: Session = Depends(get_session), current_user: dict = Depends(get_current_user)):
    return create_rating(
        session,
        userId=rating.userId,
        movieId=rating.movieId,
        rating=rating.rating,
        timestamp=rating.timestamp
    )


@router.put("/{rating_id}", response_model=RatingSchema)
async def update_rating_endpoint(rating_id: int, rating_data: RatingUpdate, session: Session = Depends(get_session), current_user: dict = Depends(get_current_user)):
    rating = get_rating(session, rating_id)
    if not rating:
        raise HTTPException(status_code=404, detail="Rating not found")
    return update_rating(
        session,
        rating,
        rating=rating_data.rating,
        timestamp=rating_data.timestamp
    )


@router.delete("/{rating_id}")
async def delete_rating_endpoint(rating_id: int, session: Session = Depends(get_session), current_user: dict = Depends(get_current_user)):
    rating = get_rating(session, rating_id)
    if not rating:
        raise HTTPException(status_code=404, detail="Rating not found")
    delete_rating(session, rating_obj=rating)
    return {"status": "success", "message": f"Rating {rating_id} deleted"}
