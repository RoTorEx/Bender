from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def awards_menu() -> ReplyKeyboardMarkup:
    kb = [
        [KeyboardButton(text="Write"), KeyboardButton(text="Read")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="Let's write day awards!")

    return keyboard


def msg_confirm_awards_kb() -> ReplyKeyboardMarkup:
    kb = [
        [KeyboardButton(text="Yeap, save it!")],
        [KeyboardButton(text="Adjust it.")],
        [KeyboardButton(text="No, I changed my mind. Return menu.")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="Correct?")

    return keyboard
