from fastapi import FastAPI
from app.routers import users, tasks
from app.database import engine, Base
import app.models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager API",
    description="A production-ready task management system",
    version="1.0.0"
)

app.include_router(users.router)
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "Task Manager API is running!"}