from sqlalchemy.orm import Session

from app.models.user import UserTable


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user(self, user_id) -> UserTable:
        return self.db.query(UserTable).filter(UserTable.id == user_id).first()

    def is_login(self, user_id):
        return self.db.query(UserTable).filter(UserTable.id == user_id).first().is_login
