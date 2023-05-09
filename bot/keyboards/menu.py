from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def buttons_menu() -> ReplyKeyboardMarkup:
    kb = [
        # [KeyboardButton(text="Awards")]
        [KeyboardButton(text="Vocabulary"), KeyboardButton(text="Quotes")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="Choose.")
    return keyboard
