from dotenv import load_dotenv
from os import getenv

import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, F
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.filters import CommandStart
from aiogram.types import Message

from translate import translate

load_dotenv()

TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()

PROXY_URL = "mtproto://4bc2b4812b2f00758cbcdd415dc98537ef0fb9f5919fef01a3b11135464b7f3a@127.0.0.1:8443"
session = AiohttpSession(proxy=PROXY_URL)

bot = Bot(token=TOKEN, request_timeout=30, session=session)

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет, это бот-переводчик из русского языка на эсперанто! Принцип работы прост: вы пишете сообщение боту на русском - он отвечает на эсперанто, и наоборот!\nSaluton, mi estas roboto por tradukado inter la rusa kaj Esperanto! Ĝi funkcias simple: vi sendas al la roboto mesaĝon en la rusa, kaj ĝi respondas en Esperanto — kaj inverse!")

@dp.message(F.text)
async def text_message_handler(message: Message) -> None:
    await message.reply(translate(message.text))

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())