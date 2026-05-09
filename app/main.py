import asyncio

from app.bot import tg_bot
from app.dispatcher import dp


async def main():
    print("Bot started ...")
    dp.start_polling(tg_bot)


asyncio.run(main())
