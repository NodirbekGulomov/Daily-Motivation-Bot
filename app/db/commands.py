from app.db.base import get_connection


async def get_all_users_id() -> list:
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT tg_id FROM users
        """)

        users_id = []
        for user in cur.fetchall():
            users_id.append(user[0])
        return users_id


async def get_random_motivation() -> str:
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT text FROM motivations ORDER BY random() LIMIT 1
        """)
        return cur.fetchone()[0]


async def add_motivation(text: str) -> None:
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO motivations (text) VALUES (?)
        """, (text,))


async def add_user(tg_id: int) -> None:
    try:
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO users (tg_id) VALUES (?)
            """, (tg_id,))
    except Exception as e:
        print(e)
