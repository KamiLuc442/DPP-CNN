from pydantic import BaseModel
from typing import Optional


class MovieBase(BaseModel):
    title: str
    genres: Optional[str] = None


class MovieCreate(MovieBase):
    pass


class MovieUpdate(BaseModel):
    title: Optional[str] = None
    genres: Optional[str] = None


class MovieSchema(MovieBase):
    id: int

    class Config:
        orm_mode = True
