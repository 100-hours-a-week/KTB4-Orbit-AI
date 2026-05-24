# URL : https://fastapi.tiangolo.com/tutorial/
# ai 팁 : 서버사이드 템플릿 렌더링을 지원하기 위해 Jinja2Templates 객체를 선언하여 프론트엔드 파일인 index.html을 클라이언트에게 서빙하는 정석 구문입니다.
# 출처: https://fastapi.tiangolo.com/tutorial/templates/
# 출처: https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-the-same-router-multiple-times

from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from config import init_db
from routers import posts, comments

@asynccontextmanager
async def lifespan(app: FastAPI):
    """애플리케이션이 구동될 때 데이터베이스 인프라 구조를 초기화합니다."""
    init_db()
    yield

app = FastAPI(title="Weekly Challenge - Controller Pattern", lifespan=lifespan)

# [FastAPI 공식 문서 가이드] 분리된 각각의 라우터들을 메인 앱에 마운트(포함)합니다.
app.include_router(posts.router)
app.include_router(comments.router)

# [FastAPI 템플릿 가이드] HTML을 응답하기 위해 Jinja2 템플릿 환경을 구성합니다.
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def render_index(request: Request):
    """UI 단일 프론트엔드 인덱스 페이지를 제공합니다."""
    return templates.TemplateResponse("index.html", {"request": request})