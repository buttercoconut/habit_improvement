from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class GoalBase(BaseModel):
    title: str
    description: Optional[str] = None
    target_date: datetime

class GoalCreate(GoalBase):
    user_id: int

class Goal(GoalBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    progress: float = 0.0  # 0.0 to 1.0

    class Config:
        orm_mode = True
