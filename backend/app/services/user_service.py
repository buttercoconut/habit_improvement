from sqlalchemy.orm import Session
from ..models.user import User, UserCreate
from ..models.goal import Goal, GoalCreate

class UserService:
    @staticmethod
    def create_user(db: Session, user_in: UserCreate) -> User:
        user = User(email=user_in.email, full_name=user_in.full_name)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def get_all_users(db: Session):
        return db.query(User).all()

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
