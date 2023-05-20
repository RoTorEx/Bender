from aiogram import Router
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from src.config import build_logger
from src.components.keyboards import buttons_menu
from src.components.states import MenuState


logger = build_logger(__name__)
commands_router = Router()


@commands_router.message(commands=["start"])
async def cmd_start(message: Message) -> None:
    """/start -> add new customer and start bot."""
    if message.from_user:  # Checking for None
        await message.answer(f"Nice to see you, {message.from_user.first_name}.\nEnter '/menu' to continue.")

    else:
        await message.answer("Hello %username%.\nEnter '/menu' to continue.")


@commands_router.message(commands=["menu"])
async def cmd_menu(message: Message, state: FSMContext) -> None:
    """/menu -> add menu buttons & clean state."""
    await state.clear()
    await state.set_state(MenuState.start_menu)
    await message.answer("Here are menu buttons!", reply_markup=buttons_menu())


@commands_router.message(commands=["clean"])
async def cmd_cancel(message: Message, state: FSMContext) -> None:
    """/clean - remove menu buttons."""
    await state.clear()
    await state.set_state(MenuState.end_menu)
    await message.answer("Cleaning...", reply_markup=ReplyKeyboardRemove())
