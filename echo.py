from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType

BOT_TOKEN = '6812909660:AAEq7qTQTbsuDYYZ2vIKxaEallvQV-2m9YE'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands=["start"]))
async def startCommand(msg: Message):
    await msg.answer('Привет! Я эхо-бот.\nНапиши или отправь мне что-нибудь')

@dp.message(F.AUDIO)
async def audioEcho(msg: Message):
    print(msg)
    await msg.reply_audio(msg.audio.file_id)

@dp.message(F.PHOTO)
async def photoEcho(msg: Message):
    print(msg)
    await msg.reply_photo(msg.photo[0].file_id)

@dp.message(F.VOICE)
async def voiceEcho(msg: Message):
    print(msg)
    await msg.reply_voice(msg.voice.file_id)

@dp.message(F.DOCUMENT)
async def docEcho(msg: Message):
    print(msg)
    await msg.reply_document(msg.document.file_id)

@dp.message(F.STICKER)
async def stickerEcho(msg: Message):
    print(msg)
    await msg.reply_sticker(msg.sticker.file_id)

@dp.message(F.VIDEO)
async def videoEcho(msg: Message):
    print(msg)
    await msg.reply_video(msg.video.file_id)

@dp.message()
async def echo(msg: Message):
    await msg.reply(text=msg.text)

if __name__ == "__main__":
    dp.run_polling(bot)