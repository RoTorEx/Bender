from aiogram.dispatcher.fsm.state import State, StatesGroup


class AwardsState(StatesGroup):
    start_awards = State()
    enter_awards = State()
    confirm_awards = State()
