from pydantic import BaseModel
from typing import Optional


class TagBase(BaseModel):
    userId: int
    movieId: int
    tag: Optional[str] = None
    timestamp: Optional[str] = None


class TagSchema(TagBase):
    id: int

    class Config:
        orm_mode = True


class TagCreate(TagBase):
    pass


class TagUpdate(BaseModel):
    tag: Optional[str] = None
    timestamp: Optional[str] = None
