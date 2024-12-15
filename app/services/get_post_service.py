from app.models.post import PostTable
from app.repositories.post_repository import PostRepository
from app.repositories.user_repository import UserRepository


class GetPostService:
    def __init__(
        self, post_repository: PostRepository, user_repository: UserRepository
    ):
        self.post_repository = post_repository
        self.user_repository = user_repository

    def get_post_info(self, post_id, user_id) -> PostTable:
        # check user existence
        if not self.user_repository.get_user(user_id):
            return None
        post = self.post_repository.get_post(post_id)
        if not post or not self.__is_visible(post, user_id):
            return None
        return post

    def __is_visible(self, post: PostTable, user_id) -> bool:
        if post.user_id == user_id:
            return True
        elif not post.is_private:
            return True
        else:
            return False
