from fastapi import HTTPException
from config import get_db_connection
from services import summarize_text


def create_new_comment(post_id: int, content: str):
    """부모 게시글의 존재 여부를 먼저 검증한 뒤 댓글을 삽입합니다."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM posts WHERE id = ?", (post_id,))
    if not cursor.fetchone():
        conn.close()
        raise HTTPException(
            status_code=404, detail="댓글을 작성할 부모 게시글이 없습니다."
        )

    cursor.execute(
        "INSERT INTO comments (post_id, content) VALUES (?, ?)",
        (post_id, content),
    )
    conn.commit()
    comment_id = cursor.lastrowid
    conn.close()
    return {"id": comment_id, "post_id": post_id, "content": content}


def get_comment_summary_logic(comment_id: int):
    """단일 댓글 항목을 식별하여 요약 결과를 반환합니다."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT content FROM comments WHERE id = ?", (comment_id,)
    )
    row = cursor.fetchone()
    conn.close()

    if not row:
        raise HTTPException(
            status_code=404, detail="요약할 댓글 정보가 없습니다."
        )

    summary = summarize_text(row["content"])
    return {"comment_id": comment_id, "summary": summary}
