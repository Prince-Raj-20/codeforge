from app.services.weakness_analyzer import analyze_weakness
from app.services.recommender import get_recommendations
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from app.database import SessionLocal
from app.dependencies import get_current_user
from app.models import (
    Submission,
    Problem,
    User,
    TestCase
)
from app.schemas import SubmissionCreate
from app.services.judge import judge_submission


router = APIRouter(
    prefix="/submissions",
    tags=["Submissions"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_submission(
    submission: SubmissionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Check that the problem exists
    problem = (
        db.query(Problem)
        .filter(Problem.id == submission.problem_id)
        .first()
    )

    if not problem:
        raise HTTPException(
            status_code=404,
            detail="Problem not found"
        )

    # Get all test cases.
    # This includes hidden test cases.
    test_cases = (
        db.query(TestCase)
        .filter(
            TestCase.problem_id == submission.problem_id
        )
        .order_by(TestCase.id)
        .all()
    )

    if not test_cases:
        raise HTTPException(
            status_code=400,
            detail="No test cases available for this problem"
        )

    # Run the submission through the judge
    result = judge_submission(
        code=submission.code,
        test_cases=test_cases,
        time_limit=problem.time_limit
    )

    # Store the submission and judging result
    new_submission = Submission(
        user_id=current_user.id,
        problem_id=submission.problem_id,
        code=submission.code,
        language=submission.language,
        status=result["status"],
        output=result["output"],
        error=result["error"],
        execution_time=result["execution_time"],
        solve_time=submission.solve_time
    )

    db.add(new_submission)
    db.commit()
    db.refresh(new_submission)

    return {
        "message": "Submission judged successfully",
        "submission_id": new_submission.id,
        "user_id": current_user.id,
        "problem_id": new_submission.problem_id,
        "status": new_submission.status,
        "output": new_submission.output,
        "error": new_submission.error,
        "execution_time": new_submission.execution_time,
        "solve_time": new_submission.solve_time
    }


@router.get("/")
def get_submissions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    submissions = (
        db.query(Submission)
        .filter(
            Submission.user_id == current_user.id
        )
        .order_by(Submission.id.desc())
        .all()
    )

    return [
        {
            "id": submission.id,
            "problem_id": submission.problem_id,
            "language": submission.language,
            "status": submission.status,
            "solve_time": submission.solve_time,
            "execution_time": submission.execution_time
        }
        for submission in submissions
    ]


@router.get("/weaknesses")
def get_weaknesses(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    submissions = (
        db.query(Submission)
        .filter(Submission.user_id == current_user.id)
        .all()
    )

    return analyze_weakness(submissions)

@router.get("/recommendations")
def get_user_recommendations(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_recommendations(
        db=db,
        user_id=current_user.id,
        limit=5
    )