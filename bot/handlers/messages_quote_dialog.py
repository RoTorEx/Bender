from aiogram import F, Router
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from sqlalchemy.ext.asyncio import AsyncSession

from bot.config.constants import TgBot
from bot.database.reader import read_random_quote
from bot.database.writer import write_new_customer, write_new_quote
from bot.keyboards.quote import msg_new_author_kb, msg_new_quoute_kb, quote_menu
from bot.state.quote_dialog import AddQuote
from bot.utils.message_cleaner import drop_message, drop_messages
from bot.utils.user_to_string import make_customer_string


router = Router()


@router.message(F.text == "Random quote", content_types="text")
async def msg_get_random_quote(message: Message, session: AsyncSession) -> None:
    """Press 'Get quote' bot return random quote from database."""
    answer = await read_random_quote(session)
    await message.answer(answer)


@router.message(F.text == "Add quote", content_types="text")
async def msg_add_quote(message: Message, state: FSMContext) -> None:
    """Press 'Add quote' bot start FSM to get quote from customer and write it to collection."""
    data = {"dropping": [message.message_id]}

    await state.set_data(data)
    await state.set_state(AddQuote.enter_quote)
    await message.answer("Enter your qoute please.", reply_markup=ReplyKeyboardRemove())


@router.message(AddQuote.enter_quote)
async def msg_new_quoute(message: Message, state: FSMContext) -> None:
    """Enter quote to bot."""
    data = await state.get_data()
    if message.from_user:   # Checking for None
        data["quote"] = message.text
        data["quote_sender_id"] = message.from_user.id
        data["quote_author"] = {
            "id": message.from_user.id,
            "first_name": message.from_user.first_name,
            "last_name": message.from_user.last_name,
            "username": message.from_user.username,
        }

    await state.set_data(data)
    await state.set_state(AddQuote.enter_author)
    await message.answer(
        "Now you enter the author's name of previous quote or use buttons below.",
        reply_markup=msg_new_quoute_kb(),
    )


@router.message(AddQuote.enter_author)
async def msg_new_author(message: Message, state: FSMContext) -> None:
    """Enter quote's author to bot."""
    data = await state.get_data()

    if message.text == "This is my quote!":
        data["author"] = make_customer_string(data["quote_author"])

    elif message.text == "Enter without author.":
        data["author"] = "Unknown author"

    else:
        data["author"] = message.text

    await state.set_data(data)
    await state.set_state(AddQuote.enter_confirm)
    await message.answer(
        f"Allright here?\n\n```\n{data['quote']}\n```\n© {data['author']}",
        reply_markup=msg_new_author_kb(),
    )


@router.message(AddQuote.enter_confirm)
async def msg_new_confirmation(message: Message, state: FSMContext, session: AsyncSession) -> None:
    """Verification and confirmation of a previously created quote."""
    data = await state.get_data()

    if message.text == "Yes alright. Save it!":
        data["dropping"].extend([message.message_id])

        await write_new_quote(data, session)  # Write quote to database
        await state.clear()
        await message.answer("New quote was added to collection!", reply_markup=quote_menu())
        await drop_messages(message.chat.id, data["dropping"])  # Drop extra FSM messages from chat

    elif message.text == "Change quote.":
        await state.set_state(AddQuote.enter_quote)
        await message.answer("Please change your quote.", reply_markup=ReplyKeyboardRemove())

    elif message.text == "Change author.":
        await state.set_state(AddQuote.enter_author)
        await message.answer("Please change quote's author.", reply_markup=msg_new_quoute_kb())

    elif message.text == "No, I changed my mind. Cancel everything.":
        data["dropping"].extend([message.message_id + 1])

        await state.clear()
        await message.answer("Returning to menu.", reply_markup=quote_menu())
        await drop_messages(message.chat.id, data["dropping"])  # Drop extra FSM messages from chat

    else:
        await drop_message(message.chat.id, message.message_id)  # Drop non handled messages in state


@router.message(F.text == "Forward quote", content_types="text")
async def msg_forward_quote(message: Message, state: FSMContext) -> None:
    """Press 'Add quote' bot start FSM to get quote from customer and write it to collection."""
    data = {"dropping": [message.message_id]}

    await state.set_data(data)
    await state.set_state(AddQuote.forward_quote)
    await message.answer(
        "Now forward somebody message to me.\n<b>I can process messages from users who have open accounts!</b>",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(AddQuote.forward_quote)
async def msg_add_forward_quote(message: Message, state: FSMContext, session: AsyncSession) -> None:
    """Write forward message to quote collection."""
    if message.forward_from is None:
        await drop_message(message.chat.id, message.message_id)

    else:
        if message.forward_from.id not in TgBot.customer_list:
            await write_new_customer(message.forward_from, session)

        data = await state.get_data()
        if message.from_user and message.forward_from:
            data["dropping"].extend([message.message_id])
            data["quote"] = message.text
            data["quote_sender_id"] = message.from_user.id
            data["quote_author"] = {
                "id": message.forward_from.id,
                "first_name": message.forward_from.first_name,
                "last_name": message.forward_from.last_name,
                "username": message.forward_from.username,
            }
            data["author"] = make_customer_string(data["quote_author"])

        await write_new_quote(data, session)  # Write quote to database
        await state.clear()
        await message.answer("Forwarded quote was added to collection!", reply_markup=quote_menu())
        await drop_messages(message.chat.id, data["dropping"])  # Drop extra FSM messages from chat
