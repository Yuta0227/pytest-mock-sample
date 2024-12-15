from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.api_schemas.get_post_schema import (GetPostRequest, GetPostResponse,
                                             GetPostSchema)
from app.core.container import Container
from app.services.get_post_service import GetPostService

router = APIRouter()


@router.get("/posts/{post_id}")
@inject
def get_post_info(
    get_post_request: GetPostRequest = Depends(),
    service: GetPostService = Depends(Provide[Container.get_post_service]),
) -> GetPostResponse:
    if post := service.get_post_info(
        get_post_request.post_id, get_post_request.user_id
    ):
        return GetPostResponse(
            result=True,
            post=GetPostSchema(title=post.title, description=post.description),
        )
    return GetPostResponse(result=False, post=None)
