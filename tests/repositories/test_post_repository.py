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
                PostTable(
                    id=1, title="test", description="test", user_id=1, is_private=False
                ),
                UserTable(
                    id=1,
                    name="test",
                    email="test",
                    password="test@example.com",
                    created_at=get_datetime_now_db_format(),
                    is_login=False,
                ),
            ]
        )
        cls.db.commit()

    @classmethod
    def test_get_existing_post(cls):
        response = cls.post_repository.get_post(1)
        assert response.id == 1
        assert response.title == "test"
        assert response.description == "test"
        assert response.user_id == 1
        assert response.is_private == False

    @classmethod
    def test_get_non_existing_post(cls):
        response = cls.post_repository.get_post(2)
        assert response == None
