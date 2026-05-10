from aiogram import Router, F
from aiogram.types import Message

from app.core.config import ADMIN_ID
from app.db.commands import add_motivation

router = Router()


@router.message(F.text.startswith("/add_motivation"))
async def add_motivation_handler(message: Message):
    if not message.from_user:
        return

    if not message.text:
        return

    if ADMIN_ID == message.from_user.id:
        await add_motivation(message.text.split(":")[1].strip())
        await message.answer(text="Motivation added!")
    else:
        await message.answer(text="Error")
