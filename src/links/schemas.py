from pydantic import BaseModel
from typing import Optional


class LinkBase(BaseModel):
    imdbId: Optional[str] = None
    tmdbId: Optional[str] = None


class LinkSchema(LinkBase):
    movieId: int


    class Config:
        orm_mode = True
