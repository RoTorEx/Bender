from aiogram.dispatcher.fsm.state import State, StatesGroup


class MenuState(StatesGroup):
    start_menu = State()
    end_menu = State()
