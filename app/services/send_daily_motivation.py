from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pytz import timezone

from app.services.send_motivation import send_random_motivation_to_all_users


def send_daily_motivation_to_all_users():
    scheduler = AsyncIOScheduler(timezone=timezone("Asia/Tashkent"))
    scheduler.add_job(
        func=send_random_motivation_to_all_users,
        trigger='cron',
        hour=21,
        minute=14
    )
    scheduler.start()
