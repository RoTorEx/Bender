from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def awards_menu() -> ReplyKeyboardMarkup:
    kb = [
        [KeyboardButton(text="Write"), KeyboardButton(text="Read")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    return keyboard
