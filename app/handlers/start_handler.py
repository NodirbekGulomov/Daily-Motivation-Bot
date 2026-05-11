from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.db.commands import add_user

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    if not message.from_user:
        return

    await add_user(message.from_user.id)
    await message.answer("Sizga har kuni 09:00da random hikmatli soz yuboriladi.")
