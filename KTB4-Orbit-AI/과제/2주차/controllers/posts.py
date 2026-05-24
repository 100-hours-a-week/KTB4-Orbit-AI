#컨트롤러 비즈니스 로직 계층
# URL : https://docs.python.org/3/library/sqlite3.html

from fastapi import HTTPException
from config import get_db_connection
from services import summarize_text


def create_new_post(title: str, content: str):
    """새로운 게시글을 데이터베이스에 안전하게 삽입합니다."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO posts (title, content) VALUES (?, ?)", (title, content)
    )
    conn.commit()
    post_id = cursor.lastrowid
    conn.close()
    return {"id": post_id, "title": title, "content": content}


def read_all_posts():
    """전체 게시글 목록을 반환합니다."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, content FROM posts")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]


def read_post_detail(post_id: int):
    """게시글 상세 내용과 해당 게시글에 매핑된 댓글 목록을 병합하여 반환합니다."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, title, content FROM posts WHERE id = ?", (post_id,)
    )
    post_row = cursor.fetchone()

    if not post_row:
        conn.close()
        raise HTTPException(
            status_code=404, detail="요청하신 게시글을 찾을 수 없습니다."
        )

    cursor.execute(
        "SELECT id, post_id, content FROM comments WHERE post_id = ?",
        (post_id,),
    )
    comment_rows = cursor.fetchall()
    conn.close()

    post_data = dict(post_row)
    post_data["comments"] = [dict(c) for c in comment_rows]
    return post_data


def get_post_summary_logic(post_id: int):
    """게시글 본문을 찾아 요약 서비스로 전달합니다."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM posts WHERE id = ?", (post_id,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        raise HTTPException(
            status_code=404, detail="요약할 게시글이 존재하지 않습니다."
        )

    summary = summarize_text(row["content"])
    return {"post_id": post_id, "summary": summary}