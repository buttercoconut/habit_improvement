from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..models.goal import Goal, GoalCreate
from ..services.goal_service import GoalService
from ..dependencies import get_db

router = APIRouter(prefix="/goals", tags=["goals"])

@router.post("/", response_model=Goal)
def create_goal(goal: GoalCreate, db: Session = Depends(get_db)):
    return GoalService.create_goal(db, goal)

@router.get("/", response_model=List[Goal])
def list_goals(user_id: int, db: Session = Depends(get_db)):
    return GoalService.get_goals_by_user(db, user_id)
