# app/models/problem.py

from sqlalchemy import Column, Integer, String, Text

from app.database import Base


class Problem(Base):
    __tablename__ = "problems"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(200), nullable=False)

    description = Column(Text, nullable=False)

    difficulty = Column(String(20), nullable=False)

    topic = Column(String(100), nullable=True)

    input_format = Column(Text, nullable=False)

    output_format = Column(Text, nullable=False)

    constraints = Column(Text, nullable=False)

    sample_input = Column(Text, nullable=False)

    sample_output = Column(Text, nullable=False)

    time_limit = Column(Integer, nullable=False, default=3)