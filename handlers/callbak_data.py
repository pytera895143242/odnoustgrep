from aiogram import types
from misc import dp, bot
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from .sqlit import update_country,cheak_traf,reg_user,cheak_chat_id,get_country
import random

reg_user(0)
list_channel = cheak_traf()

name_channel_1 = list_channel[0][0][1:]
link_channel_1 = list_channel[0][1]

name_channel_2 = list_channel[1][0][1:]
link_channel_2 = list_channel[1][1]

name_channel_3 = list_channel[2][0][1:]
link_channel_3 = list_channel[2][1]

channel_posts = -1001525589284

list_channel = cheak_traf()
name_channel_1 = list_channel[0]
name_channel_2 = list_channel[1]
name_channel_3 = list_channel[2]
name_channel_4 = list_channel[3]

def obnovlenie():
    global name_channel_1,name_channel_2,name_channel_3,name_channel_4
    list_channel = cheak_traf()
    name_channel_1 = list_channel[0]
    name_channel_2 = list_channel[1]
    name_channel_3 = list_channel[2]
    name_channel_3 = list_channel[3]


content_chat = -1001765817067

text_stop = """Ах шалунишка 😈 сначала смотри видос, потом тыкай)"""


BIGtext_one = """Ууууууу Салам ✊🏻

Одноус на связи 🤙 

Ну что!!! Наконец-то хоть что-то нормально будет, а не сказки, как дед насрал в коляске))

Кстати, что думаешь нам надо познакомиться?)

Или сразу поедем по программе?"""


markup = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='Погнали', callback_data='pognali')
markup.add(bat_a)


markup_ready = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='✅ Готово', callback_data='ready')
markup_ready.add(bat_a)


markup_dating = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='Давай познакомимся 🤝', callback_data='dating')
bat_b = types.InlineKeyboardButton(text='Давай сразу к делу 😎', callback_data='program')
markup_dating.add(bat_a)
markup_dating.add(bat_b)

markup_da = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='Играем 🎸', callback_data='games')
markup_da.add(bat_a)

markup_go = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='Гоооооо', callback_data='program')
markup_go.add(bat_a)

markup_workshop = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='Программа воркшопа', callback_data='workshop')
markup_workshop.add(bat_a)


markup_member = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='Хочу учавствовать', callback_data='member')
markup_member.add(bat_a)



markup_country = types.InlineKeyboardMarkup()
bat_1 = types.InlineKeyboardButton(text='Россия 🇷🇺', callback_data='ru')
bat_2 = types.InlineKeyboardButton(text='Казахстан 🇰🇿', callback_data='kz')
bat_3 = types.InlineKeyboardButton(text='Кыргызстан 🇰🇬', callback_data='kr')
bat_4 = types.InlineKeyboardButton(text='Узбекистан 🇺🇿', callback_data='uzb')
bat_5 = types.InlineKeyboardButton(text='Беларусь 🇧🇾', callback_data='bel')
bat_6 = types.InlineKeyboardButton(text='Украина 🇺🇦', callback_data='uk')
bat_7 = types.InlineKeyboardButton(text='Другая страна', callback_data='another_country')

markup_country.add(bat_1)
markup_country.add(bat_2)
markup_country.add(bat_3)
markup_country.add(bat_4)
markup_country.add(bat_5)
markup_country.add(bat_6)
markup_country.add(bat_7)


class st(StatesGroup):
    step1 = State()
    step2 = State()
    step3 = State()
    step4 = State()
    step5 = State()


