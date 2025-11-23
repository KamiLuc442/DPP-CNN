from pydantic import BaseModel
from typing import Optional


class RatingBase(BaseModel):
    userId: int
    movieId: int
    rating: Optional[float] = None
    timestamp: Optional[str] = None


class RatingSchema(RatingBase):
    id: int


    class Config:
        orm_mode = True


class RatingCreate(RatingBase):
    pass


class RatingUpdate(BaseModel):
    rating: Optional[float] = None
    timestamp: Optional[str] = None
