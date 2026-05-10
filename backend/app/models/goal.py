from pydantic import BaseModel, Field
from datetime import datetime

class GoalBase(BaseModel):
    title: str
    description: str | None = None
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
