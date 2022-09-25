from aiogram.dispatcher.fsm.state import State, StatesGroup


class AddQuote(StatesGroup):
    forward_quote = State()
    enter_quote = State()
    enter_author = State()
    enter_confirm = State()
