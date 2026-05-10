from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..models.user import User, UserCreate
from ..services.user_service import UserService
from ..dependencies import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return UserService.create_user(db, user)

@router.get("/", response_model=List[User])
def list_users(db: Session = Depends(get_db)):
    return UserService.get_all_users(db)
