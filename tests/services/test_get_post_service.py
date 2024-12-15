from datetime import datetime
from unittest.mock import MagicMock

import pytest

from app.models.post import PostTable
from app.models.user import UserTable
from app.services.get_post_service import GetPostService


@pytest.fixture()
def get_post_service():
    return GetPostService(post_repository=MagicMock(), user_repository=MagicMock())


def test_non_existing_user(get_post_service):
    get_post_service.user_repository.get_user.return_value = None
    assert get_post_service.get_post_info(1, 1) == None


def test_non_existing_post(get_post_service):
    get_post_service.user_repository.get_user.return_value = UserTable(
        id=1,
        name="name",
        email="email",
        password="password",
        created_at=datetime.now(),
        is_login=True,
    )
    get_post_service.post_repository.get_post.return_value = None
    assert get_post_service.get_post_info(1, 1) == None


def test_get_private_post_from_non_author(get_post_service):
    get_post_service.user_repository.get_user.return_value = UserTable(
        id=1,
        name="name",
        email="email",
        password="password",
        created_at=datetime.now(),
        is_login=True,
    )
    get_post_service.post_repository.get_post.return_value = PostTable(
        id=1, title="title", description="description", user_id=2, is_private=True
    )
    assert get_post_service.get_post_info(1, 1) == None


def test_get_private_post_from_author(get_post_service):
    get_post_service.user_repository.get_user.return_value = UserTable(
        id=1,
        name="name",
        email="email",
        password="password",
        created_at=datetime.now(),
        is_login=True,
    )
    get_post_service.post_repository.get_post.return_value = PostTable(
        id=1, title="title", description="description", user_id=1, is_private=True
    )
    assert (
        get_post_service.get_post_info(1, 1)
        == get_post_service.post_repository.get_post.return_value
    )


def test_get_public_post(get_post_service):
    get_post_service.user_repository.get_user.return_value = UserTable(
        id=1,
        name="name",
        email="email",
        password="password",
        created_at=datetime.now(),
        is_login=True,
    )
    get_post_service.post_repository.get_post.return_value = PostTable(
        id=1, title="title", description="description", user_id=2, is_private=False
    )
    assert (
        get_post_service.get_post_info(1, 1)
        == get_post_service.post_repository.get_post.return_value
    )
