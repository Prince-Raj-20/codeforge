# app/schemas/test_case.py

from pydantic import BaseModel


class PublicTestCaseResponse(BaseModel):
    id: int
    input_data: str
    expected_output: str

    class Config:
        from_attributes = True