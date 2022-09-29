from aiogram import Router
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from sqlalchemy.ext.asyncio import AsyncSession

from bot.config.logger_builder import build_logger
from bot.database.writer import write_new_customer
from bot.keyboards.quote import quote_menu
from bot.utils.message_cleaner import drop_messages


logger = build_logger(__name__)
router = Router()


@router.message(commands=["start"])
async def cmd_start(message: Message, session: AsyncSession) -> None:
    """/start -> add new customer and start bot"""
    if message.from_user:  # Checking for None
        await write_new_customer(message.from_user, session)
        await message.answer(f"Nice to see you, {message.from_user.first_name}.\nEnter '/menu' to continue.")

    else:
        await message.answer("Hello %username%.\nEnter '/menu' to continue.")


@router.message(commands=["menu"])
async def cmd_menu(message: Message, state: FSMContext) -> None:
    """/menu -> add menu buttons & clean state"""
    await state.clear()
    await message.answer("Now you see menu buttons.\nEnter '/cancel' to remove menu.", reply_markup=quote_menu())


@router.message(commands=["cancel"])
async def cmd_cancel(message: Message, state: FSMContext) -> None:
    """/cancel -> downgrade finite-state machine & hide menu"""
    data = await state.get_data()
    if "dropping" in data:
        data["dropping"].extend([message.message_id])
        await drop_messages(message.chat.id, data["dropping"])  # Drop extra FSM messages from chat
    await state.clear()
    await message.answer("Cleaning...\nEnter '/menu' add menu.", reply_markup=ReplyKeyboardRemove())
