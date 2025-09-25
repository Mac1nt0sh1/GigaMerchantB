# common.py
from fastapi import APIRouter, Request
from aiogram.types import Update
from ..config_reader import bot, dp

router = APIRouter()

@router.post("/webhook")
async def webhook(request: Request):
    update = Update(**await request.json())
    await dp.feed_webhook_update(bot, update)
    return {"ok": True}
