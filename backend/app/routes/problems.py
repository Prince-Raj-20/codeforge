# app/routes/problems.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Problem, TestCase
from app.schemas.problem import ProblemResponse
from app.schemas.test_case import PublicTestCaseResponse


router = APIRouter(
    prefix="/problems",
    tags=["Problems"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[ProblemResponse])
def get_problems(
    db: Session = Depends(get_db)
):
    problems = (
        db.query(Problem)
        .order_by(Problem.id)
        .all()
    )

    return problems


@router.get("/{problem_id}", response_model=ProblemResponse)
def get_problem(
    problem_id: int,
    db: Session = Depends(get_db)
):
    problem = (
        db.query(Problem)
        .filter(Problem.id == problem_id)
        .first()
    )

    if not problem:
        raise HTTPException(
            status_code=404,
            detail="Problem not found"
        )

    sample_test_case = (
        db.query(TestCase)
        .filter(
            TestCase.problem_id == problem_id,
            TestCase.is_public == True
        )
        .order_by(TestCase.id)
        .first()
    )

    return {
        "id": problem.id,
        "title": problem.title,
        "description": problem.description,
        "difficulty": problem.difficulty,
        "topic": problem.topic,
        "input_format": problem.input_format,
        "output_format": problem.output_format,
        "constraints": problem.constraints,
        "sample_input": (
            sample_test_case.input_data
            if sample_test_case else ""
        ),
        "sample_output": (
            sample_test_case.expected_output
            if sample_test_case else ""
        )
    }

@router.get(
    "/{problem_id}/test-cases",
    response_model=list[PublicTestCaseResponse]
)
def get_public_test_cases(
    problem_id: int,
    db: Session = Depends(get_db)
):
    problem = (
        db.query(Problem)
        .filter(Problem.id == problem_id)
        .first()
    )

    if not problem:
        raise HTTPException(
            status_code=404,
            detail="Problem not found"
        )

    test_cases = (
        db.query(TestCase)
        .filter(
            TestCase.problem_id == problem_id,
            TestCase.is_public == True
        )
        .order_by(TestCase.id)
        .all()
    )

    return test_cases