@dp.callback_query_handler(lambda call: True, state='*')
async def answer_push_inline_button(call, state: FSMContext):
    if call.data == 'go':
        try:
            if ((await state.get_data())['first_video']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True


        if flag == False:
            await call.message.answer(text_stop)
        else:
            await call.message.answer('Смотри, мы с командой откопали способ')
            await asyncio.sleep(3)
            await call.message.answer("""Как новичку ворваться в индустрию телеграма максимально безболезненно""")
            await asyncio.sleep(4)
            await call.message.answer("Благодаря модели tgstart")
            await asyncio.sleep(3)
            await call.message.answer("Пока другие вкладывают деньги в каналы, покупают дорогое обучение, рискуя тем, что может ничего не получиться.")
            await asyncio.sleep(6)
            await call.message.answer("Мы двигаемся по модели, которая позволяет новичку не совершать тупых ошибок!")
            await asyncio.sleep(5)
            await call.message.answer("""Сегодня узнаешь про телеграм.
И вместе соберём твой бизнес в тг.""")
            await asyncio.sleep(4)
            await call.message.answer("""Будет жарко 🔥🔥🔥""")
            await asyncio.sleep(2)
            await bot.send_message(chat_id=call.message.chat.id , text= """Едем дальше?))""",reply_markup = markup)


    if call.data == 'pognali':
        await bot.copy_message(chat_id=call.message.chat.id, from_chat_id= content_chat, message_id = 434, caption = BIGtext_one,reply_markup=markup_dating)

    if call.data == 'dating':
        await bot.send_message(chat_id=call.message.chat.id,
                               text="""Чтобы не писать киломметровую статью про себя, на которую всем похер 😂""")
        await asyncio.sleep(3)
        await bot.send_message(chat_id=call.message.chat.id,
                               text="""У меня есть 4 ахриненных вопроса, которые помогут нам познакомиться)""")
        await asyncio.sleep(3)
        await bot.send_message(chat_id=call.message.chat.id, text="""Формат такой, я начинаю отвечать потом ты))""")
        await asyncio.sleep(3)
        await bot.send_message(chat_id=call.message.chat.id, text="""Но… это не просто познакомиться 😏 в конце расскажу, что придумал))
<tg-spoiler>не профуфукай</tg-spoiler>
Играем?""", reply_markup=markup_da)


    if call.data == 'games':
        await st.step2.set()
        await bot.send_message(chat_id=call.message.chat.id, text="""Зовут меня Никола, можно просто Коля, Колян, или Одноус)) На данный момент тусуюсь в Узбекистане, 25 лет 

А тебя как звать? Сколько лет? Где живёшь?

<i>Отвечай прям сюда в бота, в одном сообщении)👇</i>""")

    if call.data == 'program':
        await bot.send_message(text="""Не буду долго тянуть, скажу прямо.

Приглашаю тебя на workshop, по модели «Tgstart»

Структура программы, и что будем делать?

<code>Жми на кнопку 👇</code>""", chat_id=call.message.chat.id, reply_markup=markup_workshop)

    if call.data == 'workshop':
        await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=490,
                               caption="""✔️Вместе соберём правильный, стартовый телеграм канал.

✔️Пройдёмся и разберём все детали.

✔️На выходе у тебя будет канал  и понимание что дальше делать.

🔥 Без воды, только мясо)

Стартуем сегодня, через 5 минут 

Жми на кнопку👇""", reply_markup= markup_member)

    if call.data == 'member':
        await bot.send_message(text="""Отлично 👍 

Такс, теперь пройдём мини регистрацию.

С какой ты страны?""",chat_id= call.message.chat.id, reply_markup=markup_country)



    if call.data == 'ru': #Россия
        await bot.delete_message(chat_id=call.message.chat.id, message_id= call.message.message_id)
        update_country(id = call.message.chat.id, country= call.data)
        await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=498,caption="""Это мой тг - https://t.me/rilttok""")

    if call.data == 'bel': #Беларусь
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        update_country(id = call.message.chat.id, country= call.data)
        await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=498,caption="""Это мой тг - https://t.me/rilttok""")
    if call.data == 'uk': #Украина
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        update_country(id = call.message.chat.id, country= call.data)
        await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=498, caption="""Это мой тг - https://t.me/rilttok""")
    if call.data == 'another_country': #Другая страна
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        update_country(id = call.message.chat.id, country= call.data)
        await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=498,caption="""Это мой тг - https://t.me/rilttok""")


    if call.data == 'kz' or call.data == 'kr' or call.data == 'uzb': #Казахстан. Кыргызстан. Узбекистан +
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        update_country(id = call.message.chat.id, country= call.data)
        await bot.send_message(text = f"""Отлично 👍 
Последний этап:

<b>Чтобы получить доступ на workshop, подпишись на каналы ⬇️ 

1) {name_channel_1[8:]}
2) {name_channel_2[8:]}
3) {name_channel_3[8:]}
4) {name_channel_4[8:]}</b>

После того как подпишешься, жми на кнопку «Готово» . Бот проверит и даст тебе доступ!""",chat_id=call.message.chat.id, disable_web_page_preview=True,reply_markup=markup_ready)
        await asyncio.sleep(3)
        await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=515)

    if call.data == 'ready':
        id_list = cheak_chat_id()

        try:
            proverka1 = (await bot.get_chat_member(chat_id=id_list[0], user_id=call.message.chat.id)).status
        except:
            proverka1 = 'member'

        try:  # Канал 2
            proverka2 = (await bot.get_chat_member(chat_id=id_list[1], user_id=call.message.chat.id)).status
        except:
            proverka2 = 'member'

        try:  # Канал 3
            proverka3 = (await bot.get_chat_member(chat_id=id_list[2], user_id=call.message.chat.id)).status
        except:
            proverka3 = 'member'

        try:  # Канал 3
            proverka4 = (await bot.get_chat_member(chat_id=id_list[3], user_id=call.message.chat.id)).status
        except:
            proverka4 = 'member'

        if (proverka1 == 'member' and proverka2 == 'member' and proverka3 == 'member' and proverka4 == 'member') or proverka1 == 'administrator' or proverka2 == 'administrator' or proverka3 == 'administrator' or proverka4 == 'administrator' or proverka1 == 'creator' or proverka2 == 'creator' or proverka3 == 'creator' or proverka4 == 'creator':  # Человек прошел все 3 проверки
            country = (get_country(call.message.chat.id))[0]
            markup_url = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Workshop', url= f'https://t.me/WorkShopTGbot?start={country}')
            markup_url.add(bat_a)


            await bot.send_message(chat_id= call.message.chat.id, text = """🔥 Погнали на workshop

С каналов не отписывайся, они нам пригодятся ещё.

Жми 👇""",reply_markup= markup_url)

        else:
            await bot.send_message(chat_id=call.message.chat.id , text=f"""❌ Подписки нет

<b>Чтобы получить доступ на workshop, подпишись на каналы ⬇️ 

1) {name_channel_1[8:]}
2) {name_channel_2[8:]}
3) {name_channel_3[8:]}
4) {name_channel_4[8:]}</b>

После того как подпишешься, жми на кнопку «Готово» . Бот проверит и даст тебе доступ!""",reply_markup=markup_ready,disable_web_page_preview=True)


    await bot.answer_callback_query(callback_query_id=call.id)





