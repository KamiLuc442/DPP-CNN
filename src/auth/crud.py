from sqlalchemy.orm import Session
from typing import List
from ..models import User
from .utils import get_password_hash, verify_password


def get_user_by_login(session: Session, login: str):
    return session.query(User).filter(User.login == login).first()


def get_user_by_id(session: Session, user_id: int):
    return session.query(User).filter(User.id == user_id).first()


def create_user(session: Session, login: str, password: str, roles: List[str] = None):
    if roles is None:
        roles = ['ROLE_USER']
    
    hashed_password = get_password_hash(password)
    user = User(
        login=login,
        hashed_password=hashed_password,
        roles=roles
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def authenticate_user(session: Session, login: str, password: str):
    user = get_user_by_login(session, login)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user
