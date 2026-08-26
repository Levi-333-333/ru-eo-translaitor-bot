from dotenv import load_dotenv
from os import getenv
import asyncio
import logging
import sys
from aiogram import Bot
from aiogram.client.session.aiohttp import AiohttpSession
from handlers import *

load_dotenv()
TOKEN = getenv("BOT_TOKEN")
PROXY_URL = getenv("PROXY_URL")

session = AiohttpSession(proxy=PROXY_URL)

bot = Bot(token=TOKEN, session=session)

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())