@dp.message_handler(state=st.step2, content_types=['text', 'photo', 'video', 'video_note', 'voice'])  # Предосмотр поста
async def step2(message: types.Message, state: FSMContext):
    await state.finish()
    await asyncio.sleep(1)
    await bot.copy_message(chat_id=message.chat.id, from_chat_id=content_chat, message_id=448)
    await asyncio.sleep(3)
    await message.answer(text="""Так, мини рассказ:

Начал свой путь в интернет- заработке с 2018 года. В общем не вчера пришёл.

Мини история:

В 19 лет открыл спортивно танцевальный комплекс) первое крупное знакомство с оффлайн бизнесом. Год занимался, потом вышел с дела, перешёл только на онлайн)

В 21 год занимался:
SMM/ Aрбитраж трафика/ Tаргет/Блогинг/ Фрилансил, брал заказы.
В среднем делал 2к$ 

В 24 года 
Создал команду по привлечению подписчиков в тг каналы.
Привлекли более 3х млн аудитории.
Заработано чистыми больше 30к$ 
Так же вкачал:
Тг бот - 1.2млн аудитории
Тг каналы- 120к, 60к, и мелких по 30к.
Инста - 60к

Все было прокачано и продано скупщикам, примерно за 15к$ +
Весь этот движ сделан за 6 месяцев в 2021году)

Сейчас, на данный момент ничего не делаю, по кайфу обучением занимаюсь, инвестирую в людей, на Релаксе короче)""")

    await asyncio.sleep(3)
    await message.answer(text="""А у тебя какой был опыт? Чем сейчас занимаешься?)""")
    await st.step3.set()


