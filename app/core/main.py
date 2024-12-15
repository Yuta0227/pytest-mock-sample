import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from app.controllers import get_post_controller
from app.core.container import Container, wire_controllers
from app.core.db_connect import engine, get_db
from app.core.di import get_controller_routers


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup event
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("Database connection successful")
    except Exception as e:
        # TODO: this is where it fails
        print(f"Database connection failed: {e}")
    yield

    # Shutdown event (if needed)
    print("Application shutdown")


if "PYTEST_CURRENT_TEST" in os.environ:
    load_dotenv(dotenv_path=".env.test")
else:
    load_dotenv(dotenv_path=".env")

app = FastAPI(lifespan=lifespan)

# TODO: the command of uvicorn is "uvicorn app.core.main:app --reload". I am running this in the directory where main.py is located.

routers = get_controller_routers()

for router in routers:
    app.include_router(router)


container = Container()
wire_controllers(container)
app.container = container


@app.get("/")
def read_root():
    return {"Hello": "World"}
