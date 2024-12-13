from dependency_injector.containers import (DeclarativeContainer,
                                            WiringConfiguration)
from dependency_injector.providers import Configuration, Factory, Singleton

from app.core.db_connect import SessionLocal, get_db
from app.core.di import get_controllers
from app.repositories.post_repository import PostRepository
from app.services.get_post_service import GetPostService


class Container(DeclarativeContainer):
    db_session = Singleton(SessionLocal)
    wiring_config = WiringConfiguration(modules=get_controllers())
    post_repository = Singleton(PostRepository, db=db_session)
    get_post_service = Singleton(GetPostService, post_repository=post_repository)


def wire_controllers(container: Container):
    container.wire(modules=get_controllers())
