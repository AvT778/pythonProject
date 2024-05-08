from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
import random

BOT_TOKEN = '6812909660:AAEq7qTQTbsuDYYZ2vIKxaEallvQV-2m9YE'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
users = {}
def getRandomNum() -> int:
    return random.randint(0, 100)
ATTEMPTS = 5
yesBtn = KeyboardButton(text='Давай')
noBtn = KeyboardButton(text='Не хочу')
cancelBtn = KeyboardButton(text='Выйти из игры')
statBtn = KeyboardButton(text='Статистика')
kbStart = ReplyKeyboardMarkup(keyboard=[[yesBtn, noBtn], [statBtn]], one_time_keyboard=True)

@dp.message(CommandStart())
async def start(msg: Message):
    await msg.answer(text='Привет! Я - бот для игры угадай число. Давай я загадаю целое число от 0 до 100, а ты попробуешь угадать, согласен?',
                     reply_markup=kbStart)
    if msg.from_user.id not in users:
        users[msg.from_user.id] = {'inGame': False, 'num': 0, "attempts": 0, 'totalGames': 0, 'wins': 0}

@dp.message(F.text == 'Статистика')
async def stat(msg: Message):
    await msg.answer(text=f"Ваша статистика:\nВсего игр сыграно: {users[msg.from_user.id]['totalGames']}\nЧисло побед: {users[msg.from_user.id]['wins']}")

@dp.message(F.text == 'Выйти из игры')
async def cancel(msg: Message):
    if users[msg.from_user.id]['inGame']:
        await msg.answer(text='Вы вышли из игры.\nЕсли захотите поиграть снова, нажмите на кнопку Старт')
    await msg.answer()

@dp.message(F.text == 'Давай')
async def yes(msg: Message):
    if not users[msg.from_user.id]['inGame']:
        users[msg.from_user.id]['inGame'] = True
        users[msg.from_user.id]['num'] = getRandomNum()
        users[msg.from_user.id]['attempts'] = ATTEMPTS
        await msg.answer('Отлично! Я уже загадал. Попробуй отгадать!')
    else:
        await msg.answer(f'Мы уже играем.\nВаши оставшиеся попытки: {users[msg.from_user.id]["attempts"]}')

@dp.message(F.text == 'Не хочу')
async def no(msg: Message):
    if users[msg.from_user.id]['inGame']:
        await msg.answer('Хорошо. Приходите, когда появится желание')
    else:
        await msg.answer(f'Мы уже играем.\nВаши оставшиеся попытки: {users[msg.from_user.id]["attempts"]}')

@dp.message(lambda x: x.text and x.text.isdigit() and 0 <= int(x.text) <= 100)
async def game(msg: Message):
    if users[msg.from_user.id]['attempts'] == 0:
        if int(msg.text) == users[msg.from_user.id]['num']:
            users[msg.from_user.id]['inGame'] = False
            users[msg.from_user.id]['totalGames'] += 1
            users[msg.from_user.id]['wins'] += 1
            await msg.answer("Ура! Ты угадал мое число!\nПоздравляю!\n\nВаша статистика обновлена")
        else:
            users[msg.from_user.id]['inGame'] = False
            users[msg.from_user.id]['totalGames'] += 1
            await msg.answer(f'Увы, но это проигрыш...\nМое число - {users[msg.from_user.id]["num"]}\n\nВаша статистика обновлена')
    if users[msg.from_user.id]['inGame']:
        if int(msg.text) == users[msg.from_user.id]['num']:
            users[msg.from_user.id]['inGame'] = False
            users[msg.from_user.id]['totalGames'] += 1
            users[msg.from_user.id]['wins'] += 1
            await msg.answer("Ура! Ты угадал мое число!\nПоздравляю!\n\nВаша статистика обновлена")
        elif int(msg.text) > users[msg.from_user.id]['num']:
            await msg.answer(f"Загаданное мной число меньше! Оставшиеся попытки: {users[msg.from_user.id]['attempts']}")
            users[msg.from_user.id]['attempts'] -= 1
        elif int(msg.text) < users[msg.from_user.id]['num']:
            await msg.answer(f"Загаданное мной число больше! Оставшиеся попытки: {users[msg.from_user.id]['attempts']}")
            users[msg.from_user.id]['attempts'] -= 1

@dp.message()
async def others(msg: Message):
    if users[msg.from_user.id]['inGame']:
        await msg.answer('Мы с вами играем. Я принимаю только числа в диапазоне от 0 до 100')
    else:
        await msg.answer('Я могу воспринимать только некоторые команды. Рекомендую пользоваться только кнопками')

if __name__ == "__main__":
    dp.run_polling(bot)