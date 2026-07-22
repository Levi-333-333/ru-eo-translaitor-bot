from aiogram import Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from translate import translate
from restrictions import is_long

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет, это бот-переводчик из русского языка на эсперанто! Принцип работы прост: вы пишете сообщение боту на русском - он отвечает на эсперанто, и наоборот!\n\nSaluton, mi estas roboto por tradukado inter la rusa kaj Esperanto! Ĝi funkcias simple: vi sendas al la roboto mesaĝon en la rusa, kaj ĝi respondas en Esperanto — kaj inverse!")

@dp.message(F.text)
async def text_message_handler(message: Message) -> None:
    if is_long(message.text):
        await message.reply("Длинна сообщения не доджна превышать 5000 симполов. Уменьшите объём текста.\n\nLa mesaĝo longeco ne devas superi 5000 signojn. Redukti la kvanton da teksto.")
        return
    await message.reply(translate(message.text))