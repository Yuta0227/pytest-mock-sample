from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from app.core.db_connect import Base


class UserTable(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    created_at = Column(DateTime)
    is_login = Column(Boolean)

    posts = relationship("PostTable", back_populates="user")
