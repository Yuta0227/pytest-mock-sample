# app/models/post.py
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from app.core.db_connect import Base


class PostTable(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    description = Column(String(255), index=True)
    user_id = Column(ForeignKey("users.id"))
    is_private = Column(Boolean)

    user = relationship("UserTable", back_populates="posts")

    @classmethod
    def test_public_post_data(cls):
        return cls(id=1, title="test", description="test", user_id=1, is_private=False)
