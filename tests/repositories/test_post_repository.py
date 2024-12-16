from app.helpers.helper import get_datetime_now_db_format
from app.models.post import PostTable
from app.models.user import UserTable
from app.repositories.post_repository import PostRepository
from tests.base_test import BaseTest


class TestPostRepository(BaseTest):
    @classmethod
    def _initialize_repository(cls):
        cls.post_repository = PostRepository(cls.db)

    @classmethod
    def _insert_data(cls):
        cls.db.add_all(
            [
                PostTable.test_public_post_by_user1_data(),
                UserTable.test_not_login_user1_data(),
            ]
        )
        cls.db.commit()

    @classmethod
    def test_get_existing_post(cls):
        response = cls.post_repository.get_post(
            PostTable.test_public_post_by_user1_data().id
        )
        assert response.id == PostTable.test_public_post_by_user1_data().id
        assert response.title == PostTable.test_public_post_by_user1_data().title
        assert (
            response.description
            == PostTable.test_public_post_by_user1_data().description
        )
        assert response.user_id == PostTable.test_public_post_by_user1_data().user_id
        assert (
            response.is_private == PostTable.test_public_post_by_user1_data().is_private
        )

    @classmethod
    def test_get_non_existing_post(cls):
        non_existing_post_id = 2
        response = cls.post_repository.get_post(non_existing_post_id)
        assert response == None
