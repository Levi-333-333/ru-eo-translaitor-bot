from aiogram import Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from translate import translate

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет, это бот-переводчик из русского языка на эсперанто! Принцип работы прост: вы пишете сообщение боту на русском - он отвечает на эсперанто, и наоборот!\n\nSaluton, mi estas roboto por tradukado inter la rusa kaj Esperanto! Ĝi funkcias simple: vi sendas al la roboto mesaĝon en la rusa, kaj ĝi respondas en Esperanto — kaj inverse!")

@dp.message(F.text)
async def text_message_handler(message: Message) -> None:
    try:
        await message.reply(translate(message.text))
    except Exception as e:
        await message.reply(str(e))