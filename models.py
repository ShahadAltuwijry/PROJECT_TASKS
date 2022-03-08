from database import Base
from sqlalchemy import Column, Integer, String, Date, Boolean


class Tasks(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    isComplete = Column(Boolean, default=False)
    deadline = Column(Date, index=True)
    