from fastapi import FastAPI
from .routes import user, goal

app = FastAPI(title="Habit Improvement API")

app.include_router(user.router)
app.include_router(goal.router)
