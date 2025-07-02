from .schemas.post import Post
from .schemas.user import User


class DummyDatabase:
    users: dict[int, User] = {}
    posts: dict[int, Post] = {}


db = DummyDatabase()