@dp.message_handler(state=st.step3, content_types=['text', 'photo', 'video', 'video_note', 'voice'])  # Предосмотр поста
async def step3(message: types.Message, state: FSMContext):
    await state.finish()
    await asyncio.sleep(1)
    await bot.copy_message(chat_id=message.chat.id,from_chat_id=content_chat,message_id=455)
    await asyncio.sleep(3)
    await message.answer(text="""Едим дальше 🤙

<b>Что получаеться лучше всего?</b>""")
    await asyncio.sleep(2)
    await message.answer(text="""Лучше всего у меня получаеться создавать команды и немного наставлять людей)

Вот надавал советов 17-ти летнему пацану, он заработал пол ляма, можешь посмотреть - https://t.me/rilttok/246 
Сейчас мне помогает + своё мутит)

Так же хорошо выходит организовывать, раньше собирал танцоров, сейчас людей, которые хотят фигачить в инэте)""",disable_web_page_preview=True)

    await asyncio.sleep(3)
    await message.answer(text="""А у тебя что прёт лучше всего?""")

    await st.step4.set()


@dp.message_handler(state=st.step4, content_types=['text', 'photo', 'video', 'video_note', 'voice'])  # Предосмотр поста
async def step4(message: types.Message, state: FSMContext):
    await state.finish()
    await asyncio.sleep(1)
    await bot.copy_message(chat_id=message.chat.id,from_chat_id=content_chat,message_id=464)
    await asyncio.sleep(3)
    await message.answer(text="""🤙 Двигаемся некст, последний вопрос) 

<b>Что вообще хочешь? Планы/цели/желания))</b>""")
    await asyncio.sleep(2)
    await message.answer(text="""За себя скажу следующее

Я хочу просто делать то, что нравится, не париться и передавать людям свой вайб, сегодня постараюсь прям афигенно до тебя всё донести, дать осознанность, понимание, уверен получится)))

Цель у меня - заполнить 4 сферы на 100% (здоровье, бизнес, семья, вера)
Великих планов нет, ставлю короткие задачи, потом добиваюсь, либо не добиваюсь, и дальше кайфую)""")

    await asyncio.sleep(3)
    await message.answer(text="""А ты что хочешь? Цели какие?""")
    await st.step5.set()


@dp.message_handler(state=st.step5, content_types=['text', 'photo', 'video', 'video_note', 'voice'])  # Предосмотр поста
async def step5(message: types.Message, state: FSMContext):
    await state.finish()
    await asyncio.sleep(1)
    await message.answer(text="Вот и познакомились, твои ответы буду читать лично.")
    await asyncio.sleep(2)
    await bot.copy_message(chat_id=message.chat.id, from_chat_id=content_chat, message_id=474)
    await asyncio.sleep(3)

    await message.answer(text="""Смотри, я частенько мучу разные проекты, и мне иногда нужны люди, либо которые что-то умеют делать, или просто прикольные)

Возможно по сотрудничаем 😉

<b>А сейчас жми на кнопку и погнали уже по делу👇</b>""", reply_markup=markup_go)