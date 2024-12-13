# app/models/post.py
from sqlalchemy import Column, Integer, String

from app.core.db_connect import Base


class PostTable(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
