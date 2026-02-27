from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .crud import authenticate_user, create_user, get_user_by_login
from .schemas import LoginRequest, LoginResponse, UserCreate, UserResponse
from .utils import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES, require_admin, get_current_user
from ..database import get_session

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user_data: UserCreate, session: Session = Depends(get_session)):
    if get_user_by_login(session, user_data.login):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Login already registered"
        )
    
    user = create_user(
        session=session,
        login=user_data.login,
        password=user_data.password,
        roles=user_data.roles
    )
    
    return UserResponse(
        id=user.id,
        login=user.login,
        roles=user.roles
    )


@router.post("/login", response_model=LoginResponse)
def login(login_data: LoginRequest, session: Session = Depends(get_session)):
    user = authenticate_user(session, login_data.login, login_data.password)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect login or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.login, "user_id": user.id, "roles": user.roles},
        expires_delta=access_token_expires
    )
    
    return LoginResponse(
        access_token=access_token,
        token_type="bearer",
        user=UserResponse(
            id=user.id,
            login=user.login,
            roles=user.roles
        )
    )


@router.get("/user_details", response_model=UserResponse)
def get_user_details(current_user: dict = Depends(get_current_user)):
    return UserResponse(
        id=current_user.get("user_id"),
        login=current_user.get("sub"),
        roles=current_user.get("roles", [])
    )


users_router = APIRouter(tags=["users"])


@users_router.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_new_user(
    user_data: UserCreate, 
    session: Session = Depends(get_session),
    current_user: dict = Depends(require_admin)
):
    if get_user_by_login(session, user_data.login):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Login already registered"
        )
    
    user = create_user(
        session=session,
        login=user_data.login,
        password=user_data.password,
        roles=user_data.roles
    )
    
    return UserResponse(
        id=user.id,
        login=user.login,
        roles=user.roles
    )
