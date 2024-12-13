from pydantic import BaseModel


class Post(BaseModel):
    id: int
    title: str
    description: str


class PostRepository:
    def get_post(self, post_id) -> Post:
        if post_id == 0:
            return None
        return Post(id=post_id, title="Post title", description="Post description")

    def create_post(self, post):
        return {"status": "created", "post": post}

    def update_post(self, post_id, post):
        return {"status": "updated", "post": post}

    def delete_post(self, post_id):
        return {"status": "deleted", "post_id": post_id}
