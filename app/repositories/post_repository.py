from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.models.post import PostTable
from app.models.user import UserTable


class PostRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_post(self, post_id) -> PostTable:
        return (
            self.db.query(PostTable)
            .join(UserTable, UserTable.id == PostTable.user_id)
            .filter(PostTable.id == post_id)
            .first()
        )
