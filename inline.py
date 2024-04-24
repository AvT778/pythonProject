from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

BOT_TOKEN = '6812909660:AAEq7qTQTbsuDYYZ2vIKxaEallvQV-2m9YE'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
yaBtn = InlineKeyboardButton(text='Яндекс', callback_data='yaBtn_pressed')
googleBtn = InlineKeyboardButton(text='Google', callback_data='googleBtn_pressed')

kb = InlineKeyboardMarkup(inline_keyboard=[[yaBtn], [googleBtn]])

@dp.callback_query(F.data.in_(['yaBtn_pressed']))
async def yaBtnPressed(cb: CallbackQuery):
    if cb.message.text != 'Спасибо, что предпочитаете отечественный продукт!':
        await cb.message.edit_text(text='Спасибо, что предпочитаете отечественный продукт!', reply_markup=cb.message.reply_markup)
    await cb.answer()

@dp.callback_query(F.data.in_(['googleBtn_pressed']))
async def googleBtnPressed(cb: CallbackQuery):
    if cb.message.text != 'Советуем пересмотреть своё отношение к Яндексу, ведь там появилось очень много нового!':
        await cb.message.edit_text(text='Советуем пересмотреть своё отношение к Яндексу, ведь там появилось очень много нового!', reply_markup=cb.message.reply_markup)
    await cb.answer()

@dp.message(CommandStart())
async def start(msg: Message):
    await msg.answer(text='Какой поисковик вы предпочитаете?', reply_markup=kb)

if __name__ == "__main__":
    dp.run_polling(bot)