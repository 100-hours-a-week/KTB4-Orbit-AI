#데이터베이스 설정 및 초기화
# 참고 URL : https://peps.python.org/pep-0008/#constants

import sqlite3

DB_NAME = "orbit.db"

def get_db_connection():
    # sqlite3.Connection(DB_NAME) 대신 표준 함수인 sqlite3.connect(DB_NAME)를 사용하여 연결합니다.
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # post 테이블 생성
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """)
    
    # comment 테이블 생성
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            post_id INTEGER NOT NULL,
            content TEXT NOT NULL,
            FOREIGN KEY (post_id) REFERENCES posts (id) ON DELETE CASCADE
        )
    """)

    conn.commit()
    conn.close()
