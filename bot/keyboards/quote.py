from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def quote_menu() -> ReplyKeyboardMarkup:
    kb = [
        [KeyboardButton(text="Add quote"), KeyboardButton(text="Forward quote")],
        [KeyboardButton(text="Random quote")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="Choose.")
    return keyboard


def msg_new_quoute_kb() -> ReplyKeyboardMarkup:
    kb = [
        [KeyboardButton(text="This is my quote!"), KeyboardButton(text="Enter without author.")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="Who author?")

    return keyboard


def msg_new_author_kb() -> ReplyKeyboardMarkup:
    kb = [
        [KeyboardButton(text="Yes alright. Save it!")],
        [KeyboardButton(text="Change quote."), KeyboardButton(text="Change author.")],
        [KeyboardButton(text="No, I changed my mind. Cancel everything.")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="Who author?")

    return keyboard
