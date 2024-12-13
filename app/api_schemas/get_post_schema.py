from pydantic import BaseModel
from typing import Optional
from app.repositories.post_repository import Post


class GetPostRequest(BaseModel):
    post_id: int


class GetPostResponse(BaseModel):
    result: bool
    post: Optional[Post] = None
