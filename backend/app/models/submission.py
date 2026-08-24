from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    problem_id = Column(
        Integer,
        ForeignKey("problems.id"),
        nullable=False
    )

    code = Column(Text, nullable=False)

    language = Column(
        String(20),
        nullable=False,
        default="cpp"
    )

    status = Column(
        String(30),
        nullable=False
    )

    output = Column(Text, nullable=True)

    error = Column(Text, nullable=True)

    execution_time = Column(
        Integer,
        nullable=True
    )

    solve_time = Column(
        Integer,
        nullable=True
    )

    problem = relationship("Problem")