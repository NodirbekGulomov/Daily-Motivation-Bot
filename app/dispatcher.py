from aiogram import Dispatcher
from app.handlers.add_motivation_handler import router as add_motivation_router
from app.handlers.start_handler import router as start_router

dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(add_motivation_router)
