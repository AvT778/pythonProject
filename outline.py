from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.types.web_app_info import WebAppInfo

BOT_TOKEN = '6812909660:AAEq7qTQTbsuDYYZ2vIKxaEallvQV-2m9YE'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
webAppBtn = KeyboardButton(text='Открыть Яндекс', web_app=WebAppInfo(url='https://ya.ru/'))
contactBtn = KeyboardButton(text='Отправить телефон', request_contact=True)
geoBtn = KeyboardButton(text='Отправить геолокацию', request_location=True)
poll1Btn = KeyboardButton(text='Создать викторину', request_poll=KeyboardButtonPollType(type='quiz'))
poll2Btn = KeyboardButton(text='Создать опрос', request_poll=KeyboardButtonPollType(type='regular'))

keyboard = ReplyKeyboardMarkup(keyboard=[[webAppBtn], [contactBtn, geoBtn], [poll1Btn, poll2Btn]], resize_keyboard=True, one_time_keyboard=True)

@dp.message(CommandStart())
async def processStart(msg: Message):
    await msg.answer(text='Тестим специальные кнопки :^', reply_markup=keyboard)

if __name__ == "__main__":
    dp.run_polling(bot)