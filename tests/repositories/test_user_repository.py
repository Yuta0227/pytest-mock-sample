from app.helpers.helper import get_datetime_now_db_format
from app.models.user import UserTable
from app.repositories.user_repository import UserRepository
from tests.base_test import BaseTest


class TestUserRepository(BaseTest):
    DATETIME = get_datetime_now_db_format()
    user_data = {
        "id": 1,
        "name": "test",
        "email": "test@example.com",
        "password": "password",
        "created_at": DATETIME,
        "is_login": False,
    }

    @classmethod
    def _initialize_repository(cls):
        cls.user_repository = UserRepository(cls.db)

    @classmethod
    def _insert_data(cls):
        cls.db.add_all([UserTable(**cls.user_data)])
        cls.db.commit()

    @classmethod
    def test_get_existing_user(cls):
        response = cls.user_repository.get_user(1)
        assert response.id == cls.user_data["id"]
        assert response.name == cls.user_data["name"]
        assert response.email == cls.user_data["email"]
        assert response.password == cls.user_data["password"]
        assert (
            response.created_at.strftime("%Y-%m-%d %H:%M:%S")
            == cls.user_data["created_at"]
        )
        assert response.is_login == cls.user_data["is_login"]

    @classmethod
    def test_get_non_existing_user(cls):
        response = cls.user_repository.get_user(2)
        assert response == None
