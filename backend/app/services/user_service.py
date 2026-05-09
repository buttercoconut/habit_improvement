from sqlalchemy.orm import Session
from ..models.db_models import User, Goal
from ..models.user import UserCreate
from ..models.goal import GoalCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_users(self):
        return self.db.query(User).all()

    def create_user(self, user_in: UserCreate):
        hashed_password = pwd_context.hash(user_in.password)
        db_user = User(email=user_in.email, full_name=user_in.full_name, hashed_password=hashed_password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

class GoalService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_goals(self):
        return self.db.query(Goal).all()

    def get_goal(self, goal_id: int):
        return self.db.query(Goal).filter(Goal.id == goal_id).first()

    def create_goal(self, goal_in: GoalCreate):
        db_goal = Goal(**goal_in.dict())
        self.db.add(db_goal)
        self.db.commit()
        self.db.refresh(db_goal)
        return db_goal

    def calculate_completion(self, goal: Goal):
        # Simple completion: progress field already represents completion
        return goal.progress

    def recommend_content(self, user_id: int):
        # Placeholder for collaborative/content-based filtering
        return ["Sample content 1", "Sample content 2"]
