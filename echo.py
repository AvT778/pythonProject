from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType

BOT_TOKEN = '6812909660:AAEq7qTQTbsuDYYZ2vIKxaEallvQV-2m9YE'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands=["start"]))
async def startCommand(msg: Message):
    await msg.answer('Привет! Я эхо-бот.\nНапиши или отправь мне что-нибудь')

@dp.message(F.content_type == ContentType.PHOTO)
async def photoEcho(msg: Message):
    print(msg)
    await msg.reply_photo(msg.photo[0].file_id)

@dp.message()
async def echo(msg: Message):
    await msg.reply(text=msg.text)

if __name__ == "__main__":
    dp.run_polling(bot)