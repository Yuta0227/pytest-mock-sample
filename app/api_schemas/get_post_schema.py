from typing import Optional

from pydantic import BaseModel


class GetPostSchema(BaseModel):
    title: str
    description: str


# class PostInDBBase(GetPostSchema):
#     id: int
#     class Config:
#         orm_mode = True


class GetPostRequest(BaseModel):
    post_id: int
    user_id: int


class GetPostResponse(BaseModel):
    result: bool
    post: Optional[GetPostSchema] = None
