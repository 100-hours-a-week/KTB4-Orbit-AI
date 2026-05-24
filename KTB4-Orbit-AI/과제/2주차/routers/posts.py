#라우터 라우팅 계층 
#URL : https://fastapi.tiangolo.com/tutorial/bigger-applications/
# 서비스가 커지게 되면은 이제 그 main.py가 커지게 되니까 APIrouter를 사용해 기능 도메인별로 URL경로와 문서 그룹으로
# 분리하는 전형적인 설계 방식을 ㅅ사용합니다

# URL: https://fastapi.tiangolo.com/tutorial/bigger-applications/#apirouter

from fastapi import APIRouter
from models import PostCreate
import controllers.posts as post_controller


router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("")
def create_post(post: PostCreate):
    return post_controller.create_new_post(post.title, post.content)


@router.get("")
def get_posts():
    return post_controller.read_all_posts()


@router.get("/{post_id}")
def get_post_detail(post_id: int):
    return post_controller.read_post_detail(post_id)


@router.get("/{post_id}/summary")
def get_post_summary(post_id: int):
    return post_controller.get_post_summary_logic(post_id)