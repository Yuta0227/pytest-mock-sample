from unittest.mock import MagicMock

import pytest
import requests

from app.api_schemas.get_post_schema import (GetPostRequest, GetPostResponse,
                                             GetPostSchema)
from app.controllers.get_post_controller import get_post_info
from app.models.post import PostTable
from app.models.user import UserTable
from tests.base_test import BaseTest


@pytest.fixture()
def mock_get_post_service():
    return MagicMock()


def test_get_post_succeeds(mock_get_post_service):
    mock_get_post_service.get_post_info.return_value = PostTable.test_public_post_data()

    request = GetPostRequest(post_id=1, user_id=1)
    response = get_post_info(get_post_request=request, service=mock_get_post_service)
    assert response == GetPostResponse(
        result=True,
        post=GetPostSchema(
            title=PostTable.test_public_post_data().title,
            description=PostTable.test_public_post_data().description,
        ),
    )


def test_get_post_fails(mock_get_post_service):
    mock_get_post_service.get_post_info.return_value = None

    request = GetPostRequest(post_id=1, user_id=1)
    response = get_post_info(get_post_request=request, service=mock_get_post_service)
    assert response == GetPostResponse(result=False, post=None)


class TestGetPostController(BaseTest):
    @classmethod
    def _insert_data(cls):
        cls.db.add_all(
            [UserTable.test_not_login_user_data(), PostTable.test_public_post_data()]
        )
        cls.db.commit()

    @classmethod
    def test_e2e(cls):
        post_id = str(PostTable.test_public_post_data().id)
        user_id = str(UserTable.test_not_login_user_data().id)
        response = cls.client.get(
            "/posts/" + post_id, params={"post_id": post_id, "user_id": user_id}
        )
        assert response.status_code == 200
        assert response.json() == {
            "result": True,
            "post": {
                "title": PostTable.test_public_post_data().title,
                "description": PostTable.test_public_post_data().description,
            },
        }
