from app.models.user import UserTable
from app.repositories.user_repository import UserRepository
from tests.base_test import BaseTest


class TestUserRepository(BaseTest):

    @classmethod
    def _initialize_repository(cls):
        cls.user_repository = UserRepository(cls.db)

    @classmethod
    def _insert_data(cls):
        cls.db.add_all([UserTable.test_not_login_user_data()])
        cls.db.commit()

    @classmethod
    def test_get_existing_user(cls):
        response = cls.user_repository.get_user(UserTable.test_not_login_user_data().id)
        assert response.id == UserTable.test_not_login_user_data().id
        assert response.name == UserTable.test_not_login_user_data().name
        assert response.email == UserTable.test_not_login_user_data().email
        assert response.password == UserTable.test_not_login_user_data().password
        assert (
            response.created_at.strftime("%Y-%m-%d %H:%M:%S")
            == UserTable.test_not_login_user_data().created_at
        )
        assert response.is_login == UserTable.test_not_login_user_data().is_login

    @classmethod
    def test_get_non_existing_user(cls):
        non_existing_user_id = 2
        response = cls.user_repository.get_user(non_existing_user_id)
        assert response == None

    @classmethod
    def test_is_login(cls):
        response = cls.user_repository.is_login(UserTable.test_not_login_user_data().id)
        assert response == UserTable.test_not_login_user_data().is_login
