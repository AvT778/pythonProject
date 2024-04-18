from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

BOT_TOKEN = '6812909660:AAEq7qTQTbsuDYYZ2vIKxaEallvQV-2m9YE'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
contactBtn = KeyboardButton(text='Отправить телефон', request_contact=True)
geoBtn = KeyboardButton(text='Отправить геолокацию', request_location=True)
pollBtn = KeyboardButton(text='Создать опрос/викторину', request_poll=KeyboardButtonPollType())

keyboard = ReplyKeyboardMarkup(keyboard=[[contactBtn, geoBtn], [pollBtn]], resize_keyboard=True, one_time_keyboard=True)

@dp.message(CommandStart())
async def processStart(msg: Message):
    await msg.answer(text='Тестим специальные кнопки :^', reply_markup=keyboard)
@dp.message(F.text == 'Собак 🦮')
async def dogAnswer(msg: Message):
    await msg.answer(text='Верно! Но вы видели, как кошки боятся огурцов?')
@dp.message(F.text == 'Огурцов 🥒')
async def cucumberAnswer(msg: Message):
    await msg.answer(text='Да, иногда кажется, что огурцов кошки боятся больше')

if __name__ == "__main__":
    dp.run_polling(bot)