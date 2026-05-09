from fastapi import FastAPI
from .routes import user, goal

app = FastAPI(title="Habit Improvement API")

app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(goal.router, prefix="/goals", tags=["goals"])

# Health check
@app.get("/health")
async def health_check():
    return {"status": "ok"}
