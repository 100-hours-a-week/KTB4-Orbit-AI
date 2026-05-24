# KTB4-Orbit-AI
WEEK2 Web backend programming @ llm integration

> KTB4 위클리챌린지 2주차  - FastAPI로 커뮤니티 서비스 백엔드 구현 및 Gemini api 연동

---

## 목표 

FastAPI 웹 프레임워크와 SQLite3 DB를 활용한 MVC/컨트롤러 패턴 기반의 커뮤니티 서비스 구축
- 데이터베이스 영속성(Persistence)을 가지는 게시글 및 댓글 CRUD API 구현
- 구글 Gemini 2.5 Flash 모델을 연동하여 게시글 본문 및 댓글의 비동기 AI 핵심 요약 기능 구현
- Jinja2Templates를 활용하여 프론트엔드 UI(HTML/CSS)와 백엔드 API 간의 단일 진입점(Single Endpoint) 서빙

## 프로젝트 구조
과제/2주차/
├── main.py            # 애플리케이션 진입점 및 라우터 등록
├── config.py          # 데이터베이스 인프라 구조 초기화 (init_db)
├── models.py          # SQLite3 연동 스키마 정의 (Post, Comment)
├── services.py        # 구글 Gemini API 연동 및 LLM 비동기 요약 로직
├── controllers/       # 비즈니스 로직 처리 레이어
│   ├── __init__.py
│   ├── posts.py
│   └── comments.py
├── routers/           # HTTP 요청 명사(URI) 라우팅 레이어
│   ├── __init__.py
│   ├── posts.py
│   └── comments.py
└── templates/         # UI 서빙 레이어
    └── index.html     # 단일 페이지 프론트엔드 템플릿
    
## 설치 및 실행
의존성 라이브러리 설치
```bash
pip3 install fastapi uvicorn google-genai jinja2
```

서버 실행
```bash
export GEMINI_API_KEY="본인 제미나이 api키"
python3 -m uvicorn main:app --reload
```

웹 화면 접속(UI) : http://127.0.0.1:8000/
FastAPI 자동 문서화(Swagger UI) 확인: http://127.0.0.1:8000/docs

## 주요 기능 
게시글 및 댓글 CRUD: 작성된 데이터가 로컬 orbit.db에 안전하게 적재 및 조회됩니다.

Gemini AI 핵심 요약: 게시글 상세 내용이나 복잡한 댓글 목록을 클릭 한 번으로 gemini-2.5-flash 모델이 한 문장으로 즉시 요약합니다.

## 백엔드 핵심 설계 

- 컨트롤러 패턴 분리 : 라우팅 역항을 하는 루터와 실제 데이터 비즈니스 로직을 처리하는 controllers를 PEP8 표준 명명 규칙에 맞게 완벽하게 분리하여 유지보수성을 올리기

- 보안 및 환경변수 : 깃허브 소스코드 유출을 막기 위해 services.py 내부의 genai.client() 생성자 괄호를 비워뒀습니다.



## 회고
1주차에는 이제 CLI 환경에서 파이썬 기초 문법과 비동기를 맛 보았다면, 2주차에는 실제 산업에서 사용하는 웹 백엔드의 정석구조인 MVC와 컨트롤러 패턴을 적용하여 
FastAPI와 데이터베이스, 서비스 레이어 분리를 깊이 있게 경험을 할 수 있었습니다.
파이썬의 import 규칙과 가상환경 설정, 가벼우면서도 강력한 fastapi의 구조를 하는것이 저에게는 큰 도전이었습니다.
아직 파이썬의 기본 문법이 익숙하지 않아 조금 헤매는 부분도 있었지만 교재와 ai를 활용하여 조금더 쉽게 이해하고 적용할 수 있었ㅅ습니다.

개발 과정에서 파이썬 버전 인식 문제 (path) 꼬임으로 인해 uvicorn 실행 오류를 겪거나, 깃허브 업로드 과정에서 하위 저장소 인덱스가 자꾸 꼬여서
1주차 자료가 유실될뻔한 순간도 있었습니다.
그러나 깃의 인덱스를 초기화 하는 (git rm -rf --cached .)하고 원격 저장소 충돌을 해결해 나가면서 버전을 제어하는 개발자로서의 시야도 한층 넓어질 수 있었던거 같습니다.

아직 1,2주차에 배운 용어들과 개발 환경이 모두 낯설고 어렵게만 느껴지지만 조금씩 더 배우고 해보고 경험을 하다보면은 익숙해지고 좋아질거라고 생각을 합니다.
앞으로도 직면하는 기술적 한계에 부딪힐 때마다 부족한 만큼 시간을 더 투자하고 배우며, 끊임없이 성장하는 개발자(엔지니어)가 되겠습니다.
