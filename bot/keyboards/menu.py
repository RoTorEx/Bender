from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def buttons_menu() -> ReplyKeyboardMarkup:
    kb = [
        [KeyboardButton(text="Awards")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder=":D")

    return keyboard
