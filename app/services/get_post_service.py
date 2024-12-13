from app.repositories.post_repository import PostRepository
from app.api_schemas.get_post_schema import Post


class GetPostService:
    def __init__(self, post_repository: PostRepository):
        self.post_repository = post_repository

    def get_post(self, post_id) -> Post:
        return self.post_repository.get_post(post_id)
