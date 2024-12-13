from app.models.post import PostTable
from app.repositories.post_repository import PostRepository


class GetPostService:
    def __init__(self, post_repository: PostRepository):
        self.post_repository = post_repository

    def get_post(self, post_id) -> PostTable:
        return self.post_repository.get_post(post_id)
