from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.bot import tg_bot
from app.core.config import ADMIN_ID
from app.db.db import get_random_quote, get_all_users, add_user, add_quote

router = Router()


async def send_daily_motivation():
    quote = get_random_quote()
    if not quote:
        return

    users = get_all_users()
    for user_id in users:
        try:
            await tg_bot.send_message(user_id, f"🌟 Kun hikmati:\n\n{quote}")
        except Exception:
            continue


@router.message(CommandStart)
async def start_command(message: Message):
    add_user(message.from_user.id)
    await message.answer("Xush kelibsiz! Endi sizga har kuni soat 09:00 da motivatsion xabarlar yuboriladi.")


@router.message(F.text == "/add_quote")
async def add_quote_request(message: Message):
    if message.from_user.id == ADMIN_ID:
        text = message.text.replace("/add_quote ", "")
        if text == "/add_quote":
            await message.answer(
                "Xato! Buyruqdan keyin hikmatli so'zni yozing. Masalan:\n`/add_quote Vaqt - omad kalitidir.`")
        else:
            add_quote(text)
            await message.answer("Yangi hikmatli so'z bazaga qo'shildi! ✅")
    else:
        await message.answer("Siz admin emassiz! ❌")
