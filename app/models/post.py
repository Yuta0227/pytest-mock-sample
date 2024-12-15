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

    def get_columns(self):
        return [column.key for column in self.__table__.columns]
