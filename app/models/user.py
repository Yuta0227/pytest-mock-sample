from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from app.core.db_connect import Base
from app.helpers.helper import get_datetime_now_db_format


class UserTable(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    created_at = Column(DateTime)
    is_login = Column(Boolean)

    posts = relationship("PostTable", back_populates="user")

    @classmethod
    def test_not_login_user_data(cls):
        return cls(
            id=1,
            name="test",
            email="test",
            password="test@example.com",
            created_at=get_datetime_now_db_format(),
            is_login=False,
        )
