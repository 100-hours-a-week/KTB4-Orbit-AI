#모델 계층
# FastAPI 공식 문서
# URL: https://fastapi.tiangolo.com/tutorial/body/
# URL : https://fastapi.tiangolo.com/tutorial/body/#create-your-data-model

from typing import Optional
from pydantic import BaseModel

class PostCreate(BaseModel):
    title: str
    content : str

class CommentCreate(BaseModel):
    content : str
  #  post_id : str

class CommentResponse(BaseModel):
    id : int
    post_id : int
    content : str

class PostDetailResponse(BaseModel):
    id : int
    title: str
    content : str
    comments : list[CommentResponse]