import os

import pytest
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker

from app.core.db_connect import Base
from app.core.main import app


class BaseTest:
    @classmethod
    def _create_db(cls):
        load_dotenv(".env.test", override=True)
        DATABASE_URL = os.getenv("DATABASE_URL")
        cls.engine = create_engine(DATABASE_URL)
        cls.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=cls.engine
        )
        inspector = inspect(cls.engine)
        existing_tables = inspector.get_table_names()
        if not existing_tables:
            Base.metadata.create_all(bind=cls.engine)
        Base.metadata.create_all(bind=cls.engine)
        cls.db = cls.SessionLocal()

    @classmethod
    def create_client(cls):
        cls.client = TestClient(app)

    @classmethod
    def setup_class(cls):
        cls.create_client()
        cls._create_db()
        cls._delete_data()
        cls._insert_data()
        cls._initialize_repository()

    @classmethod
    def teardown_class(cls):
        cls.db.close()
        cls.engine.dispose()

    @classmethod
    def _delete_data(cls):
        for table in reversed(Base.metadata.sorted_tables):
            cls.db.execute(table.delete())
        cls.db.commit()

    @classmethod
    def _initialize_repository(cls):
        pass

    @classmethod
    def _insert_data(cls):
        pass
