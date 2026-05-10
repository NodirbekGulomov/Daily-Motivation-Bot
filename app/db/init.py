from app.db.models import create_users_table, create_motivations_table


def init_db() -> None:
    create_users_table()
    create_motivations_table()
