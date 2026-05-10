from app.bot import tg_bot
from app.db.commands import get_all_users_id, get_random_motivation


async def send_random_motivation_to_all_users():
    all_users_id = await get_all_users_id()
    motivation = await get_random_motivation()
    for user_id in all_users_id:
        await tg_bot.send_message(chat_id=user_id, text=motivation)
