from aiogram import F, Router
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from bot.handlers.commands import buttons_menu
from bot.keyboards.awards import awards_menu
from bot.services.awards import AwardsService
from bot.states.awards_state import AwardsState
from bot.states.menu_state import MenuState


router = Router()
service = AwardsService()


@router.message(MenuState.start_menu, F.text == "Awards", content_types="text")
async def msg_start_awards_dialog(message: Message, state: FSMContext) -> None:
    """Starts Awards dialog."""
    await state.set_state(AwardsState.start_awards)
    await message.answer(
        "Yoopee! Day Awards! ^^",
        reply_markup=awards_menu(),
    )


@router.message(AwardsState.start_awards, F.text == "Read", content_types="text")
async def msg_read_awards(message: Message, state: FSMContext) -> None:
    await service.get_data_from_sheet()
    await message.answer("Not implemented :'(")


@router.message(AwardsState.start_awards, F.text == "Write", content_types="text")
async def msg_enter_awards(message: Message, state: FSMContext) -> None:
    await state.set_state(AwardsState.enter_awards)
    await message.answer("Enter your day awards please.", reply_markup=ReplyKeyboardRemove())


@router.message(AwardsState.enter_awards, content_types="text")
async def msg_confirm_awards(message: Message, state: FSMContext) -> None:
    # await state.set_state(AwardsState.confirm_awards)
    # await message.answer("Enter your day awards please.", reply_markup=ReplyKeyboardRemove())

    await state.set_state(AwardsState.confirm_awards)
    await message.answer(f"Allright here?\n\n```\n{message.text}\n```", reply_markup=None)


@router.message(AwardsState.confirm_awards, F.text == "Yeap!", content_types="text")
async def msg_write_awards(message: Message, state: FSMContext) -> None:
    await service.write_data_in_sheet(message.text)
    await state.clear()
    await state.set_state(MenuState.start_menu)
    await message.answer("Wrote it!", reply_markup=buttons_menu())
