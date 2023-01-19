from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
import fuction_bot as fb


class FSMAdmin(StatesGroup):
    id_user = State()


@dp.callback_query_handler(lambda c: c.data =="add", state=None)
async def app_user_id(call: types.callback_query):
    await FSMAdmin.id_user.set()
    await with State.next()
    await bot.send_message(call.message.chat.id, "Видите id пользователя которого хотите добавить")


@dp.message_handler(state=FSMAdmin.price)
async def seve_user(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)
    async with state.proxy() as data:
        fb.add_user(data)
    await state.finish()