from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject
from app.services.get_post_service import GetPostService
from app.core.container import Container
from app.api_schemas.get_post_schema import GetPostRequest, GetPostResponse

router = APIRouter()


@router.get("/posts/{post_id}")
@inject
def get_post(
    get_post_request: GetPostRequest = Depends(),
    service: GetPostService = Depends(Provide[Container.get_post_service]),
) -> GetPostResponse:
    if post := service.get_post(get_post_request.post_id):
        return GetPostResponse(result=True, post=post)
    return GetPostResponse(result=False, post=None)
