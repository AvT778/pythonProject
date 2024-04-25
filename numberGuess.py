from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import random

BOT_TOKEN = '6812909660:AAEq7qTQTbsuDYYZ2vIKxaEallvQV-2m9YE'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

user = {'inGame': False, 'num': 0, "attempts": 0, 'totalGames': 0, 'wins': 0}
def getRandomNum() -> int:
    return random.randint(0, 100)
ATTEMPTS = 5
yesBtn = InlineKeyboardButton(text='Давай', callback_data='yesBtn_pressed')
noBtn = InlineKeyboardButton(text='Не хочу', callback_data='noBtn_pressed')
cancelBtn = KeyboardButton(text='Выйти из игры')
statBtn = InlineKeyboardButton(text='Статистика', callback_data='stat')
kbStart = InlineKeyboardMarkup(inline_keyboard=[[yesBtn, noBtn], [statBtn]])

@dp.message(F.text('stat'))
async def stat(msg: Message):
    await msg.answer(text=f'Ваша статистика:\nВсего игр сыграно: {user["totalGames"]}\nЧисло побед: {user['wins']}')

@dp.message(F.text('Выйти из игры'))
async def cancel(msg: Message):
    if user['inGame']:
        await msg.answer(text='Вы вышли из игры.\nЕсли захотите поиграть снова, нажмите на кнопку Старт')
    await msg.answer()

@dp.callback_query(F.text.in_(['yesBtn_pressed']))
async def yes(msg: Message):
    if not user['inGame']:
        user['inGame'] = True
        user['num'] = getRandomNum()
        user['attempts'] = ATTEMPTS
        await msg.answer('Отлично! Я уже загадал. Попробуй отгадать!')
    else:
        await msg.answer(f'Мы уже играем.\nВаши оставшиеся попытки: {user["attempts"]}')

@dp.message(lambda x: x.text and x.text.isdigit() and 0 <= int(x.text) <= 100)
async def game(msg: Message):
    if user['attempts'] == 0:
        user['inGame'] = False
        user['totalGames'] += 1
        await msg.answer(f'Увы, но это проигрыш...\nМое число - {user['num']}\n\nВаша статистика обновлена')
    if user['inGame']:
        if int(msg.text) == user['num']:
            user['inGame'] = False
            user['totalGames'] += 1
            user['wins'] += 1
            await msg.answer("Ура! Ты угадал мое число!\nПоздравляю!\n\nВаша статистика обновлена")
        elif int(msg.text) > user['num']:
            user['attempts'] -= 1
            await msg.answer(f"Загаданное мной число меньше! Оставшиеся попытки: {user['attempts']}")
        elif int(msg.text) < user['num']:
            user['attempts'] -= 1
            await msg.answer(f'Загаданное мной число больше! Оставшиеся попытки: {user['attempts']}')

@dp.message(CommandStart())
async def start(msg: Message):
    await msg.answer(text='Привет! Я - бот для игры угадай число. Давай я загадаю целое число от 0 до 100, а ты попробуешь угадать, согласен?',
                     reply_markup=kbStart)

@dp.message()
async def others(msg: Message):
    if user['inGame']:
        await msg.answer('Мы с вами играем. Я принимаю только числа в диапазоне от 0 до 100')
    else:
        await msg.answer('Я могу воспринимать только некоторые команды. Рекомендую пользоваться только кнопками')

if __name__ == "__main__":
    dp.run_polling(bot)