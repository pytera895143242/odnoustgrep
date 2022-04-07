from aiogram import types
from misc import dp,bot
from .sqlit import reg_user
from .callbak_data import st
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

content_chat = -1001765817067
ids_user = []

markup = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='Далее', callback_data='go')
markup.add(bat_a)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message, state: FSMContext):
    reg_user(message.chat.id)
    await st.step1.set()
    await state.update_data(first_video='stop')

    await message.answer(text="""Наверняка видишь, как многие ведут свои телеграм каналы.""")
    await asyncio.sleep(3)
    await message.answer(text="""И конечно все не просто так""")
    await asyncio.sleep(2)
    await message.answer(text="""Когда ты ведёшь свой телеграм канал, можно неплохо зарабатывать, и это не новость""")
    await asyncio.sleep(3)
    await bot.copy_message(chat_id=message.chat.id, from_chat_id= content_chat, message_id = 406, caption= """<b>Ввожу в курс дела ☝️</b>""",reply_markup=markup)

    await asyncio.sleep(120) # 2 минуты
    await state.update_data(first_video = 'start')


