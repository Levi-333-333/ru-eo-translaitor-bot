from dotenv import load_dotenv
from os import getenv

import asyncio
import logging
import sys

from googletrans import Translator

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message

load_dotenv()

TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()
translator = Translator()

bot = Bot(token=TOKEN)

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет, это бот-переводчик из русского языка на эсперанто! Принцип работы прост: вы пишете сообщение боту на русском - он отвечает на эсперанто, и наоборот!\nSaluton, mi estas roboto por tradukado inter la rusa kaj Esperanto! Ĝi funkcias simple: vi sendas al la roboto mesaĝon en la rusa, kaj ĝi respondas en Esperanto — kaj inverse!")

@dp.message(F.text)
async def text_message_handler(message: Message) -> None:
    input_language = (await translator.detect(message.text)).lang
    output_lang = 'ru' if input_language == 'eo' else 'eo'

    result = await translator.translate(message.text, output_lang, input_language)

    await message.reply(result.text)

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())