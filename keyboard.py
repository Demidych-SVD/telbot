from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

start = InlineKeyboardMarkup(row_width=1)
authorized = InlineKeyboardMarkup(row_width=1)
stop = InlineKeyboardMarkup(row_width=1)
markup = InlineKeyboardMarkup(row_width=2)
admin = InlineKeyboardMarkup(row_width=2)
ml = ReplyKeyboardMarkup(resize_keyboard=True)
button0 = InlineKeyboardButton(text="Проверка папок", callback_data="but_test")
button1 = InlineKeyboardButton(text="Проверка всех серверов", callback_data="but_ping")
adm0 = InlineKeyboardButton(text="Добавить", callback_data="add")
app = InlineKeyboardButton(text="app", callback_data='add_ok')
adm1 = InlineKeyboardButton(text="Отказаь", callback_data="refuse")
authorization = InlineKeyboardButton(text="Запрос на регистрацию", callback_data="Authorization")
authorization1 = InlineKeyboardButton(text="Нажми на меня ☺", callback_data="user")
b0 = KeyboardButton("Проверка папок")
b1 = KeyboardButton("Проверка всех серверов")
markup.add(button0, button1)
ml.add(b0).insert(b1)
authorized.add(authorization1)
start.add(authorization)
admin.add(adm0)