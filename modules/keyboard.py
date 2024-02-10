import aiogram

button_admin = aiogram.types.KeyboardButton(text = "Адміністратор", callback_data="адмін")

button_client = aiogram.types.KeyboardButton(text = "Клієнт", callback_data = "клієнт")

Keyboard = aiogram.types.ReplyKeyboardMarkup(keyboard = [[button_admin, button_client]])


button_buy = aiogram.types.InlineKeyboardButton(text = "Купити", callback_data="купити")

button_decline = aiogram.types.InlineKeyboardButton(text = "Вилучити", callback_data = "Вилучити")

button_confirm = aiogram.types.InlineKeyboardButton(text = "Підтвердити", callback_data = "підтвердити")



button_option = aiogram.types.InlineKeyboardButton(text = "Параметр", callback_data = "параметр")

Keyboard2 = aiogram.types.InlineKeyboardMarkup(inline_keyboard = [[button_buy,  button_decline,button_confirm, button_option]])

    
