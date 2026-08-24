import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.routes.auth import router as auth_router
from app.routes.problems import router as problems_router
from app.database import Base, engine
from app.models import User, Problem, Submission
from app.routes.submissions import router as submissions_router


class HealthResponse(BaseModel):
    message: str


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CodeForge API",
    description="Backend API for an online coding platform",
    version="1.0.0",
)

frontend_url = os.getenv("FRONTEND_URL", "http://localhost:3000")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_url],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(problems_router)
app.include_router(submissions_router)


@app.get("/", response_model=HealthResponse)
def root():
    return {"message": "CodeForge: CodeForge API is running"}