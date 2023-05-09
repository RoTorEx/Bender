from aiogram.dispatcher.fsm.state import State, StatesGroup


class VocabularyState(StatesGroup):
    start_vocabulary = State()
