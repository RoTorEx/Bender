from aiogram.dispatcher.fsm.state import State, StatesGroup


class QuoteState(StatesGroup):
    start_quote = State()
    forward_quote = State()
    enter_quote = State()
    enter_author = State()
    enter_confirm = State()
