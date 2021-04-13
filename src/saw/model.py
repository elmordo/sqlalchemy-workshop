from datetime import datetime

from saw.declarative import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship


def generate_random_color():
    return "000000"


class TaskGroup(Base):
    __tablename__ = "task_groups"
    __fillable__ = ["name", "comment", "color"]

    id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    name = Column(Text(), nullable=False)
    comment = Column(Text())
    color = Column(Text(6), nullable=False, default=generate_random_color)
    created_at = Column(DateTime(), nullable=False, default=datetime.now)


class Task(Base):
    __tablename__ = "tasks"
    __fillable__ = ["name", "comment", "completed_at"]

    id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    task_group_id = Column(Integer(), ForeignKey(TaskGroup.id, ondelete="CASCADE"))
    name = Column(Text(), nullable=False)
    comment = Column(Text())
    created_at = Column(DateTime(), nullable=False, default=datetime.now)
    completed_at = Column(DateTime())

    task_group = relationship(TaskGroup)


TaskGroup.tasks = relationship(Task)
