from typing import Optional
from pydantic import BaseModel

class PostCreate(BaseModel):
    title: str
    content: str

class CommentCreate(BaseModel):
    content: str

class CommentResponse(BaseModel):
    id: int
    post_id: int
    content: str

class PostDetailResponse(BaseModel):
    id: int
    title: str
    content: str
    comments: list[CommentResponse]
