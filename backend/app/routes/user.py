from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..models.user import User, UserCreate
from ..services.user_service import UserService
from ..dependencies import get_db

router = APIRouter()

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    user = service.create_user(user_in)
    return user

@router.get("/", response_model=List[User])
async def list_users(db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_all_users()
