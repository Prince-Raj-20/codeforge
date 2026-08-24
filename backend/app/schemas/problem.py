# app/schemas/problem.py

from pydantic import BaseModel


class ProblemResponse(BaseModel):
    id: int
    title: str
    description: str
    difficulty: str
    topic: str | None = None

    input_format: str
    output_format: str
    constraints: str

    sample_input: str | None = None
    sample_output: str | None = None

    class Config:
        from_attributes = True