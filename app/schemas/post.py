from pydantic import BaseModel


class PostCreate(BaseModel):
    user: int
    title: str


class Post(BaseModel):
    id: int
    user: int
    title: str


class PostPartialUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
