import time

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from time import sleep


from aiogram.dispatcher.filters.state import State, StatesGroup

import config
import fuction_bot as fb
from keyboard import markup, ml, start, authorized, admin, stop
import users as us


stprage = MemoryStorage()
bot = Bot(config.token)
dp = Dispatcher(bot=bot, storage=stprage)


class FSMAdmin(StatesGroup):
    id_user = State()
p = 0

@dp.callback_query_handler(lambda c: c.data == "add", state=None)
async def app_user_id(call: types.callback_query):
    await FSMAdmin.id_user.set()
    await bot.send_message(call.message.chat.id, "Видите id пользователя которого хотите добавить")


@dp.message_handler(content_types=['id_user'], state=FSMAdmin.id_user)
async def save_user(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id_user'] = message.text
    await FSMAdmin.next()
    await bot.send_message(message.chat.id, "Так держать")
    async with state.proxy() as data:
        await message.reply(data)
        us.add_user(int(data))
    await state.finish()


@dp.message_handler(commands=['start'])
# """Привествие нового плользователя"""
async def starts(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user = fb.authorized(user_id)
    if user == True:
        await bot.send_message(message.chat.id, "hi", reply_markup=authorized)
    else:
        await bot.send_message(message.chat.id, "Приветствую, подойти на запрос на регистрацию", reply_markup=start)


@dp.callback_query_handler(lambda c: c.data == "Authorization")  # запрос на регистрацию
async def authorizations(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    ban = us.examination_ban(call.from_user.id)
    if ban == None:
        user = fb.authorized(call.from_user.id)
        last_name = call.from_user.last_name
        if last_name == None:
            last_name = "..."
        message = fb.authorization(call.from_user.id, call.from_user.first_name, last_name)
        await bot.send_message(call.message.chat.id, "Запрост содан, ожидайте потверждения")


@dp.callback_query_handler(lambda c: c.data == "user")  # После авторизации
async def authorizeds(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    user = fb.authorized(call.from_user.id)
    if user == True:
        user_name = call.from_user.first_name
        await bot.send_message(call.message.chat.id, "Приветствую " + user_name, reply_markup=ml)
        await bot.send_message(call.message.chat.id, "Готов к работе!", reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "but_test")  # Проверка доступности сетевых папок
async def test(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    ban = us.examination_ban(call.from_user.id)
    if ban == None:
        user = fb.authorized(call.from_user.id)
        if user == True:
            messages = fb.test()
            for message in messages:
                await bot.send_message(call.message.chat.id, message)


@dp.message_handler(content_types=['text'])  # Для клавиатуры
async def test_text(message: types.Message):
    users = fb.authorized(message.from_user.id)
    if users == True:
        if message.text == "Проверка папок":
            user_id = message.from_user.id
            ban = us.examination_ban(user_id)
            if ban == None:
                messag = fb.test()
                for messages in messag:
                    await bot.send_message(message.chat.id, messages)
        if message.text == "Проверка всех серверов":
            user_id = message.from_user.id
            ban = us.examination_ban(user_id)
            if ban == None:
                messages = fb.ping_all_server()
                for name, report in messages.items():
                    messag = name + "-" + report
                    await bot.send_message(message.chat.id, messag)
        if message.text == "naglfar":
            """Типо пароль для роботы с ботом"""
            user_name = message.from_user.first_name
            await bot.send_message(message.chat.id, "Приветствую " + user_name, reply_markup=ml)
            await bot.send_message(message.chat.id, "Готов к работе!", reply_markup=markup)
        if message.text == "1234":
            """защита от злоумышлеников"""
            user_id = message.from_user.id
            user_name = message.from_user.first_name
            user_last_name = message.from_user.last_name
            us.ban(user_id, user_name, user_last_name)
            await bot.send_message(message.chat.id, "I'm sorry, you're banned!")
        if message.text == "admin":
            user_id = message.from_user.id
            users_list = us.users(user_id)
            for user in users_list:
                await bot.send_message(message.chat.id, user, reply_markup=admin)


@dp.callback_query_handler(lambda c: c.data == "but_ping")
# """Ping Серверов"""
async def ping(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    ban = us.examination_ban(call.from_user.id)
    if ban == None:
        user = fb.authorized(call.from_user.id)
        if user == True:
            messages = fb.ping_all_server()
            for name, report in messages.items():
                message = name + "-" + report
                await bot.send_message(call.message.chat.id, message)




executor.start_polling(dp)


