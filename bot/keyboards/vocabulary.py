from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def vocabulary_menu() -> ReplyKeyboardMarkup:
    kb = [
        [KeyboardButton(text="Write"), KeyboardButton(text="Learn")],
        [KeyboardButton(text="Add to vocabulary")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="Choose.")
    return keyboard
