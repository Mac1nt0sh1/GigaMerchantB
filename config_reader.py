from pathlib import Path
from typing import AsyncGenerator
from contextlib import asynccontextmanager

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from aiogram import Bot, Dispatcher
from fastapi import FastAPI
from tortoise import Tortoise


ROOT_DIR = Path(__file__).parent.parent


class Config(BaseSettings):
    BOT_TOKEN: SecretStr
    DB_URL: SecretStr

    WEBHOOK_URL: str = "https://hrqkq-104-239-74-10.a.free.pinggy.link"
    WEBAPP_URL: str = "https://gigamerchanb.web.app"

    APP_HOST: str = "localhost"
    APP_PORT: int = 8080

    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / "server" / ".env",
        env_file_encoding="utf-8"
    )

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    await bot.set_webhook(
        url=f"{config.WEBHOOK_URL}/webhook",
        allowed_updates=dp.resolve_used_update_types(),
        drop_pending_updates=True,
    )
    await Tortoise.init(config=TORTOISE_ORM)
    try:
        yield
    finally:
        await Tortoise.close_connections()
        await bot.session.close()
    
config = Config()

bot = Bot(config.BOT_TOKEN.get_secret_value().strip())
dp = Dispatcher()
app = FastAPI(lifespan=lifespan)

TORTOISE_ORM = {
    "connections": {"default": config.DB_URL.get_secret_value().strip()},
    "apps": {
        "models": {
            "models": ["server.db.models.user", "aerich.models"],
            "default_connection": "default",
        }
    },
}
