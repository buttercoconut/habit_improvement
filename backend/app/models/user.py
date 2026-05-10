from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional

class UserBase(BaseModel):
    email: str
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True

class GoalBase(BaseModel):
    title: str
    description: Optional[str] = None
    target_date: datetime

class GoalCreate(GoalBase):
    pass

class Goal(GoalBase):
    id: int
    user_id: int
    progress: float = 0.0
    created_at: datetime
    class Config:
        orm_mode = True
