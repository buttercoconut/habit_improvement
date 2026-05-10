from sqlalchemy.orm import Session
from ..models.goal import Goal, GoalCreate

class GoalService:
    @staticmethod
    def create_goal(db: Session, goal_in: GoalCreate) -> Goal:
        goal = Goal(**goal_in.dict())
        db.add(goal)
        db.commit()
        db.refresh(goal)
        return goal

    @staticmethod
    def get_goals_by_user(db: Session, user_id: int):
        return db.query(Goal).filter(Goal.user_id == user_id).all()
