from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.api_schemas.get_post_schema import PostSchema
from app.models.post import PostTable


class PostRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_post(self, post_id):
        if post := self.db.query(PostTable).filter(PostTable.id == post_id).first():
            return post
        return None

    def create_post(self, post):
        return {"status": "created", "post": post}

    def update_post(self, post_id, post):
        return {"status": "updated", "post": post}

    def delete_post(self, post_id):
        return {"status": "deleted", "post_id": post_id}
