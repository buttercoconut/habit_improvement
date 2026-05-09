from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..models.goal import Goal, GoalCreate
from ..services.goal_service import GoalService
from ..dependencies import get_db

router = APIRouter()

@router.post("/", response_model=Goal, status_code=status.HTTP_201_CREATED)
async def create_goal(goal_in: GoalCreate, db: Session = Depends(get_db)):
    service = GoalService(db)
    goal = service.create_goal(goal_in)
    return goal

@router.get("/", response_model=List[Goal])
async def list_goals(db: Session = Depends(get_db)):
    service = GoalService(db)
    return service.get_all_goals()

@router.get("/{goal_id}", response_model=Goal)
async def get_goal(goal_id: int, db: Session = Depends(get_db)):
    service = GoalService(db)
    goal = service.get_goal(goal_id)
    if not goal:
        raise HTTPException(status_code=404, detail="Goal not found")
    return goal
