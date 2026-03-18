from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .user import Base

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    url = Column(String, nullable=False)
    status = Column(String, default="PENDING")
    result = Column(String, nullable=True)

    user = relationship("User")