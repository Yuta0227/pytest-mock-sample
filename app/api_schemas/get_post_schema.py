from typing import Optional

from pydantic import BaseModel


class PostSchema(BaseModel):
    id: int
    title: str
    description: str


class GetPostRequest(BaseModel):
    post_id: int


class GetPostResponse(BaseModel):
    result: bool
    post: Optional[PostSchema] = None
