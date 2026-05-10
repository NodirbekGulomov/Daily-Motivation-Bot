import asyncio

from app.bot import tg_bot
from app.db.init import init_db
from app.dispatcher import dp
from app.services.send_daily_motivation import send_daily_motivation_to_all_users


async def main():
    init_db()
    send_daily_motivation_to_all_users()
    print("Bot started...")
    await dp.start_polling(tg_bot)


if __name__ == "__main__":
    asyncio.run(main())
