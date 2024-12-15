from unittest.mock import MagicMock

import pytest

from app.api_schemas.get_post_schema import (GetPostRequest, GetPostResponse,
                                             GetPostSchema)
from app.controllers.get_post_controller import get_post_info
from app.models.post import PostTable


@pytest.fixture()
def mock_get_post_service():
    return MagicMock()


def test_get_post_succeeds(mock_get_post_service):
    mock_get_post_service.get_post_info.return_value = PostTable(
        id=1, title="title", description="description", user_id=1, is_private=False
    )

    request = GetPostRequest(post_id=1, user_id=1)
    response = get_post_info(get_post_request=request, service=mock_get_post_service)
    assert response == GetPostResponse(
        result=True, post=GetPostSchema(title="title", description="description")
    )


def test_get_post_fails(mock_get_post_service):
    mock_get_post_service.get_post_info.return_value = None

    request = GetPostRequest(post_id=1, user_id=1)
    response = get_post_info(get_post_request=request, service=mock_get_post_service)
    assert response == GetPostResponse(result=False, post=None)
