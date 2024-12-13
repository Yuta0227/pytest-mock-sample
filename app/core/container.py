from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Configuration, Singleton, Factory
from app.repositories.post_repository import PostRepository
from app.services.get_post_service import GetPostService
from app.core.di import get_controllers


class Container(DeclarativeContainer):
    wiring_config = WiringConfiguration(modules=get_controllers())
    post_repository = Singleton(PostRepository)
    get_post_service = Singleton(GetPostService, post_repository=post_repository)


def wire_controllers(container: Container):
    container.wire(modules=get_controllers())
