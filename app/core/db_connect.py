# db_connect.py
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Load environment variables from .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
print(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# TODO: I need to find a way to connect to mysql from api container inside devcontainer
# using host.docker.internal as host might work since that is how it is done in my work project
# whether this is docker-from-docker or docker-to-docker seems pretty important
def get_db():
    db = SessionLocal()
    try:
        print("DB connection successful!")
        yield db
    finally:
        db.close()
