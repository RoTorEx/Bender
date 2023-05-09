from aiogram import F, Router
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from bot.keyboards import awards_menu, buttons_menu, msg_confirm_awards_kb
from bot.services import AwardsService
from bot.states import AwardsState, MenuState


service = AwardsService()
awards_router = Router()


@awards_router.message(MenuState.start_menu, F.text == "Awards", content_types="text")
async def msg_start_awards_dialog(message: Message, state: FSMContext) -> None:
    """Starts Awards dialog."""
    await state.set_state(AwardsState.start_awards)
    await message.answer(
        "Yoopee! Day Awards! ^^",
        reply_markup=awards_menu(),
    )


@awards_router.message(AwardsState.start_awards, F.text == "Read", content_types="text")
async def msg_read_awards(message: Message) -> None:
    # await service.get_data_from_sheet()
    await message.answer("Not implemented :'(")


@awards_router.message(AwardsState.start_awards, F.text == "Write", content_types="text")
async def msg_enter_awards(message: Message, state: FSMContext) -> None:
    await state.set_state(AwardsState.enter_awards)
    await message.answer("Enter your day awards please.", reply_markup=ReplyKeyboardRemove())


@awards_router.message(AwardsState.enter_awards, content_types="text")
async def msg_confirm_awards(message: Message, state: FSMContext) -> None:
    data = await state.get_data()

    data["text"] = message.text
    data["sender"] = {
        "id": message.from_user.id,
        "first_name": message.from_user.first_name,
        "last_name": message.from_user.last_name,
        "username": message.from_user.username,
    }

    await state.set_data(data)
    await state.set_state(AwardsState.confirm_awards)
    await message.answer(f"Is all right here??\n\n```\n{message.text}\n```", reply_markup=msg_confirm_awards_kb())


@awards_router.message(AwardsState.confirm_awards)
async def msg_write_awards(message: Message, state: FSMContext) -> None:
    data = await state.get_data()

    if message.text == "Yeap, save it!":
        day_awards = data.get("text")
        await service.write_data_in_sheet(day_awards)
        await state.clear()
        await message.answer("Wrote it!", reply_markup=buttons_menu())

    elif message.text == "Adjust it.":
        await state.set_state(AwardsState.enter_awards)
        await message.answer("Please enter your edited day awards ^^", reply_markup=ReplyKeyboardRemove())

    elif message.text == "No, I changed my mind. Cancel everything.":
        await state.clear()
        await message.answer("Returning to menu.", reply_markup=awards_menu())
