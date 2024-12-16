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
    non_existing_user_id = 1
    get_post_service.user_repository.get_user.return_value = None
    assert get_post_service.get_post_info(1, non_existing_user_id) == None


def test_non_existing_post(get_post_service):
    non_existing_post_id = 1
    get_post_service.user_repository.get_user.return_value = (
        UserTable.test_not_login_user1_data()
    )
    get_post_service.post_repository.get_post.return_value = None
    assert (
        get_post_service.get_post_info(
            non_existing_post_id, UserTable.test_not_login_user1_data().id
        )
        == None
    )


def test_get_private_post_from_non_author(get_post_service):
    get_post_service.user_repository.get_user.return_value = (
        UserTable.test_not_login_user1_data()
    )
    get_post_service.post_repository.get_post.return_value = (
        PostTable.test_private_post_by_user1_data()
    )
    assert (
        get_post_service.get_post_info(
            UserTable.test_not_login_user1_data().id,
            PostTable.test_private_post_by_user1_data().id,
        )
        == None
    )


def test_get_private_post_from_author(get_post_service):
    get_post_service.user_repository.get_user.return_value = (
        UserTable.test_not_login_user1_data()
    )
    get_post_service.post_repository.get_post.return_value = (
        PostTable.test_private_post_by_user1_data()
    )
    assert (
        get_post_service.get_post_info(
            PostTable.test_private_post_by_user1_data().id,
            UserTable.test_not_login_user1_data().id,
        )
        == get_post_service.post_repository.get_post.return_value
    )


def test_get_public_post_from_non_author(get_post_service):
    get_post_service.user_repository.get_user.return_value = (
        UserTable.test_login_user2_data()
    )
    get_post_service.post_repository.get_post.return_value = (
        PostTable.test_public_post_by_user1_data()
    )
    assert (
        get_post_service.get_post_info(
            PostTable.test_public_post_by_user1_data().id,
            UserTable.test_login_user2_data().id,
        )
        == get_post_service.post_repository.get_post.return_value
    )
