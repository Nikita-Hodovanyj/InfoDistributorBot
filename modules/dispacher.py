import aiogram
import asyncio
import sqlite3
import os
import modules.keyboard
from aiogram import (Bot, 
                     types, 
                     Dispatcher
                    
)
from aiogram.filters import (Command, 
                             CommandStart
)

image_burger = aiogram.types.FSInputFile(path=os.path.abspath(__file__ + "/../images/burger.jpg"))

api_token = aiogram.Bot(token = "6590152148:AAFnT6WZwdJEh2iusJ82gCmJD-lKmn7sol4")

dispatcher = Dispatcher()

connection = sqlite3.connect("USERS.db")
cursor = connection.cursor()

def create_users_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
        name TEXT,
        password TEXT 
        )
    """)


create_users_table()

connection.commit()

connection = sqlite3.connect("ADMINS.db")
cursor = connection.cursor()

def create_admins_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ADMIN (
        name TEXT,
        email TEXT,
        phone TEXT,
        password TEXT 
        )
    """)

create_admins_table()

connection.commit()

@dispatcher.message(CommandStart())
async def bot_start(message: types.Message):
    await message.answer("Привіт, користувачу, обери хто ти 👋", reply_markup = modules.keyboard.Keyboard)

user_state = {}
user_data = {}
user_state_k = {}
user_data_k = {}
@dispatcher.message()
async def message_handler(message:aiogram.types.Message):
    global user_state
    user_id = message.from_user.id
    if message.text == "Адміністратор":
        delate = aiogram.types.ReplyKeyboardRemove()
        await message.answer("Введіть email: ", reply_markup = delate)
        user_state[user_id] = 'email'
    elif user_state.get(user_id) == 'email':
        user_data['email'] = message.text
        delate = aiogram.types.ReplyKeyboardRemove()
        await message.answer("Введіть номер телефона: ", reply_markup = delate)
        user_state[user_id] = 'phone'
    elif user_state.get(user_id) == 'phone':
        user_data['phone'] = message.text
        delate = aiogram.types.ReplyKeyboardRemove()
        await message.answer("Введіть ім'я: ", reply_markup = delate)
        user_state[user_id] = 'name'
    elif user_state.get(user_id) == 'name':
        user_data['name'] = message.text
        delate = aiogram.types.ReplyKeyboardRemove()
        await message.answer("Введіть пароль: ", reply_markup = delate)
        user_state[user_id] = 'password'
    elif user_state.get(user_id) == 'password':
        user_data['password'] = message.text
        delate = aiogram.types.ReplyKeyboardRemove()
        await message.answer("Всі дані успішно введені!", reply_markup = delate)
        user_state[user_id] = 'done'
        cursor.execute("INSERT INTO ADMIN (name, email, phone, password) VALUES (?, ?, ?, ?)", (user_data['name'], user_data['email'], user_data['phone'], user_data['password']))
        connection.commit()
        await message.answer_photo(photo = image_burger, reply_markup = modules.keyboard.Keyboard2)  
        
        
        
    elif message.text =="Клієнт":
        # await message.edit_reply_markup(reply_markup=None)
        delate = aiogram.types.ReplyKeyboardRemove()
        await message.answer("Введіть ім'я: ", reply_markup = delate)
        user_state_k[user_id] = 'name_k'
    elif user_state_k.get(user_id) == 'name_k':
        user_data_k['name_k'] = message.text
        delate = aiogram.types.ReplyKeyboardRemove()
        await message.answer("Введіть пароль: ", reply_markup = delate)
        user_state_k[user_id] = 'password_k'
    elif user_state_k.get(user_id) == 'password_k':
        user_data_k['password_k'] = message.text
        delate = aiogram.types.ReplyKeyboardRemove()
        await message.answer("Користувач успішно доданий!", reply_markup = delate)
        user_state_k[user_id] = 'done_k'
        cursor.execute("INSERT INTO users (name, password) VALUES (?, ?)", (user_data_k['name_k'], user_data_k['password_k']))
        connection.commit()
        await message.answer_photo(photo = image_burger, reply_markup = modules.keyboard.Keyboard2)





