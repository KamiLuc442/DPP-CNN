from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .crud import *
from .schemas import *
from ..database import get_session
from ..auth.utils import get_current_user

router = APIRouter(prefix="/tags", tags=["tags"])


@router.get("/", response_model=list[TagSchema])
async def read_tags(session: Session = Depends(get_session), current_user: dict = Depends(get_current_user)):
    return get_tags(session)


@router.get("/{tag_id}", response_model=TagSchema)
async def read_tag(tag_id: int, session: Session = Depends(get_session), current_user: dict = Depends(get_current_user)):
    tag = get_tag(tag_id, session)
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    return tag


@router.post("/", response_model=TagSchema)
async def create_tag_endpoint(tag: TagCreate, session: Session = Depends(get_session), current_user: dict = Depends(get_current_user)):
    return create_tag(
        userId=tag.userId,
        movieId=tag.movieId,
        session=session,
        tag=tag.tag,
        timestamp=tag.timestamp
    )


@router.put("/{tag_id}", response_model=TagSchema)
async def update_tag_endpoint(tag_id: int, tag_data: TagUpdate, session: Session = Depends(get_session), current_user: dict = Depends(get_current_user)):
    tag = get_tag(tag_id, session)
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    return update_tag(
        tag,
        session=session,
        tag=tag_data.tag,
        timestamp=tag_data.timestamp
    )


@router.delete("/{tag_id}")
async def delete_tag_endpoint(tag_id: int, session: Session = Depends(get_session), current_user: dict = Depends(get_current_user)):
    tag = get_tag(tag_id, session)
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    delete_tag(tag, session)
    return {"status": "success", "message": f"Tag {tag_id} deleted"}
