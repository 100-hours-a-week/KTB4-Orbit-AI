from fastapi import APIRouter
from models import CommentCreate
import controllers.comments as comment_controller

router = APIRouter(tags=["comments"])


@router.post("/posts/{post_id}/comments")
def create_comment(post_id: int, comment: CommentCreate):
    return comment_controller.create_new_comment(post_id, comment.content)


@router.get("/comments/{comment_id}/summary")
def get_comment_summary(comment_id: int):
    return comment_controller.get_comment_summary_logic(comment_id)
